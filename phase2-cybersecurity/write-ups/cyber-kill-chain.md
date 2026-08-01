# Cyber Kill Chain

A practical study of the Cyber Kill Chain framework, the WannaCry ransomware attack, and the relationship between defensive security tools and each stage of the attack lifecycle.

## 1. What is the Cyber Kill Chain?

The Cyber Kill Chain is a cybersecurity framework that describes the sequence of steps an attacker typically follows during a cyberattack. It breaks an attack into a series of phases, allowing security professionals to understand how an attack progresses from beginning to end. By viewing an attack as a structured process rather than a single event, the Cyber Kill Chain provides a systematic way to analyze cyber threats and identify opportunities to detect or stop an attack before it succeeds.

## 2. Why does it exist?

The Cyber Kill Chain was originally developed by Lockheed Martin to help defenders understand how cyberattacks progress so they can respond more effectively. Instead of waiting until an attacker successfully compromises a system, the framework enables security teams to detect, interrupt, or stop an attack at different stages of its lifecycle. This proactive approach helps organizations reduce the impact of attacks and strengthen their overall security posture.

## 3. The Seven Stages of the Cyber Kill Chain

### 3.1 Reconnaissance 

During the Reconnaissance stage, attackers gather publicly available information about their target before attempting any attack. They collect details such as IP addresses, domain information, open ports, server technologies, and other publicly accessible data to better understand the target's environment. This process does not involve exploiting vulnerabilities; instead, it focuses on learning as much as possible about the target. The information collected during this stage helps attackers plan and prepare for the later stages of the attack.

### 3.2 Weaponization

During the Weaponization stage, the attacker prepares the tools and components needed to carry out the attack before interacting with the target. This may involve creating or modifying malware, selecting an exploit, preparing ransomware, crafting a malicious document, or developing another type of payload. The attacker combines the exploit with the payload to create a weapon that can achieve the intended objective. Once this preparation is complete, the attack is ready for the next stage.

### 3.3 Delivery

During the Delivery stage, the attacker sends the prepared weapon to the target through a suitable delivery method. Common delivery methods include phishing emails, malicious attachments, malicious websites, or exploiting a vulnerable network service. The primary objective of this stage is to successfully deliver the exploit and payload to the target system. At this point, the attack has reached the target, but the system has not necessarily been compromised yet.

### 3.4 Exploitation

During the Exploitation stage, the attacker takes advantage of a vulnerability in the target system to execute the prepared exploit. If the vulnerability is successfully exploited, the payload is triggered, allowing the attacker to achieve the intended effect, such as executing malicious code or gaining unauthorized access. This is the stage where the target system begins to be compromised. The success of this stage depends on the presence of an exploitable vulnerability and the effectiveness of the prepared exploit.

### 3.5 Installation

During the Installation stage, the attacker establishes a persistent presence on the compromised system after successfully exploiting a vulnerability. This may involve installing malware, ransomware, a backdoor, or another malicious program that allows continued access to the system. The primary objective is to establish persistence and maintain access without repeating the initial exploitation process. This stage enables the attacker to maintain long-term access and continue their activities on the compromised system.

### 3.6 Command and Control (C2)

During the Command and Control (C2) stage, the attacker establishes a communication channel with the compromised system to control it remotely. This channel allows the attacker to send commands, receive data, and manage the malicious software installed during the Installation stage. Communication may occur through various protocols or network services while attempting to blend in with normal network traffic. This stage enables the attacker to remotely manage the compromised system, execute additional commands, transfer data, and coordinate further malicious activities throughout the attack.

### 3.7 Actions on Objectives

During the Actions on Objectives stage, the attacker carries out the primary goal of the attack after successfully progressing through the previous stages. Depending on the attacker's objective, this may involve encrypting files with ransomware, stealing credentials, exfiltrating sensitive data, destroying information, installing cryptominers, or performing financial fraud. This stage represents the point at which the attacker achieves the intended outcome of the attack. All of the previous stages exist to make this final objective possible.

## 4. WannaCry Example

 1. **Reconnaissance** Before launching the attack, the attackers identified systems running vulnerable versions of Microsoft Windows that exposed the SMB service. This information helped them identify potential targets susceptible to the EternalBlue vulnerability.

 2. **Weaponization** The attackers prepared the WannaCry ransomware by combining the EternalBlue exploit with the ransomware payload. This created a weapon capable of exploiting the SMB vulnerability and encrypting files on compromised systems.

 3. **Delivery** The prepared weapon was delivered by sending specially crafted SMB packets to vulnerable systems over the network. The objective of this stage was to deliver the exploit and payload to the target, not yet to compromise it.

 4. **Exploitation** The EternalBlue exploit successfully triggered the SMB vulnerability on unpatched Windows systems. This allowed the ransomware payload to execute and marked the beginning of the compromise.

 5. **Installation** After successful exploitation, the WannaCry ransomware installed itself on the compromised system, established persistence, and prepared to continue its malicious activities.

 6. **Command and Control (C2)** Although WannaCry did not rely on a traditional Command and Control (C2) infrastructure like many other malware families, the Cyber Kill Chain's C2 stage generally represents the point where attackers establish communication with compromised systems to remotely manage them, issue commands, transfer data, or coordinate further malicious activities. In WannaCry's case, the malware included a kill-switch domain that influenced whether it continued executing, making it a useful example for understanding the concept, even though its behavior differed from that of conventional C2-based malware.

 7. **Actions on Objectives** The ransomware encrypted the victim's files and displayed a ransom demand requesting payment in exchange for a decryption key. This stage represented the attacker's primary objective and the final outcome of the attack.

## 5. Mapping My Phase 1 Security Tools

During Phase 1 of my cybersecurity learning journey, I developed several practical tools that support different areas of defensive security. While studying the Cyber Kill Chain, I verified the actual purpose of each tool instead of assuming it belonged to a specific stage. This helped me understand that security tools often serve different functions and do not always map directly to a single Kill Chain stage.

| Tool | Primary Security Function | Relation to the Cyber Kill Chain |
|------|---------------------------|----------------------------------|
| Port Scanner | Reconnaissance | Helps defenders identify exposed services and open ports before attackers discover them. |
| DNS Recon Tool | Reconnaissance | Collects publicly available domain information to help defenders understand and secure their external infrastructure. |
| Web Security Header Analyzer | Security Assessment | Identifies missing or weak HTTP security headers so websites can be hardened before attackers attempt exploitation. |
| Python Log Analyzer | Incident Detection & Response | Detects suspicious activity from log files and helps investigate attacks that may occur across multiple Kill Chain stages. |
| Bash Log Analyzer | Incident Detection & Response | Analyzes web server logs to identify unusual behavior such as excessive requests, POST activity, and suspicious 404 errors. |
| Security Audit Script | Security Auditing & Hardening | Reviews local system configurations, open ports, login activity, and insecure permissions to reduce the attack surface before exploitation occurs. |
| System Information Script | System Administration / System Inventory | Collects basic system information to help administrators understand the current environment before performing maintenance or security tasks. |

Rather than forcing every tool into a single Cyber Kill Chain stage, I learned to classify each tool according to its actual security purpose and how it supports defensive security.

## 6. Key Lessons Learned

Studying the Cyber Kill Chain helped me understand that cyberattacks are structured processes rather than isolated events. Each stage builds upon the previous one, giving defenders multiple opportunities to detect, interrupt, or prevent an attack before it reaches its objective.

One of the most important lessons I learned during this exercise was that not every security tool belongs to a specific Cyber Kill Chain stage. Some tools support reconnaissance and security assessment before an attack occurs, while others help detect, investigate, respond to, or prevent attacks after they have started. Understanding the actual purpose of each tool is more valuable than forcing it into a single stage of the Kill Chain.

Another important lesson was the value of verification. Instead of assuming where my own projects belonged, I executed each tool, reviewed its functionality, and verified its role in defensive security. This process strengthened my understanding of both the Cyber Kill Chain and the practical use of security tools.

This document represents my first verified cybersecurity write-up in Phase 2, built from practical experimentation, tool verification, and real-world examples rather than memorization.

## 7. References

- Lockheed Martin. *Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains.*
- MITRE ATT&CK Framework: https://attack.mitre.org/
- CISA. *Ransomware Guide*: https://www.cisa.gov/stopransomware/ransomware-guide
- Microsoft Learn – Security Documentation: https://learn.microsoft.com/security/

## 8. Disclaimer

This document is intended for educational purposes and reflects my current understanding as I continue learning cybersecurity. As I gain more practical experience and study advanced topics, I will update this document to reflect improved knowledge and industry best practices.