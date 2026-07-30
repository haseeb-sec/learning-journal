# Progress Log — Haseeb Ullah Shah

## Session 1 — 15/06/2026

**What I completed:** Configured my Python development environment by installing Git, Visual Studio Code, Python, and creating my learning-journal repository on GitHub. Made my first Git commit and successfully pushed it to GitHub.

**What I learned:** Learned the fundamentals of Git and GitHub, version control, and how a GitHub repository serves as a public record of my learning journey and technical progress.

**What confused me:** TryHackMe account creation failed because of a browser compatibility issue. Switching from Chrome to Microsoft Edge resolved the problem.

**Next step:** Start Phase 1 by learning Linux command-line fundamentals through TryHackMe.

## Session 2 — 18/06/2026

**What I completed:** Practiced Linux navigation commands, explored a real web server access log, searched for specific patterns, identified bot traffic, and counted POST requests using standard Linux utilities.

**What I learned:** Learned how to navigate the Linux filesystem using pwd, ls, and cd, inspect files with cat, head, and tail, and search text efficiently using grep. I also gained my first exposure to analyzing server log files from a security perspective.

**What confused me:** The TryHackMe virtual machine disconnected after being idle, making me think something had gone wrong. I later learned that temporary lab machines automatically reset after inactivity.

Real-world security connection: Security analysts regularly inspect web server logs to identify suspicious requests, automated scanners, bot activity, and indicators of unauthorized access. This session introduced me to one of the most common tasks performed during security monitoring.

**Next step:** Continue Linux Fundamentals by learning file permissions and file management.

## Session 3 — 04/07/2026

**What I completed:** Practiced Linux file permissions by creating files, viewing permission settings, and modifying permissions using chmod. Successfully changed file permissions from overly permissive settings to safer defaults.

**What I learned:** Learned how Linux file permissions work, how to interpret ls -l output, and how numeric permission values control read, write, and execute access for different users.

**What confused me:** While already inside folder1, I mistakenly tried listing folder1 again, which helped me better understand relative paths and my current working directory.

Real-world security connection: Correct file permissions help protect sensitive data and reduce unnecessary access. Misconfigured permissions are a common source of security vulnerabilities on Linux systems.

**Next step:** Continue Linux Fundamentals by practicing file creation, copying, moving, and deletion.

## Session 4 — 04/07/2026

**What I completed:** Created, copied, moved, renamed, and deleted files and directories using standard Linux commands while practicing independent filesystem management.

**What I learned:** Learned how to use mkdir, touch, echo, cp, mv, rm, and rm -r to manage files and directories efficiently from the command line.

**What confused me:** I attempted to enter folder3 while already inside another directory and initially became confused about relative paths before understanding how directory navigation works.

**Real-world security connection:** File management is a fundamental skill for Linux system administration, incident response, malware analysis, and security automation, where files and logs must frequently be organized and managed.

**Next step:** Learn Linux networking commands and understand how they are used during security investigations.

## Session 5 — 07/07/2026

**What I completed:** Investigated a live TryHackMe machine as if it were a compromised Linux server. Identified its IP address, tested external connectivity, examined listening services, inspected active network connections, and verified the integrity of the /etc/hosts file.

**What I learned:** Learned how to use ip addr, ping, ss -tuln, ss -tn, and cat /etc/hosts to collect networking information and perform basic system reconnaissance during an investigation.

**What confused me:** Although I understood what each command did individually, I struggled to understand why they were used together during a security investigation. I also found the concept of open ports confusing and did not initially understand why they represent potential attack surfaces.

**How it got cleared:** Understanding improved after working through a real-world investigation scenario involving an online store. Viewing each command as a question a security analyst asks during incident response—identifying the system, checking connectivity, discovering exposed services, inspecting active connections, and verifying possible tampering—connected the commands into a complete investigation workflow.

**Real-world security connection:** These networking commands form part of the initial investigation process used by security analysts when examining Linux servers for signs of compromise, unauthorized access, or service exposure.

**Next step:** Complete the Linux Fundamentals Part 1 room on TryHackMe and begin learning Python fundamentals.

## Linux Fundamentals Part 1 — TryHackMe — 07/07/2026

**What I completed:** Successfully completed the Linux Fundamentals Part 1 room on TryHackMe, reinforcing everything I had previously practiced through hands-on Linux exercises. I answered the room questions independently and gained practical experience using the Linux command line.

**Points earned:** 88

**What I learned:** Strengthened my understanding of essential Linux commands, including `pwd`, `ls`, `cd`, `echo`, `cat`, `grep`, `chmod`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `ip addr`, `ping`, `ss -tuln`, and `ss -tn`. I became more confident navigating the Linux filesystem, managing files and permissions, and performing basic networking tasks.

**What confused me:** Nothing major. The room served as a review of the concepts I had already learned, and completing the exercises confirmed that I understood the fundamentals.

**Real-world security connection:** Linux is the primary operating system used for servers, cloud infrastructure, penetration testing, and many cybersecurity tools. Building confidence with the Linux command line provides the foundation for future work in system administration, security automation, and incident response.

**Next step:** Begin learning Python fundamentals and start building small automation projects.

## Python Basics — 07/07/2026

**What I completed:** Revised the core Python fundamentals, including variables, data types, loops, conditionals, functions, and file handling. Although I had studied these concepts previously, I completed a focused revision to strengthen my understanding before building real-world security tools.

**What I learned:** Refreshed my understanding of how variables store data, how different data types are used, how loops automate repetitive tasks, and how conditionals control program flow. I also revised creating and calling functions to write reusable code and practiced reading files in Python, which is essential for processing logs and automating security tasks.

**What confused me:** Nothing significant. Since this was primarily a revision session, the concepts were familiar and helped reinforce my existing knowledge.

**Real-world security connection:** These Python fundamentals form the foundation of security automation. Concepts such as loops, conditionals, functions, and file handling are used in tools that analyze logs, scan networks, process reports, and automate repetitive cybersecurity tasks.

**Next step:** Build my first Python security project by applying these fundamentals to a real-world problem.

## Python Project — Log Analyzer — 07/08/2026

**What I completed:** Built a CLI-based Log Analyzer in Python that reads a web server `access.log` file, extracts client IP addresses, counts the total requests made by each IP, identifies suspicious IPs based on a configurable request threshold, and automatically generates a clean `report.txt` summarizing the analysis.

**What I learned:** I learned how to build a complete Python application by combining variables, loops, conditionals, functions, dictionaries, and file handling. I practiced reading log files line by line, extracting useful information from each entry, organizing data using dictionaries, identifying suspicious activity based on request frequency, and generating an automated security report. I also gained experience structuring code into reusable functions and developing a practical command-line security tool.

**What confused me:** Nothing significant. This project reinforced the Python fundamentals I had recently revised and gave me confidence applying them to solve a real-world security problem.

**Real-world security connection:** Log analysis is one of the most common tasks performed by security analysts and incident responders. Web server logs are routinely examined to identify suspicious traffic, brute-force attempts, automated scanners, and other indicators of compromise. This project automated a simplified version of that investigation process.

**Next step:** Build a multithreaded Python Port Scanner to strengthen my understanding of networking, sockets, and TCP communication.


## Python Project — Port Scanner — 07/08/2026

**What I completed:** Built a CLI-based Python Port Scanner that scans a target IP address over a specified range of ports, identifies which ports are open, displays the results in the terminal, and automatically generates a `scan_report.txt` file containing the scan results.

**What I learned:** I learned how to use Python's `socket` module to establish TCP connections and determine whether a port is open or closed. I also learned how to scan a range of ports using loops, organize the program into reusable functions, handle connection timeouts, store the discovered open ports in a list, and automatically generate a well-formatted report containing the scan results.

**What confused me:** Understanding the `socket` module and the networking terminologies such as `AF_INET` and `SOCK_STREAM` was initially confusing because they were completely new to me. After discussing these concepts and studying them further, I understood that a socket is the endpoint used to establish a network connection, `AF_INET` specifies that the connection uses the IPv4 address family, and `SOCK_STREAM` specifies that the connection uses the TCP protocol. Once I understood how these components work together, the overall logic of the port scanner became much clearer.

**Real-world security connection:** Port scanning is commonly used by security professionals to identify exposed services on a target system. Knowing which ports are open helps determine the attack surface and provides the foundation for further security assessment.

**Next step:** Improve the Log Analyzer by adding bot detection, failed login detection, and command-line arguments so it can analyze any log file instead of relying on a hardcoded filename.

## Python Project — Log Analyzer Update — 07/14/2026

**What I completed:** Enhanced the Log Analyzer by adding support for command-line arguments using the `sys` module, allowing the program to analyze any log file specified by the user instead of relying on a hardcoded filename. I also added bot and crawler detection by identifying common user-agent keywords such as `Bot`, `bot`, `crawler`, and `spider`. In addition, I implemented failed login detection by analyzing HTTP `401 Unauthorized` responses and flagging IP addresses that exceeded a configurable threshold of failed login attempts. Finally, I updated the generated `report.txt` to include dedicated sections for detected bots and suspicious login attempts, making the report more comprehensive and useful.

**What I learned:** I learned how to use the `sys` module and `sys.argv` to accept command-line arguments, making Python scripts more flexible and reusable. I strengthened my understanding of dictionaries by using them to count failed login attempts for each IP address and practiced creating multiple detection functions that each perform a specific task. I also learned how basic security monitoring can be performed by analyzing web server logs for suspicious request patterns, automated bots, crawlers, and repeated authentication failures. This project also reinforced the importance of writing modular, reusable code by separating each detection feature into its own function.

**What confused me:** Understanding command-line arguments with `sys.argv` was initially new because I had only executed Python scripts by clicking the Run button in Visual Studio Code. After experimenting with the program and learning how arguments are passed from the command line, I understood how Python receives user input through `sys.argv` and why this approach makes CLI tools more practical and reusable.

**Real-world security connection:** Web server logs provide valuable information for detecting suspicious activity. Automating the detection of bots, repeated failed logins, and unusual request patterns helps security analysts identify potential attacks more efficiently.

**Next step:** Add multithreading to the Port Scanner.

## Python Project — Port Scanner (Multithreading Upgrade) — 07/14/2026

**What I completed:** Improved my CLI-based Python Port Scanner by implementing multithreading using Python's `threading` module. Instead of scanning ports one by one, the scanner now creates a separate thread for each port, allowing multiple ports to be scanned concurrently. I also updated the project documentation to reflect the new functionality and features.

**What I learned:** I learned the fundamentals of multithreading in Python and how it can significantly improve the performance of a port scanner. I learned how to create and manage threads using `threading.Thread()`, how the `target` and `args` parameters work, why `start()` is required to begin a thread, why `join()` is used to wait for all threads to finish, and how multiple threads can share the same `open_ports` list to store scan results. I also learned the difference between creating a thread and actually starting it, and how multithreading allows multiple ports to be scanned at the same time instead of sequentially.

**What confused me:** The multithreading concepts were completely new to me, especially understanding what a thread actually is, how multiple threads run concurrently, why a separate function was needed for each thread, and the purpose of `threading.Thread()`, `target`, `args`, `start()`, and `join()`. These concepts were initially difficult to visualize, but after studying them step by step, the overall workflow became much clearer.

**Real-world security connection:** Multithreading is widely used in security tools to improve performance when performing repetitive network operations such as port scanning. Scanning multiple ports concurrently makes the tool significantly faster and more practical for real-world use.

**Next step:** Build a Web Request Tool using Python's `requests` library.

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

## Python Project - DNS Reconnaissance Tool - 07/25/2026

**What I completed:** Built a CLI-based DNS Reconnaissance Tool in Python that accepts a target domain as a command-line argument, performs DNS resolution, checks whether the website is reachable over HTTPS, retrieves WHOIS information, extracts the most important registration details, and automatically generates a clean reconnaissance report. I also completed the project entirely inside my Ubuntu WSL2 development environment and pushed it to GitHub.

**What I learned:** I learned how to perform DNS lookups using Python's `socket` module, send HTTP requests using the `requests` library, execute Linux commands from Python using `subprocess.run()`, and parse raw WHOIS output into a concise report. Beyond the project itself, I gained practical experience with networking tools such as `traceroute`, `curl`, `dig`, `whois`, and `ufw`, understanding how they relate to DNS resolution, routing, HTTP/HTTPS communication, TLS, and basic firewall management. I also migrated my development workflow completely to Ubuntu WSL2, created and managed Python virtual environments there, and recovered my project after accidentally losing the files before pushing them to GitHub.

**What confused me:** The biggest challenge was understanding the difference between Windows and Ubuntu file systems and working across both environments. Initially, my project was stored in the Windows file system, which caused path and environment confusion until I permanently moved my `learning-journal` into Ubuntu WSL2. I also found `socket.getaddrinfo()` and `subprocess.run()` unfamiliar because they introduced concepts that interact directly with networking and the operating system. Another challenge was connecting networking commands such as `traceroute`, `dig`, `curl`, and `whois` to real cybersecurity investigations instead of viewing them as isolated commands. Working through practical scenarios made these concepts much easier to understand.

**Next Step:** Verify that my existing Bash scripts run correctly inside Ubuntu WSL2 so all projects use a single Linux development environment before continuing with Networking Fundamentals and building more advanced security tools.

# 25-07-2026 — Phase 1 Completion & Ubuntu WSL2 Migration

## What I completed
- Verified all shell scripts on Ubuntu WSL2.
- Confirmed `myscript.sh`, `sysinfo.sh`, `security_audit.sh`, and `log_analyzer.sh` all run correctly in the Ubuntu environment.
- Finished migrating my learning environment to Ubuntu WSL2, which is now my permanent development environment.
- Officially completed Phase 1 of my AI-Augmented Security Engineer roadmap.
- Prepared my repositories for the next stage of learning.

## What I learned
- Working in one consistent environment is much more reliable than switching between Windows PowerShell, Git Bash, and Ubuntu.
- Shell scripts should be tested on a real Linux environment instead of relying on Windows compatibility.
- Verifying and documenting completed work is just as important as writing the code itself.

## What confused me
- I experienced a Git merge conflict because I had previously worked from multiple environments.
- This reinforced the importance of using Ubuntu WSL2 as my single development environment.

## Real-world security connection
- Security engineers rely heavily on Linux systems for scripting, automation, log analysis, and system administration. Verifying my scripts on Ubuntu makes them much closer to real-world usage.

## One thing I can now do independently
- Create, execute, troubleshoot, and verify Bash scripts in Ubuntu WSL2.

## Status
- Networking Fundamentals — Completed
- **Phase 1 — Complete ✓**

# 30-07-2026 — Phase 1.5: CIA Triad & Professional Security Findings

## What I completed
- Studied the CIA Triad (Confidentiality, Integrity, and Availability).
- Connected the CIA Triad to real-world security incidents and my own Python security tools.
- Learned how professional security findings are written.
- Created `docs/sample-finding.md` for the Web Security Header Analyzer project.
- Wrote three professional security findings based on the assessment of `https://python.org`:
  - Missing Content-Security-Policy Header
  - Missing X-Content-Type-Options Header
  - Missing X-XSS-Protection Header

## What I learned
- Every security incident can be analyzed through the CIA Triad.
- Security tools generate evidence, but security engineers must interpret that evidence and communicate it professionally.
- A professional finding follows a consistent structure:
  - Title
  - Severity
  - Description
  - Evidence
  - Impact
  - Recommendation
- Not every missing security header has the same risk. Modern security assessments require understanding current browser behavior instead of blindly trusting scanner output.

## What confused me
- I initially struggled to understand what each HTTP security header actually did.
- I also assumed every missing security header should receive the same severity rating. Learning why `X-XSS-Protection` is considered Low severity helped me understand that security requires judgment, not just following automated scanner results.

## Real-world security connection
- Security engineers don't stop after discovering a vulnerability. They must document the evidence, explain the business impact, assign an appropriate severity, and provide practical remediation recommendations for clients.

## One thing I can now do independently
- Analyze missing HTTP security headers and write professional security findings based on real assessment results.

## Status
- **Phase 1.5 — Complete ✓**
- **Phase 2 — Ready to Begin**