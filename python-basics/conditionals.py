ports = [22, 80, 443, 3306, 8080]

for port in ports:
    if port == 22 or port == 3306:
        print("WARNING! Risky port found: " + str(port))
    
    else:
        print("OK! Safe port: " + str(port))