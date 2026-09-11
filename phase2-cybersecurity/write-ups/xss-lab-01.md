# Reflected XSS Security Assessment Lab

## Overview

This lab was built to practice a complete web security assessment workflow:

**Reconnaissance → Identification → Exploitation → Impact → Root Cause → Remediation → Retest**

The application is a local Flask application containing a deliberately vulnerable reflected XSS endpoint.

All data used in the lab is synthetic.

## Target

* Application: Local Flask XSS Lab
* URL: `http://127.0.0.1:5000/`
* Vulnerable parameter: `name`
* Vulnerability: Reflected Cross-Site Scripting (XSS)
* Severity: Context-dependent; potentially High in an authenticated application with sensitive data or privileged actions

## 1. Reconnaissance

The application was first accessed normally through the browser and Burp Suite.

A normal request to:

```http
GET /
```

returned the application page.

After logging in as the synthetic user `victim`, the page displayed:

```text
Logged in as: victim
Fake secret: FAKE-SECRET-12345
```

This established an authenticated application context for the later security testing.

## 2. Identifying the Input Reflection

The application accepts a `name` parameter:

```http
GET /?name=Haseeb
```

The response reflected the supplied value into the HTML:

```html
<h2>Hello, Haseeb</h2>
```

This indicated that user-controlled input was being inserted into the page and warranted testing for HTML/JavaScript injection.

## 3. XSS Exploitation

The following payload was supplied through the `name` parameter:

```html
<script>alert(document.body.innerText)</script>
```

The application returned the payload directly inside the HTML:

```html
<h2>Hello, <script>alert(document.body.innerText)</script></h2>
```

The browser interpreted the injected `<script>` element as executable JavaScript.

The resulting alert displayed:

```text
Logged in as: victim
Fake secret: FAKE-SECRET-12345
```

This confirmed reflected XSS execution in the victim's page context.

## 4. Impact Demonstration

The test was extended beyond a simple JavaScript alert.

The injected JavaScript was able to read information rendered on the page, including the synthetic secret.

A same-origin request was also tested:

```javascript
fetch('/')
    .then(r => r.text())
    .then(t => alert(t.includes('FAKE-SECRET-12345')))
```

The result was:

```text
true
```

This demonstrated that JavaScript executing through the XSS could make a request to the same application and process the returned authenticated page content.

### Important Session Observation

The Flask session cookie was configured with the `HttpOnly` attribute.

Therefore, JavaScript could not directly read the session cookie through `document.cookie`.

However, `HttpOnly` does not prevent XSS itself. JavaScript running in the victim's browser can still interact with the application through normal same-origin browser requests.

This distinction is important:

**HttpOnly helps protect the session cookie from direct JavaScript theft; it does not eliminate the impact of XSS.**

## 5. Root Cause

The vulnerable template contained:

```html
<h2>Hello, {{ name|safe }}</h2>
```

Jinja normally escapes HTML supplied through template variables.

The `|safe` filter explicitly marks the value as trusted HTML and disables the normal escaping behavior.

Because `name` came directly from the HTTP request:

```python
name = request.args.get("name", "")
```

the application was effectively treating attacker-controlled input as trusted HTML.

The vulnerable data flow was:

```text
HTTP request
    ↓
name parameter
    ↓
request.args.get("name")
    ↓
Jinja template
    ↓
|safe
    ↓
Raw HTML/JavaScript in response
    ↓
Browser executes attacker-controlled JavaScript
```

## 6. Remediation

The vulnerable template was changed from:

```html
<h2>Hello, {{ name|safe }}</h2>
```

to:

```html
<h2>Hello, {{ name }}</h2>
```

This restores Jinja's normal HTML escaping behavior.

No additional sanitization was required for this specific output because the application only intended to display the supplied name as text.

## 7. Retest

After restarting the Flask application with the corrected code, the original XSS payload was tested again.

The browser no longer executed the JavaScript.

Instead, the payload appeared as visible text:

```text
Hello, <script>alert(document.body.innerText)</script>
```

The absence of JavaScript execution confirmed that the original reflected XSS vulnerability was successfully remediated.

## 8. Security Review

A source-code review was also performed for common XSS-related patterns.

The relevant input and rendering locations were:

```python
name = request.args.get("name", "")
return render_template_string(HTML, name=name)
```

The review found no remaining:

* `|safe`
* `innerHTML`
* `Markup`

usage in the application.

The `.venv` directory was also excluded from Git using `.gitignore`.

## 9. Attacker → Defender Workflow

This lab demonstrated the complete security workflow:

### Attacker

1. Discover an input parameter.
2. Determine whether the value is reflected.
3. Test whether HTML is interpreted.
4. Confirm JavaScript execution.
5. Determine what information the script can access.
6. Test interaction with the same-origin application.

### Defender

1. Trace the untrusted input to its output.
2. Identify the unsafe template behavior.
3. Remove the unnecessary trust override.
4. Restart the application.
5. Re-run the original attack.
6. Confirm that the payload is escaped and no longer executes.
7. Review related code for similar unsafe patterns.

## 10. OWASP Mapping

This vulnerability maps to:

* **OWASP Top 10: A03 — Injection**
* Cross-Site Scripting (XSS)

The core security failure was allowing untrusted input to become executable browser-side content.

## 11. AI Security Bridge

The underlying security principle also applies to AI systems.

Traditional XSS:

```text
Untrusted input → trusted HTML context → unintended execution
```

A related AI-security pattern is:

```text
Untrusted input → trusted instruction context → unintended model behavior
```

The mechanisms are different, but the broader lesson is similar:

> **Data must not automatically be treated as trusted instructions.**

This is one reason traditional application-security concepts such as input trust boundaries, output encoding, context separation, and authorization remain relevant when moving into AI security.

## 12. Result

The lab successfully demonstrated and remediated a reflected XSS vulnerability.

### Before remediation

Attacker-controlled JavaScript was executed by the browser and could access information available to the victim's page context.

### After remediation

The same payload was rendered as text rather than executable HTML/JavaScript.

The vulnerability was therefore successfully reproduced, understood, fixed, and retested.

## Evidence

The vulnerable application version is preserved as:

```text
phase2-cybersecurity/xss-lab/app-v1-backup.py
```

The remediated application is:

```text
phase2-cybersecurity/xss-lab/app.py
```

Git commit containing the lab code:

```text
130caa2 — Add reflected XSS security assessment lab
```
