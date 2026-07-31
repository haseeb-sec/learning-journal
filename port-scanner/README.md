# Python Port Scanner

## What this tool does

This is a CLI-based Python port scanner that scans a target IPv4 address over a specified range of TCP ports. It uses multithreading to perform scans more efficiently, identifies which ports are open, displays the results in the terminal, and automatically generates a `scan_report.txt` file containing the scan results.

## Features

- CLI-based Python application
- Supports command-line arguments using `argparse`
- Scans a configurable range of TCP ports
- Supports IPv4 targets
- Uses multithreading for faster scanning
- Validates user-supplied port ranges
- Displays open ports in the terminal
- Automatically generates a `scan_report.txt` file

## How to run it

1. Make sure Python 3 is installed on your system.
2. Open a terminal inside the project folder.
3. Run the scanner by specifying the target IPv4 address.

Example:

```bash
python3 scanner.py 127.0.0.1
```

To scan a custom port range:

```bash
python3 scanner.py 127.0.0.1 --start 20 --end 200
```

After the scan finishes, a `scan_report.txt` file will be generated automatically.

## What the output looks like

The tool generates a `scan_report.txt` file containing:

- The target IP address.
- The total number of open ports found.
- A list of all open ports discovered during the scan.

### Example Output

```text
=== PORT SCAN REPORT ===
Target: 127.0.0.1
Open ports found: 2

Port 135 - OPEN
Port 445 - OPEN
```

## Legal Warning

Only scan IP addresses you own or have explicit written permission to scan. Scanning systems without permission is illegal in most countries.