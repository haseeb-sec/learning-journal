with open("ips.txt", "r") as file:
    for line_number, ip in enumerate(file, start=1):
        print(f"Line {line_number}: {ip.strip()}")