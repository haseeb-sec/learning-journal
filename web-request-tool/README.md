# Web Security Header Analyzer

## What this tool does

This is a CLI-based Python web security analyzer that sends an HTTP request to a target website and performs a basic security assessment. It checks the HTTP status code, identifies common security headers that are present or missing, detects server software disclosure, checks for backend technology disclosure through the `X-Powered-By` header, and automatically generates a `web_report.txt` file containing the results.

## What problem it solves

Many websites unintentionally expose information that can help attackers understand how the server is configured. Missing security headers can also leave browsers without important security protections. This tool helps identify these issues quickly by providing a simple security report that highlights missing headers and publicly disclosed server information.

## Features

- CLI-based Python application
- Accepts any URL as input using command-line arguments
- Sends HTTP/HTTPS requests to the target website
- Checks the HTTP status code
- Detects common HTTP security headers
- Identifies missing security headers
- Detects server software disclosure
- Detects backend technology disclosure through the `X-Powered-By` header
- Generates a professional `web_report.txt` report
- Uses a Python virtual environment with project dependencies managed through `requirements.txt`

## Project Structure

```text
web-security-header-analyzer/
├── README.md
├── requester.py
├── requirements.txt
└── web_report.txt
```

## Requirements

Install the required dependencies before running the tool.

```bash
pip install -r requirements.txt
```

## How to run it

1. Make sure Python 3 is installed.
2. (Recommended) Create and activate a Python virtual environment.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Open the project folder in Visual Studio Code or another code editor.
5. Run the script from the terminal by providing a target URL.

Example:

```bash
python requester.py https://python.org
```

6. After the scan finishes, a `web_report.txt` file will be created automatically.

## Example Output

```text
=== WEB SECURITY REPORT ===
Target: https://python.org

Status: 200 - OK
Server: nginx
X-Powered-By: Not disclosed

--- SECURITY HEADERS PRESENT ---
[OK] X-Frame-Options
[OK] Strict-Transport-Security

--- SECURITY HEADERS MISSING ---
[MISSING] X-Content-Type-Options
[MISSING] Content-Security-Policy
[MISSING] X-XSS-Protection
```

## Notes

- Missing security headers do not necessarily mean a website is vulnerable, but they may indicate opportunities to improve browser-side security.
- Revealing server software (for example, `nginx` or `Apache`) provides additional information about the target, although it does not by itself make a server vulnerable.
- This tool performs a basic security assessment and should not be considered a complete vulnerability scanner.

## Legal Warning

Only scan websites and systems that you own or have explicit written permission to test. Unauthorized security testing may violate laws or the target organization's policies.