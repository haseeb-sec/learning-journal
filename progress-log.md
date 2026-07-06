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