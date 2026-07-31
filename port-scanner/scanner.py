import socket
import threading
import argparse

# scan_port: Tries to connect to a single port on a given IP.
# Returns True if the port is open, False if closed or unreachable.
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))

        if result == 0:
            return True
        else:
            return False
        
    except OSError:
        return False

def threaded_scan(ip, port, open_ports, lock):
    if scan_port(ip, port):
        print("Port " + str(port) + " is OPEN")
        with lock:
            open_ports.append(port)

# New multi-threaded version, it makes the searching methodology faster 
def threaded_scan_target(ip, start_port, end_port):
    print("Scanning " + ip + " from port " + str(start_port) + " to port " + str(end_port))
    open_ports = []
    threads = []
    lock = threading.Lock()
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=threaded_scan, args=(ip, port, open_ports, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    open_ports.sort()

    return open_ports

# save_report: Saves the scan results to a text file called scan_report.txt.
# Includes the target IP, number of open ports, and each open port found.
def save_report(ip, open_ports):
    with open("scan_report.txt", "w") as file:
        file.write("=== PORT SCAN REPORT ===\n")
        file.write("Target: " + ip + "\n")
        file.write("Open ports found: " + str(len(open_ports)) + "\n\n")
        for port in open_ports:
            file.write("Port " + str(port) + " - OPEN\n" )
        print("Report saved to scan_report.txt")

parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
parser.add_argument("target", help="Target IPv4 address")
parser.add_argument("--start", type=int, default=1, help="Starting port")
parser.add_argument("--end", type=int, default=1024, help="Ending port")

args = parser.parse_args()

# Run the scanner
target_ip = args.target
start_port = args.start
end_port = args.end

if start_port < 1 or end_port > 65535 or start_port > end_port:
    parser.error("Invalid port range. Use ports between 1 and 65535, and make sure --start is less than or equal to --end.")

open_ports = threaded_scan_target(target_ip, start_port, end_port)
print(f"\nScan complete.")
print(f"Open ports: {open_ports}")

save_report(target_ip, open_ports)

