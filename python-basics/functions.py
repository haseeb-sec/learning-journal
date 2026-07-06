def check_port(port):
    if port == 22 or port == 3306:
        return "Risky"
    else:
        return "Safe"
    
ports = [22, 80, 443, 3306, 8080]

print(check_port(ports[0]))
print("_________________")
print(check_port(ports[-1]))
print("_________________")
print(check_port(ports[2]))
print("_________________")
for port in ports:
    print("Port: " + check_port(port))
print("_________________")




