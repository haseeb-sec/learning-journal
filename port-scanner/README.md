# Python Port Scanner

## What this tool does

This is a CLI-based Python port scanner that scans a target IP address over a specified range of ports. It identifies which ports are open, displays the results in the terminal, and automatically generates a `scan_report.txt` file containing the scan results.

## How to run it

1. Make sure Python 3 is installed on your computer.
2. Open the Python script and set the target IP address by modifying the `target_ip` variable.
3. Adjust the port range if needed by changing the values passed to `scan_target()`.
4. Open the project folder in Visual Studio Code or any other code editor.
5. Run the Python script.
6. After the script finishes, a `scan_report.txt` file will be created automatically in the project folder.

## What the output looks like

The tool generates a `scan_report.txt` file containing:

* The target IP address.
* The total number of open ports found.
* A list of all open ports discovered during the scan.

### Example Output

=== PORT SCAN REPORT ===
Target: 127.0.0.1
Open ports found: 2

Port 135 - OPEN
Port 445 - OPEN

## Legal Warning
Only scan IP addresses you own or have explicit written permission to scan.
Scanning systems without permission is illegal in most countries.