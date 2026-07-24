# DNS Recon Tool

## Overview

The DNS Recon Tool is a CLI-based Python reconnaissance utility that gathers basic information about a target domain. It performs DNS resolution, verifies whether the website is reachable over HTTPS, retrieves WHOIS registration information, and generates a structured reconnaissance report automatically.

This project was built as part of my cybersecurity learning journey to better understand DNS, HTTP requests, WHOIS lookups, external command execution, and report generation.

---

## Features

- Resolve IPv4 and IPv6 addresses for a domain
- Check website reachability over HTTPS
- Perform WHOIS lookups using the system `whois` command
- Extract and summarize important WHOIS information
- Generate a professional reconnaissance report automatically
- Handle invalid domains and connection errors gracefully

---

## Technologies Used

- Python 3
- socket
- requests
- subprocess
- datetime
- warnings

---

## Project Structure

```
dns-recon-tool/
│
├── recon.py
├── requirements.txt
├── README.md
└── sample_report.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/learning-journal.git
```

Navigate to the project directory:

```bash
cd learning-journal/dns-recon-tool
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

### Linux / WSL

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the tool by providing a domain name:

```bash
python3 recon.py google.com
```

Example:

```bash
python3 recon.py example.com
```

The tool will:

- Resolve the domain's IP addresses
- Check HTTPS reachability
- Perform a WHOIS lookup
- Generate a report named:

```
example.com_report.txt
```

---

## Example Output

```
=== DNS RECONNAISSANCE REPORT ===

Target Domain: google.com

--- IP ADDRESSES ---
142.xxx.xxx.xxx
2a00:xxxx:xxxx::xxxx

--- REACHABILITY ---
Status Code: 200

--- WHOIS INFORMATION ---
Registrar: MarkMonitor Inc.
Creation Date: 1997-09-15
Registrant Organization: Google LLC
Registrant Country: US
Name Server: ns1.google.com
...

=== END OF REPORT ===
```

---

## What I Learned

Through this project, I learned:

- How DNS resolution works using Python's `socket` module
- How to send HTTP/HTTPS requests using the `requests` library
- How to execute external system commands using `subprocess`
- How to retrieve and summarize WHOIS information
- How to organize Python code into reusable functions
- How to generate structured text reports automatically
- Basic reconnaissance techniques commonly used during information gathering

---

## Future Improvements

- Remove duplicate WHOIS fields from different registries
- Perform reverse DNS lookups
- Retrieve MX, NS, TXT, and CNAME DNS records
- Export reports in JSON format
- Add colored terminal output
- Support scanning multiple domains from a file

---

## Disclaimer

This project is intended for educational purposes only. Use it only against domains you own or have permission to assess.