# SQL Injection Lab 03 — Determining the Number of Columns

**Platform:** PortSwigger Web Security Academy
**Topic:** SQL Injection / UNION Attack
**Lab:** SQL injection UNION attack, determining the number of columns returned by the query
**Official Lab:** https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns

## Objective

Determine how many columns are returned by the application's original SQL query using a `UNION SELECT` injection.

## What I Learned

A **SQL query** is an instruction sent to a database to retrieve or manipulate information.

A **column** is one field of data in the query result. For example:

```sql
SELECT name, price, description FROM products;
```

returns three columns: `name`, `price`, and `description`.

A `UNION` combines the results of two SQL queries. For a `UNION` to work, both queries must return the same number of columns.

## Tools Used

- **Browser:** Opened the PortSwigger lab and generated the normal request.
- **Burp Suite:** Intercepted and analyzed the HTTP request.
- **HTTP History:** Located the request containing the vulnerable `category` parameter.
- **Repeater:** Modified and resent the request with different `UNION SELECT` payloads.

The workflow was:

Browser → Burp Suite → HTTP History → Repeater

## Lab Steps

The vulnerable request was:

```text
/filter?category=Accessories
```

I sent the request to Burp Suite Repeater and tested different numbers of `NULL` values.

First:

```text
Accessories' UNION SELECT NULL--
```

This returned a **500 Internal Server Error**, showing that the number of columns did not match.

I then tested:

```text
Accessories' UNION SELECT NULL,NULL,NULL--
```

The server returned **200 OK** and the response contained an additional empty row.

## Result

The original SQL query returns **3 columns**.

Using `NULL` allowed me to test the number of columns without needing to know their data types or actual values.

## Why This Matters

Determining the column count is an important first step in a **UNION-based SQL injection**. Once the number of columns is known, an attacker can construct a UNION query with the correct number of columns and potentially retrieve data from other database tables.

## Security

The underlying vulnerability is SQL Injection caused by unsafe handling of user input in a database query.

**OWASP:** A03:2021 — Injection

## Evidence

- Vulnerable request: `/filter?category=Accessories`
- `UNION SELECT NULL` → **HTTP 500 Internal Server Error**
- `UNION SELECT NULL,NULL,NULL` → **HTTP 200 OK + additional empty row**
- Confirmed column count: **3**
- Testing tool: **Burp Suite Repeater**
- Final result: **Lab solved successfully**

## Key Takeaway

I learned that a SQL query is an instruction sent to a database, and that a UNION query must have the same number of columns as the original query. By testing `NULL` values, I determined that this application's vulnerable query returns **3 columns**.
