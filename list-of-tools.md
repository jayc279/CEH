
### Recommended Tools
*most of the security tools listed below are included in Kali-Linux - check before use*
* Nmap, Masscan	 - Network Port mapping. Masscan is faster than Nmap, mostly used when a large number of hosts need to be scanned.
* John the Ripper, Hydra - Password Cracker
* Wireshark - Network Protocol Analyzer (how info flows in n/w)
* Metasploit - identify and exploit vulnerabilities - includes exploits, payloads, auxiliary functions, etc.
* Aircrack-NG - analyze and crack wireless networks
* SQLmap - to exploit SQL injection flaws and take-over of database.
* SQLInjection - identify potential vulnerabilities in web applications that could be expoited by SQL injection attacks
* Recon-ng - web-based reconnaissance/OSINT framework
* Autopsy - Digital Forensic Investigation
* SET - Social Engineering Toolkit, automates a wide range of attacks: spear phising, credential harvesting, website cloning, etc.
* Maltego - Intelligence and Forensic - gather, analyze, and visualize publicly available information
* Google Dorking - use of advance search operators to find specific information in search results
* OSINT (Open Source Intelligence) gathering - Also known as Passive Reconnaissance.
    - Usually centers around uncovering activities as part of an investigation about an identity on the internet
    - Google Dorking, Facebook, Twitter, Github search and other available public sources. 
* OSWAP ZAP  - OpenWeb Application Security Project Zed Attack Proxy - detects vulnerabilites & security issues in web applications
* tshark - command line network protocol analyzer - part of Wireshark
* dumpcap - captures network traffic and writes to a file - setup up scripts to continuously monitor
* Burp Suite - similar to OWASP ZAP, but has more functionality such as Repeater, Intruder, etc. Community version shipped with Kali Linux
* Shodan - specifically designed for IoT devices, used in passive reconnaissance, used to discover internet facing servers, control systems, etc.
* DirBuster - is an application desgined to brute-force files/directory names on web application servers - uses a word list to scan
* BeEF - Browser Exploitation Framework. Assesses the security posture of a target environment by using client-side attacks
* Nikto - highly effective command-line vulnerability scanner. Scans web servers for dangerous files/programs, outdated software, mis-configurations, etc.
* Nessus - security scanning tool, raises alerts if it finds any vulnerabilities in the system and/or network that hackers could exploit
* DNSenum - command line tool that identifies DNS, MX, NS, etc records of a domain - used in passive reconnaissance
* Fierce - similar to dnsenum - unveils additional domains; like subdomains - extend scan to include all IPs in the /24 subnet (CIDR) - 
* Dirb - similar to dirbuster, discovers hidden files and directories on a web-site
* Snort - primarily used as a IPS/IDS - monitors network traffic for suspicious activity analyzing packets against predefined rules.
* HPing3  - version3. Port scanning, remote OC finger-printing
* P0f  - used in routine network monitoring, detection of unautorized network activity - no packets are sent to target making it harder to detect. 
* Httprint  - gather as well as analyze signatures - identifies web server characteristics even if they are obfuscated.
* Scanners - site specific; WPScan (WordPress scan), Drupal security scanner, Joomla scanner, Sharepoint scanner
* Sn1per  - Auto Exploiter -  next-generation [information gathering tool](https://github.com/1N3/Sn1per)

### Utilities
* whois - query displays information about a domain such as where it is registered and where its nameservers are pointing
* ping - primary TCP/IP command used to troubleshoot connectivity, reachability, and name resolution
* nslookup - is a network administration tool used for querying the Domain Name System (DNS) to obtain domain name or IP addres
* traceroute - network diagnostic tool used to trace the route taken by packets from a source to a destination 
* netstat - Displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics.
* arp - network utility tool used to display, add, and remove entries in the Address Resolution Protocol
