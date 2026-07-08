import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except:
        return False
    
def scan_target(ip, start_port, end_port):
    print("Scanning " + ip + " from port " + str(start_port) + " to port " + str(end_port))
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            print("Port " + str(port) + " is OPEN")
            open_ports.append(port)
    return open_ports

def save_report(ip, open_ports):
    with open("scan_report.txt", "w") as file:
        file.write("=== PORT SCAN REPORT ===\n")
        file.write("Target: " + ip + "\n")
        file.write("Open ports found: " + str(len(open_ports)) + "\n\n")
        for port in open_ports:
            file.write("Port " + str(port) + " - OPEN\n" )
        print("Report saved to scan_report.txt")

target_ip = "127.0.0.1"
open_ports = scan_target(target_ip, 1, 500)
print("\nScan complete. Open ports: " + str(open_ports))

save_report(target_ip, open_ports)
