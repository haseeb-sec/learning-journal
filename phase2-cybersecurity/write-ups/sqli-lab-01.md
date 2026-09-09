# SQL Injection Lab 01

A practical PortSwigger Web Security Academy lab demonstrating SQL injection through a vulnerable product category query.

**Official Lab:** https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

## 1. What the Lab Was

This lab was a practical SQL injection exercise from PortSwigger Web Security Academy.

The application displayed products by category. When I selected the **Accessories** category, the browser sent a GET request containing the category in the URL:

```http
GET /filter?category=Accessories HTTP/2
```

The important part of the lab was that the application was taking the value of the `category` parameter and using it unsafely in a SQL query.

The objective was to understand whether I could modify the parameter so that the SQL query behaved differently from what the application intended.

This lab helped me connect several concepts that I had previously learned separately: HTTP requests, query parameters, proxies, Burp Suite, Repeater, SQL syntax, and SQL injection.

## 2. Tools I Used

### Browser

I used the browser to interact with the lab normally. Selecting a product category caused the browser to send an HTTP GET request to the server.

### Burp Suite

Burp Suite acted as an intercepting proxy between my browser and the lab server.

The basic flow was:

```text
Browser → Burp Suite → Lab Server
Browser ← Burp Suite ← Lab Server
```

This allowed me to see the HTTP requests and responses instead of treating the communication as something hidden inside the browser.

### HTTP History

Burp's HTTP history allowed me to inspect the requests that had passed through the proxy.

This is where I could see the request containing:

```text
/filter?category=Accessories
```

### Repeater

Repeater allowed me to take the captured request and send it again with modifications.

This was important because I could change only the parameter I was testing and repeatedly send the request without having to interact with the website normally every time.

## 3. What I Did Step by Step

### Step 1 — Normal request

I opened the lab and selected **Accessories**.

The browser sent a GET request similar to:

```http
GET /filter?category=Accessories HTTP/2
```

At this point, I understood that `category=Accessories` was a **query parameter**.

The server used this parameter to determine which products should be displayed.

### Step 2 — Inspecting the request

Because Burp Suite was configured as my proxy, the request passed through Burp.

I inspected it in HTTP history and identified the category parameter.

The important part was:

```text
?category=Accessories
```

### Step 3 — Sending the request to Repeater

I sent the request to Burp Repeater.

Repeater gave me a way to repeatedly modify and resend the same HTTP request.

This helped me understand that I was not changing the website itself. I was changing the request being sent to the server.

### Step 4 — Testing SQL injection

I modified the category value and observed how the server responded.

One important test was:

```text
category=Accessories'--
```

This showed that the input was affecting the SQL statement.

However, this test did **not** remove every condition from the query. It bypassed the later part of the query while the category condition still limited the results.

This produced **4 products**.

### Step 5 — The final injection

I then used the Repeater payload:

```text
'+OR+1=1--
```

This produced a much different result.

The application returned **20 products**.

The important difference was that this payload did not simply bypass one filter. It changed the logic of the WHERE condition so that it became true for every product, while the comment marker removed the remaining part of the SQL statement.

The 20 products included products from different categories and products that were normally hidden by the released filter.

## 4. What the Backend SQL Query Looked Like

I did not have the application's source code, so the following represents the SQL query conceptually based on the behavior observed in the lab.

Normally, the query could look like:

```sql
SELECT * FROM products
WHERE category = 'Accessories'
AND released = 1;
```

The application was effectively putting the user-controlled category value directly into the SQL statement.

When I supplied:

```text
'+OR+1=1--
```

the resulting SQL could be represented as:

```sql
SELECT * FROM products
WHERE category = '' OR 1=1--'
AND released = 1;
```

The exact formatting depends on how the backend constructs the query, but the important logic is clear.

The injected value changed the query in three parts.

### `'`

The single quote closed the SQL string that the application had started.

### `OR 1=1`

`1=1` is always true.

Therefore:

```sql
category = '' OR 1=1
```

becomes true for every row because the second condition is always true.

### `--`

The `--` begins an SQL comment.

This means the remaining part of the SQL statement is ignored by the database.

Together, these three parts changed the meaning of the original query.

## 5. Why the Attack Worked

The attack worked because the application did not properly separate **SQL code** from **user-controlled data**.

The application expected the user to provide something like:

```text
Accessories
```

Instead, I supplied SQL syntax as part of the parameter.

The application then placed that input directly into the SQL query.

This allowed my input to become part of the SQL logic itself.

The important lesson for me was that SQL injection is not simply about entering a special character.

The attacker is trying to make the database interpret part of the supplied input as SQL syntax.

The three important parts of my final payload had different jobs:

```text
'       → closes the original string
OR 1=1  → creates an always-true condition
--      → comments out the remaining query
```

## 6. Understanding the 4 vs 20 Product Result

This was one of the points that initially confused me, and understanding the difference was important.

The earlier test:

```text
category=Accessories'--
```

resulted in **4 products**.

That test interfered with the query, but it did not make the entire WHERE condition true for every product. The Accessories restriction was still effectively present.

The final Repeater payload:

```text
'+OR+1=1--
```

was different.

`OR 1=1` made the condition universally true, and `--` commented out the remaining part of the query.

Therefore, the database returned **20 products** instead of the normal 3.

So the distinction is:

```text
Accessories'--
        ↓
bypassed part of the filtering
        ↓
4 products
```

while:

```text
'+OR+1=1--
        ↓
made the condition always true
        ↓
removed the remaining query logic
        ↓
20 products
```

This was an important correction in my understanding of the lab.

## 7. How a Developer Prevents It

The primary defense against SQL injection is to use **parameterized queries / prepared statements**.

Instead of constructing SQL by directly joining user input into the query, the developer should keep the SQL statement separate from the supplied value.

Conceptually:

```sql
SELECT * FROM products
WHERE category = ?
AND released = 1;
```

The application then supplies the category as data.

If the user enters:

```text
'+OR+1=1--
```

the database treats that entire value as a string rather than interpreting the characters as SQL instructions.

This prevents the attacker from changing the structure of the SQL query through the parameter.

Other security practices can also help reduce risk:

* Use parameterized queries consistently.
* Use an ORM correctly instead of manually constructing SQL strings.
* Validate input where appropriate.
* Apply least-privilege permissions to database accounts.
* Test applications for injection vulnerabilities during development and security testing.

Input validation alone should not be treated as the primary defense. The important protection is keeping user data separate from executable SQL syntax.

## 8. OWASP Category

This vulnerability belongs to:

**OWASP Top 10 — A03:2021: Injection**

SQL injection is a classic example of an injection vulnerability because attacker-controlled input is interpreted as part of a database command.

This lab gave me a practical example of what that category actually looks like instead of only learning the definition.

## 9. MITRE ATT&CK Technique

The closest MITRE ATT&CK Enterprise technique I can identify for this scenario is:

**T1190 — Exploit Public-Facing Application**

This technique covers exploiting vulnerabilities in applications that are accessible to attackers.

SQL injection itself is a vulnerability class rather than a dedicated MITRE ATT&CK technique, so T1190 is the closest applicable technique for this lab scenario.

## 10. What Confused Me and What Became Clear

At the beginning of this exercise, I was mixing several concepts together.

I understood individual terms such as HTTP, GET, parameters, proxies, and SQL injection, but I did not initially have a complete picture of how they connected.

The lab helped me connect them as one process:

```text
Browser
   ↓
HTTP GET request
   ↓
Burp Suite proxy
   ↓
HTTP history
   ↓
Repeater
   ↓
Modified query parameter
   ↓
Vulnerable backend SQL query
   ↓
Database interprets injected SQL
   ↓
Unexpected results
```

I also had confusion about the number of products returned during the different tests.

The 4-product result and the 20-product result were not the same attack effect.

`Accessories'--` bypassed one part of the filtering while keeping the category restriction.

`'+OR+1=1--` was the full injection that made the condition always true and commented out the remaining query.

That is why the final result was **20 products**.

The biggest lesson I took from this lab is that understanding an attack requires understanding the entire chain, not just memorizing a payload.

I now understand what the browser sends, what Burp intercepts, what Repeater changes, how the parameter reaches the backend, how unsafe SQL construction allows the input to become SQL syntax, and why parameterized queries prevent the same input from changing the query's meaning.

## 11. Key Takeaways

* HTTP requests are messages sent from a client to a server.
* GET requests can contain parameters in the URL.
* A query parameter is a way of providing additional information to the server.
* Burp Suite can act as a proxy between the browser and the server.
* Repeater allows captured requests to be modified and resent.
* SQL injection happens when untrusted input can change the structure of a SQL query.
* `'`, `OR 1=1`, and `--` each played a different role in the final injection.
* The final injection returned **20 products**, not 4.
* Parameterized queries keep user input separate from SQL code.
* SQL injection belongs to OWASP A03:2021 — Injection.
* The closest MITRE ATT&CK mapping for this scenario is T1190 — Exploit Public-Facing Application.

This is my second Phase 2 cybersecurity write-up. The main goal was not just to complete the lab, but to understand what actually happened between the browser, HTTP request, proxy, vulnerable application, SQL query, and database.
