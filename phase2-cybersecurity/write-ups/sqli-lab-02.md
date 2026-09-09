# SQL Injection Lab 02 — Login Bypass

A practical PortSwigger Web Security Academy lab demonstrating how SQL injection can bypass authentication.

**Official Lab:** https://portswigger.net/web-security/sql-injection/lab-login-bypass

## 1. Objective

The objective was to log in as the `administrator` user without knowing the password by exploiting SQL injection in the login form.

Unlike the previous lab, the injection point was in a **POST request body** rather than a GET URL parameter.

## 2. Request Analysis

The login form submitted:

```http
POST /login HTTP/2
```

with parameters similar to:

```text
username=test&password=test
```

I captured the request through **Burp Suite**, located it in **HTTP history**, and sent it to **Repeater** so I could modify and resend it.

The workflow was:

Browser → Burp Suite → HTTP History → Repeater

## 3. SQL Injection

I changed the username parameter to:

```text
administrator'--
```

and left the password as an arbitrary value.

A likely backend query is:

```sql
SELECT * FROM users
WHERE username = 'input'
AND password = 'input';
```

After the injection, it conceptually becomes:

```sql
SELECT * FROM users
WHERE username = 'administrator'--'
AND password = 'anything';
```

The `'` closes the username string, while `--` comments out the remaining SQL. As a result, the password condition is no longer evaluated.

## 4. Evidence

Burp Repeater returned:

```http
HTTP/2 302 Found
Location: /my-account?id=administrator
```

The redirect to the administrator account confirmed that authentication had been bypassed.

I then performed the same attack through the browser and confirmed that the PortSwigger lab was **Solved**.

## 5. Why It Worked

The application treated user-controlled login data as part of a SQL statement instead of safely separating data from SQL code.

The core issue was therefore **SQL injection in an authentication query**.

## 6. Prevention

Developers should use:

* Parameterized queries / prepared statements
* Safe ORM/database APIs
* Proper input handling
* Least-privilege database accounts
* Security testing for authentication-related injection vulnerabilities

The most important defense is to ensure that user input is treated as **data**, never as executable SQL syntax.

## 7. Security Mapping

**OWASP Top 10:** A03:2021 — Injection

**MITRE ATT&CK:** T1190 — Exploit Public-Facing Application

T1190 describes exploitation of vulnerabilities in externally accessible applications. SQL injection is the vulnerability exploited in this lab rather than a dedicated ATT&CK technique itself.

## 8. What I Learned

This lab connected the SQL injection concept from the previous lab to authentication.

The main difference was the request location:

```text
Lab 01: GET → URL parameter
Lab 02: POST → request body
```

The HTTP method changes where the input is sent, but the underlying SQL injection principle remains the same.

**Key takeaway:** SQL injection can do more than manipulate search or filtering results—it can potentially bypass authentication when login input is unsafely incorporated into SQL queries.
