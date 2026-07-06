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

# Generating report 

def generate_report(ip_counts, suspicious):
    with open("report.txt", "w") as file:
        file.write("=== LOG ANALYZER REPORT ===\n")
        file.write("Total unique IPs: " + str(len(ip_counts)) + "\n")
        file.write("\n--- ALL IPs ---\n")
        for ip, count in ip_counts.items():
            file.write(ip + " - " + str(count) + " requests\n")
        file.write("\n--- SUSPICIOUS IPs ---\n")
        for s in suspicious:
            file.write(s + "\n")
    print("Report saved to report.txt")

# Run the analyzer
lines = read_log("access.log")
ip_counts = count_ips(lines)
suspicious = find_suspicious(ip_counts)
generate_report(ip_counts, suspicious)