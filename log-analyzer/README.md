**Author:** Haseeb Ullah Shah

# Log Analyzer

## What this tool does

This is a CLI-based Python log analyzer that analyzes web server log files. It counts how many requests were made by each IP address, identifies suspicious IPs that exceed a predefined request threshold, detects bots and crawlers based on common user-agent keywords, identifies repeated failed login attempts by analyzing HTTP `401 Unauthorized` responses, and generates a clean `report.txt` file containing the analysis.

## How to run it

1. Make sure Python 3 is installed on your computer.
2. Place the log file you want to analyze in the same folder as the Python script.
3. Open the project folder in Visual Studio Code or another code editor.
4. Run the script from the terminal by providing the log file as a command-line argument:

```bash
python analyzer.py access.log
```

5. After the script finishes, a `report.txt` file will be created automatically in the project folder.

## What the output looks like

The tool generates a `report.txt` file containing:

* Total number of unique IP addresses found in the log.
* A list of all IP addresses and the number of requests made by each one.
* A list of suspicious IP addresses that exceeded the request threshold.
* A list of detected bot and crawler IP addresses.
* A list of IP addresses with repeated failed login attempts (`401 Unauthorized`).

## Example Output

=== LOG ANALYZER REPORT ===
Total unique IPs: 4

--- ALL IPs ---
192.168.1.1 - 6 requests
54.36.148.184 - 3 requests
10.0.0.5 - 5 requests
172.16.0.1 - 2 requests

--- SUSPICIOUS IPs ---
192.168.1.1 - 6 requests
10.0.0.5 - 5 requests

--- BOT IPs DETECTED ---
54.36.148.184

--- Suspicious Logins ---
10.0.0.5 - 4 failed attempts
