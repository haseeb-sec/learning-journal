import socket
import requests
import sys
import subprocess
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

def dns_lookup(domain):
    try:
        ips = socket.getaddrinfo(domain, None)
        ip_list = list(set([ip[4][0] for ip in ips]))
        return ip_list
    except:
        return []

def check_reachability(domain):
    try:
        response = requests.get("https://" + domain, timeout=5, verify=False)
        return response.status_code
    except:
        return "Unreachable"

def whois_lookup(domain):
    try:
        result = subprocess.run(
            ["whois", domain],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout
    except:
        return "Whois lookup failed"

def parse_whois(whois_data):
    important_fields = [
        "Registrar:",
        "Registrant Organization:",
        "Creation Date:",
        "Registry Expiry Date:",
        "Registrar Registration Expiration Date:",
        "Registrant Country:",
        "Name Server:"
    ]
    summary = []
    for line in whois_data.splitlines():
        for field in important_fields:
            if field.lower() in line.lower():
                summary.append(line.strip())
                break

    summary = list(dict.fromkeys(summary))
    return "\n".join(summary)

def save_report(domain, ips, status_code, whois_summary):
    filename = domain + "_report.txt"
    with open(filename, "w") as file:
        file.write("=== DNS RECONNAISSANCE REPORT ===\n")
        file.write("Date: " + str(datetime.now()) + "\n")
        file.write("Target Domain: " + domain + "\n\n")
        file.write("--- IP ADDRESSES ---\n")
        for ip in ips:
            file.write(ip + "\n")
        file.write("\n--- REACHABILITY ---\n")
        file.write("Status Code: " + str(status_code) + "\n")
        file.write("\n--- WHOIS INFORMATION ---\n")
        file.write(whois_summary + "\n")
        file.write("=== END OF REPORT ===\n")
    print("Report saved to " + filename)

if len(sys.argv) < 2:
    print("Usage: python3 recon.py <domain>")
    sys.exit()

domain = sys.argv[1]

print("Start reconnaissance on: " + domain)
print("Running DNS lookup...")
ips = dns_lookup(domain)

print("Checking reachability...")
status_code = check_reachability(domain)

print("Running whois lookup...")
whois_data = whois_lookup(domain)

whois_summary = parse_whois(whois_data)

save_report(domain, ips, status_code, whois_summary)
