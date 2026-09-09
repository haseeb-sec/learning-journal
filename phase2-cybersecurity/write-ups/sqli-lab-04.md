# SQL Injection Lab 04 — Finding a Column Containing Text

## Objective

Use a UNION-based SQL injection to determine which column in the query result can display text, then make the database retrieve the required string `zaztWz`.

## Lab

**PortSwigger Web Security Academy:** SQL injection UNION attack, finding a column containing text.

## Tools Used

- **Browser:** Opened the PortSwigger lab and confirmed the normal application behavior.
- **Burp Suite:** Intercepted and analyzed the application's HTTP request.
- **Burp Proxy / HTTP history:** Captured the request containing the vulnerable `category` parameter.
- **Burp Repeater:** Modified the request and repeatedly tested SQL injection payloads.
- **HTTP response analysis:** Compared response status codes and searched the response for the required string.

## Starting Point

In the previous SQL injection UNION lab, we established that the original query returns **3 columns**.

That meant the injected `UNION SELECT` also needed to contain exactly 3 columns.

The lab required us to determine which of those columns could accept and display text.

## Testing

### 1. Test column 1

Payload:

`Accessories' UNION SELECT 'zaztWz',NULL,NULL--`

Result:

**HTTP 500 Internal Server Error**

This indicated that placing the text value in the first column was not accepted by the application's query/result structure.

### 2. Test column 2

Payload:

`Accessories' UNION SELECT NULL,'zaztWz',NULL--`

Result:

**HTTP 200 OK**

I then searched the response in Burp Repeater for `zaztWz`.

The string appeared in the response, confirming that the second column could display text.

The PortSwigger lab was then solved successfully.

## What I Learned

- A `UNION SELECT` must return the same number of columns as the original query.
- `NULL` can be used when testing column positions without knowing the exact data types.
- A `500` response can indicate that a tested column/value combination is incompatible with the query or application.
- A successful `200 OK` response alone does not prove the correct column was found. The required value must actually appear in the response.
- In this lab, **column 2 was text-compatible and visible to the user**.
- Finding a text-capable column is an important step before using UNION SQLi to retrieve useful database information.

## How the Process Worked

The overall process was:

1. Open the PortSwigger lab in the browser.
2. Use Burp Suite to capture the vulnerable request.
3. Send the request to **Repeater**.
4. Use the 3-column result from the previous lab.
5. Place `zaztWz` in different column positions while using `NULL` for the others.
6. Compare the HTTP responses.
7. Search the response for `zaztWz`.
8. Confirm the lab is solved when the string is returned.

## Security Impact

A UNION-based SQL injection can allow an attacker to manipulate the results of a database query and potentially retrieve information from other database tables.

If sensitive information is exposed, this can lead to data disclosure and further compromise.

## Prevention

- Use parameterized queries / prepared statements.
- Never concatenate untrusted user input directly into SQL queries.
- Apply least-privilege permissions to database accounts.
- Use input validation as an additional defensive layer.
- Properly handle and monitor database errors without exposing unnecessary information.

## OWASP Mapping

**OWASP Top 10: A03:2021 — Injection**

SQL injection occurs when untrusted input is interpreted as part of a database query rather than being treated strictly as data.

## AI Security Bridge

SQL injection and prompt injection are different vulnerabilities, but they share an important security principle:

**Untrusted input must not be allowed to become unintended instructions.**

In SQL injection, the target is a database query.

In prompt injection, the target is an AI model's instruction/context processing.

## Evidence

- Original query: **3 columns**
- Column 1 test: **HTTP 500**
- Column 2 test: **HTTP 200 + `zaztWz` appeared**
- Tool used for testing: **Burp Suite Repeater**
- Final result: **Lab solved successfully**

## Result

**Solved successfully.**

I identified the text-capable column and confirmed that the required string `zaztWz` could be retrieved through the second column of the UNION result.
