import requests
import sys
import warnings
warnings.filterwarnings("ignore")

def make_request(url):
    try:
        response = requests.get(url, timeout=5, verify=False)
        return response
    except Exception as e:
        print("Error: Could not connect to " + url)
        print("Details: " + str(e))
        sys.exit() 
    
def check_headers(response):
    security_headers = [
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-XSS-Protection"
    ]

    present = []
    missing = []

    for header in security_headers:
        if header in response.headers:
            present.append(header)
        else:
            missing.append(header)
    return present, missing

def check_status(response):
    code = response.status_code

    if code == 200:
        return str(code) + " - OK"
    elif code == 301 or code == 302:
        return str(code) + " - Redirect"
    elif code == 403:
        return str(code) + " - Forbidden"
    elif code == 404:
        return str(code) + " - Not Found"
    elif code == 500:
        return str(code) + " - Server Error"
    else:
        return str(code) + " - Unknown"
    
def check_server_discloser(response):
    server = response.headers.get("Server", "Not disclosed")
    powered_by = response.headers.get("X-Powered-By", "Not disclosed")
    return server, powered_by


def save_report(url, present, missing, status, server, powered_by):
    with open("web_report.txt", "w") as file:
        file.write("=== WEB SECURITY REPORT ===\n")
        file.write("Target: " + url + "\n\n")
        file.write("Status: " + status + "\n")
        file.write("Server: " + server + "\n")
        file.write("X-Powered-By: " + powered_by + "\n")
        file.write("--- SECURITY HEADERS PRESENT ---\n")
        for h in present:
            file.write("[OK] " + h + "\n")
        file.write("--- SECURITY HEADERS MISSING ---\n")
        for h in missing:
            file.write("[MISSING] " + h + "\n")
    print("Report saved to web_report.txt")

if len(sys.argv) < 2:
    print("Usage: python requester.py <url>")
    sys.exit()

url = sys.argv[1]
response = make_request(url)
present, missing = check_headers(response)
status = check_status(response)
server, powered_by = check_server_discloser(response)
save_report(url, present, missing, status, server, powered_by)