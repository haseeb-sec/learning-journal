# Progress Log — Haseeb Ullah Shah

## Session 1 — 15/06/2026
**What I learned:** Environment setup — Git, VS Code, Python, GitHub
**What I built:** learning-journal repository on GitHub, first commit pushed
**What confused me:** TryHackMe signup had a browser error, fixed by switching to Edge
**Next step:** Start Phase 1 — Linux command line basics

Next step: Phase 1 — Linux command line basics via TryHackMe

## Session 2 — 18/06/2026
**What I learned:** Linux navigation (pwd, ls, cd), file reading (cat, head, tail), pattern searching (grep)
**What I built:** Read and analyzed a real access.log file — identified bot traffic, counted POST requests
**What confused me:** Cloud machine disconnecting on inactivity — now I understand it resets and that's normal
**Next step:** Continue Linux Fundamentals — permissions and file operations

## Session 3 — 04/07/2026
**What I learned:** Linux file permissions — reading ls -l output, chmod, permission numbers
**What I built:** Created myfile.txt, changed permissions from 777 to 644 independently
**What confused me:** Being inside folder1 and trying to ls -l folder1 — understood the mistake
**Next step:** Linux file operations — copying, moving, deleting files

## Session 4 — 04/07/2026
**What I learned:** Linux file operations — mkdir, touch, echo, cp, mv, rm, rm -r
**What I built:** Created, copied, moved, and deleted files and folders independently
**What confused me:** Tried to cd into folder3 while inside practice folder — understood the mistake
**Next step:** Linux networking commands — ping, ifconfig, netstat

## Session 5 - 07/04/2026

**What I learned:** Linux networking commands — ip addr, ping, ss -tuln, 
ss -tn, cat /etc/hosts

**What I built:** Analyzed a live TryHackMe machine as if it were a real 
compromised server. Checked its IP address, tested external connectivity, 
identified open ports, checked active connections, and verified /etc/hosts 
for tampering.

**What confused me:** I understood the commands but could not connect why 
we were running them or what the output meant in a real security context. 
The ports concept was unclear — I did not understand what an open port 
means as a security risk.

**How it got cleared:** The Islamabad online store investigation story 
connected everything. Each command answered one specific question an analyst 
asks when investigating a compromised server — identity, connectivity, open 
doors, active intruders, and tampering. After that story, the whole workflow 
made sense.

**Next step:** Complete Linux Fundamentals Part 1 room on TryHackMe 
formally, then start Python basics.

## Linux Fundamentals Part 1 — TryHackMe — 07/04/2026

**What I completed:** Linux Fundamentals Part 1 room on TryHackMe. 
Learned to run essential commands on an interactive terminal.

**Points earned:** 88

**Commands I now understand:** pwd, ls, cd, echo, cat, grep, 
chmod, mkdir, touch, cp, mv, rm, ip addr, ping, ss -tuln, ss -tn

**What confused me:** Nothing major — everything covered in 
our sessions came together in the room questions.

**Next step:** Python basics

## Python Basics - 07/06/2026

**What I completed:** Variables, Data Types, Loops, Conditionals, Functions, and File Reading. I revised these concepts because I had studied them before, but a short revision was necessary.

**What I learned:** I learned what variables are and how to use them, what data types are and the kind of data each type stores. I also learned what loops are, how they actually work, and implemented them. I revised conditionals, functions, how to create and use them, and how to create, open, and read files in Python.

**What confused me:** Nothing in particular. Everything was understandable, as this was mainly a revision of concepts I had already learned.

**Next Step:** Build a real security tool in Python by combining everything I learned today.

## Python Project - Log Analyzer - 07/06/2026

**What I completed:** Built a CLI-based Log Analyzer in Python that reads a real `access.log` file, extracts IP addresses, counts the total requests made by each IP, identifies suspicious IPs based on a configurable request threshold, and generates a clean `report.txt` file.

**What I learned:** I learned how to build a complete Python program by combining variables, loops, conditionals, functions, dictionaries, and file handling. I learned how to read a log file line by line, extract IP addresses from each log entry, count the number of requests made by each IP, identify suspicious IPs based on a threshold, and automatically generate a well-formatted report. I also learned how to organize code into reusable functions and build a practical CLI-based security tool.

**What confused me:** Nothing in particular. The project helped reinforce the Python concepts I revised earlier, and everything worked as expected after testing it with a sample `access.log` file.

**Next Step:** Build a Python port scanner from scratch.


## Python Project - Port Scanner - 07/08/2026

**What I completed:** Built a CLI-based Python Port Scanner that scans a target IP address over a specified range of ports, identifies which ports are open, displays the results in the terminal, and automatically generates a `scan_report.txt` file containing the scan results.

**What I learned:** I learned how to use Python's `socket` module to establish TCP connections and determine whether a port is open or closed. I also learned how to scan a range of ports using loops, organize the program into reusable functions, handle connection timeouts, store the discovered open ports in a list, and automatically generate a well-formatted report containing the scan results.

**What confused me:** Understanding the `socket` module and the networking terminologies such as `AF_INET` and `SOCK_STREAM` was initially confusing because they were completely new to me. After discussing these concepts with Claude, I understood that a socket is the endpoint used to establish a network connection, `AF_INET` specifies that the connection uses the IPv4 address family, and `SOCK_STREAM` specifies that the connection uses the TCP protocol. Once I understood how these components work together, the overall logic of the port scanner became much clearer.

**Next Step:** Adding three improvements to the log analyzer tool:

1. Bot detection: flag lines containing "Bot" automatically
2. Failed login detection: flag IPs with multiple 401 responses
3. Command line input: accept any filename instead of hardcoded access.log

## Python Project - Log Analyzer Update - 07/14/2026

**What I improved:** Enhanced the Log Analyzer by adding support for command-line arguments using the `sys` module, allowing the program to analyze any log file specified by the user instead of relying on a hardcoded filename. I also added bot and crawler detection by identifying common user-agent keywords such as `Bot`, `bot`, `crawler`, and `spider`. In addition, I implemented failed login detection by analyzing HTTP `401 Unauthorized` responses and flagging IP addresses that exceeded a configurable threshold of failed login attempts. Finally, I updated the generated `report.txt` to include dedicated sections for detected bots and suspicious login attempts, making the report more comprehensive and useful.

**What I learned:** I learned how to use the `sys` module and `sys.argv` to accept command-line arguments, making Python scripts more flexible and reusable. I strengthened my understanding of dictionaries by using them to count failed login attempts for each IP address and practiced creating multiple detection functions that each perform a specific task. I also learned how basic security monitoring can be performed by analyzing web server logs for suspicious request patterns, automated bots, crawlers, and repeated authentication failures. This project also reinforced the importance of writing modular, reusable code by separating each detection feature into its own function.

**What confused me:** Understanding command-line arguments with `sys.argv` was initially new because I had only executed Python scripts by clicking the Run button in Visual Studio Code. After experimenting with the program and learning how arguments are passed from the command line, I understood how Python receives user input through `sys.argv` and why this approach makes CLI tools more practical and reusable.

**Next Step:** Add multi-threading to the port scanner.

## Python Project - Port Scanner (Multithreading Upgrade) - 07/14/2026

**What I completed:** Improved my CLI-based Python Port Scanner by implementing multithreading using Python's `threading` module. Instead of scanning ports one by one, the scanner now creates a separate thread for each port, allowing multiple ports to be scanned concurrently. I also updated the project documentation to reflect the new functionality and features.

**What I learned:** I learned the fundamentals of multithreading in Python and how it can significantly improve the performance of a port scanner. I learned how to create and manage threads using `threading.Thread()`, how the `target` and `args` parameters work, why `start()` is required to begin a thread, why `join()` is used to wait for all threads to finish, and how multiple threads can share the same `open_ports` list to store scan results. I also learned the difference between creating a thread and actually starting it, and how multithreading allows multiple ports to be scanned at the same time instead of sequentially.

**What confused me:** The multithreading concepts were completely new to me, especially understanding what a thread actually is, how multiple threads run concurrently, why a separate function was needed for each thread, and the purpose of `threading.Thread()`, `target`, `args`, `start()`, and `join()`. These concepts were initially difficult to visualize, but after studying them in detail and understanding each component step by step, the overall workflow became much clearer.

**Next Step:** Build a web request tool using Python's requests library.

## Python Project - Web Security Header Analyzer - 07/18/2026

**What I completed:** Built a CLI-based Web Security Header Analyzer in Python that accepts a target URL as a command-line argument, sends an HTTP/HTTPS request to the website, checks the HTTP status code, analyzes common HTTP security headers, detects server software and backend technology disclosure, and automatically generates a professional `web_report.txt` file. I also learned how to use a Python virtual environment and manage project dependencies using a `requirements.txt` file.

**What I learned:** I learned how to use the `requests` library to communicate with web servers and process HTTP responses. I learned how to work with command-line arguments using `sys.argv`, retrieve and analyze HTTP response headers, check common security headers, interpret HTTP status codes, detect server and technology disclosure through response headers, handle connection errors using `try` and `except`, and organize the project into reusable functions. I also learned the purpose of Python virtual environments, why they are important for dependency management, and how to generate a `requirements.txt` file for reproducible projects.

**What confused me:** Several web-related concepts were new to me, especially understanding HTTP request and response objects, how response headers are stored and accessed, why security headers are important, how command-line arguments work through `sys.argv`, and how a virtual environment isolates project dependencies. These concepts were unfamiliar at first, but after implementing them step by step and testing the tool against real websites, they became much easier to understand.

**Next Step:** Basic shell scripts automating real tasks on Linux.

## Bash Scripting - Linux Security Automation - 07/23/2026

**What I completed:** Built my first Bash scripts for Linux automation and security tasks. I created `myscript.sh` to understand the basics of shell scripting, `sysinfo.sh` to collect system information such as the hostname, current user, IP addresses, open ports, and disk usage, `security_audit.sh` to perform a basic Linux security audit by checking logged-in users, recent login attempts, open ports, and files with full permissions, and `log_analyzer.sh` to analyze web server log files by counting total requests, identifying the most active IP addresses, counting POST requests, and detecting 404 errors.

**What I learned:** I learned what Bash is and why it is widely used by Linux administrators and cybersecurity professionals for automation. I learned how to create executable shell scripts, work with variables, use command-line arguments through `$1`, write conditional statements using `if`, connect commands with pipes (`|`), and process text using tools such as `awk`, `sort`, `uniq -c`, `wc -l`, `grep`, and `head`. I also learned how to make scripts executable using `chmod +x` and how Bash scripts can automate repetitive security and system administration tasks. Finally, I switched to Git Bash as my permanent environment for writing and testing Bash scripts instead of relying on temporary TryHackMe machines.

**What confused me:** Bash scripting syntax was quite different from Python, especially variable declaration, command substitution, command-line arguments, and conditional statements. Understanding the purpose of `chmod +x` also took some time initially. Another challenge was realizing that TryHackMe machines are temporary, which made it difficult to maintain projects. Switching to Git Bash provided a permanent environment where I can continue developing and improving my scripts.

**Next Step:** Complete Networking Fundamentals, the final topic of Phase 1, before moving into Core Cybersecurity and building more advanced security tools.

## Development Environment Upgrade - WSL2 Ubuntu - 07/23/2026

**What I completed:** Upgraded my development environment from Git Bash to a full Linux environment by installing Ubuntu 26.04 LTS through Windows Subsystem for Linux (WSL2). Before installing WSL2, I repaired my Windows 10 installation using an in-place repair upgrade, which restored the missing Windows optional features required for WSL2 while preserving my files, applications, and personal settings. After the repair, I enabled WSL2, installed Ubuntu, created my Linux user account, updated the operating system, installed the latest WSL components, verified Python 3.14 and Git inside Ubuntu, and configured Visual Studio Code to develop directly inside the Linux environment using the Remote - WSL extension.

**What I learned:** I learned the difference between Git Bash and a real Linux environment. I now understand that WSL2 provides a genuine Linux kernel running alongside Windows, allowing me to use the same development environment commonly used on servers and by professional software engineers. I learned how Linux and Windows filesystems interact through `/mnt`, how to navigate the Linux filesystem, how WSL integrates with Visual Studio Code, and why developing directly inside Ubuntu provides a more realistic environment for Python, cybersecurity, automation, and future AI development.

**What confused me:** Initially, WSL2 could not be installed because my Windows installation was missing the required optional features. I spent time troubleshooting feature errors, DISM commands, and virtualization settings before realizing that the Windows installation itself needed to be repaired. After completing an in-place Windows repair upgrade, all required features became available and the WSL2 installation completed successfully. I also learned the difference between PowerShell and the Ubuntu terminal and when each should be used.

**Environment Changes:**

- Repaired Windows 10 using an in-place upgrade
- Installed Windows Subsystem for Linux (WSL2)
- Installed Ubuntu 26.04 LTS
- Configured Linux user account
- Updated Ubuntu packages
- Installed and verified Python 3.14
- Installed and verified Git 2.53
- Connected Visual Studio Code to WSL2
- Confirmed WSL Version 2 as the default environment

**Next Step:** Continue Phase 1 by completing Networking Fundamentals and begin developing all future Linux, Python, and cybersecurity projects directly inside Ubuntu using WSL2 and Visual Studio Code.