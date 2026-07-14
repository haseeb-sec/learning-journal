import sys

# Function for reading the file line by line, and getting the total lines

def read_log(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

# Function for extracting the ip addresses from each line

def get_ip(line):
    ip = line.split(" ")[0]
    return ip

# Counting how many times each IP appears

def count_ips(lines):
    ip_counts = {}
    for line in lines:
        ip = get_ip(line)
        if ip in ip_counts:
            ip_counts[ip] += 1
        else: 
            ip_counts[ip] = 1
    return ip_counts

# Flagging suspicious IPs.

def find_suspicious(ip_counts, threshold=3):
    suspicious = []
    for ip, count in ip_counts.items():
        if count > threshold:
            suspicious.append(ip + " - " + str(count) + (" requests"))

    return suspicious

# Detecting the bots and crawler etc
def detect_bots(lines):
    bots = []
    for line in lines:
        if "Bot" in line or "bot" in line or "crawler" in line or "spider" in line:
            ip = get_ip(line)
            if ip not in bots:
                bots.append(ip)
    return bots

# Detecting the suspicious logins

def detect_failed_logins(lines, threshold=3):
    failed = {}
    for line in lines:
        if "401" in line:
            ip = get_ip(line)
            if ip in failed:
                failed[ip] += 1
            else:
                failed[ip] = 1
    suspicious_logins = []
    for ip, count in failed.items():
        if count >= threshold:
            suspicious_logins.append(ip + " - " + str(count) + " failed attempts")
    return suspicious_logins


# Generating report 

def generate_report(ip_counts, suspicious, bots, failed_logins):
    with open("report.txt", "w") as file:
        file.write("=== LOG ANALYZER REPORT ===\n")
        file.write("Total unique IPs: " + str(len(ip_counts)) + "\n")
        file.write("\n--- ALL IPs ---\n")
        for ip, count in ip_counts.items():
            file.write(ip + " - " + str(count) + " requests\n")
        file.write("\n--- SUSPICIOUS IPs ---\n")
        for s in suspicious:
            file.write(s + "\n")
        file.write("\n--- BOT IPs DETECTED ---\n")
        for bot in bots:
            file.write(bot + "\n")
        file.write("\n--- Suspicious Logins ---\n")
        for f in failed_logins:
            file.write(f + "\n")
    print("Report saved to report.txt")

# Run the analyzer
if len(sys.argv) < 2:
    print("Usage: python analyzer.py <logfile>")
    sys.exit()

filename = sys.argv[1]
lines  = read_log(filename)

ip_counts = count_ips(lines)
suspicious = find_suspicious(ip_counts)
bots = detect_bots(lines)
failed_logins = detect_failed_logins(lines)
generate_report(ip_counts, suspicious, bots, failed_logins)




