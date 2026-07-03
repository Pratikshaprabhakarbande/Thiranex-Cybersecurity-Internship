# Vulnerability Scanner - Complete Guide

A beginner-friendly Python application to scan network ports and detect common security vulnerabilities. This tool helps identify open ports and potential security issues on target systems.

![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Common Vulnerable Ports](#common-vulnerable-ports)
- [Understanding the Results](#understanding-the-results)
- [Security Recommendations](#security-recommendations)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)

---

## ✨ Features

- **Port Scanning**: Scan single ports or port ranges on target systems
- **Vulnerability Detection**: Identify known vulnerable ports and services
- **Banner Grabbing**: Retrieve service information from open ports
- **Detailed Reports**: Generate comprehensive vulnerability reports in text format
- **Colored Output**: Easy-to-read terminal output with color-coded severity levels
- **Multiple Scan Options**:
  - Quick scan (common ports)
  - Standard scan (ports 1-1024)
  - Full scan (all ports)
  - Custom port ranges
- **Severity Classification**: Categorize vulnerabilities as CRITICAL, HIGH, MEDIUM, or LOW
- **Security Recommendations**: Actionable advice to improve system security

---

## 🔧 Prerequisites

- **Python 3.7 or higher**
  - Check your Python version:
  ```bash
  python --version
  ```
  
- **Windows, macOS, or Linux operating system**
- **Administrator/Root privileges** (optional, for scanning well-known ports)
- **Network connectivity** to target systems
- **Firewall permissions** (may need to allow outbound connections)

---

## 📦 Installation

### Step 1: Clone or Download the Project

```bash
# Download or clone the project to your local machine
cd "path/to/Thiranex task 2"
```

### Step 2: Verify Python Installation

```bash
# Verify Python is installed
python --version

# If python doesn't work, try python3
python3 --version
```

### Step 3: Install Dependencies (Optional)

The current version uses only Python standard library, so no additional packages are required!

If you want to use advanced features, install optional dependencies:

```bash
# Navigate to project directory
cd "path/to/Thiranex task 2"

# Install requirements (if you uncomment them in requirements.txt)
pip install -r requirements.txt
```

---

## 🚀 Usage

### Basic Usage

```bash
# Navigate to project directory
cd "path/to/Thiranex task 2"

# Run the scanner
python main.py
```

### Step-by-Step Guide

1. **Start the Scanner**
   ```bash
   python main.py
   ```

2. **Enter Target Address**
   - IP address: `192.168.1.1`
   - Hostname: `example.com` or `localhost`
   - Local machine: `localhost` (recommended for beginners)

3. **Select Scan Range**
   - Option 1: Quick scan (fastest, common ports)
   - Option 2: Standard scan (ports 1-1024)
   - Option 3: Full scan (all ports, very slow)
   - Option 4: Custom range (specify your own ports)

4. **Review Results**
   - Terminal displays open ports in real-time
   - Vulnerabilities are highlighted with color codes
   - A detailed report is automatically generated

### Example Commands

```bash
# Scan localhost with quick scan
python main.py
# Enter: localhost
# Select: 1 (Quick scan)

# Scan a specific website
python main.py
# Enter: example.com
# Select: 2 (Standard scan)

# Scan custom ports
python main.py
# Enter: 192.168.1.100
# Select: 4 (Custom)
# Enter: 80,443,8080 or 1000-2000
```

### Output Files

After each scan, a vulnerability report is saved:
```
vulnerability_report_20240115_143022.txt
```

This file contains:
- Scan timestamp and target information
- Summary of findings
- Detailed vulnerability analysis
- Security recommendations

---

## 🔍 How It Works

### Port Scanning Process

1. **Connection Attempt**
   - Sends TCP connection request to each port
   - Waits for response (default 1 second timeout)
   - Port is "Open" if connection is accepted
   - Port is "Closed" if connection is refused

2. **Vulnerability Analysis**
   - Checks open ports against known vulnerable port list
   - Retrieves service information (banner grabbing)
   - Assesses severity level
   - Provides recommendations

3. **Report Generation**
   - Compiles all findings
   - Categorizes by severity
   - Includes actionable recommendations

### TCP Connection Scanning Explanation

```
Computer A (Scanner)           Computer B (Target)
     |                              |
     |------[SYN packet]----------->|
     |                              |
     |<-----[SYN-ACK packet]--------|  <- Port is OPEN
     |                              |
     |------[RST packet]----------->|
     |                              |
```

- **Open Port**: Target responds with SYN-ACK
- **Closed Port**: Target responds with RST or no response

### Why This Method?

✅ **Advantages:**
- Most reliable method
- Works through most firewalls
- Shows actual accessible services

⚠️ **Limitations:**
- Leaves log traces on target systems
- May trigger security alerts
- Not stealthy (use only for authorized testing)

---

## 📊 Common Vulnerable Ports

### CRITICAL Severity

| Port | Service | Vulnerability | Recommendation |
|------|---------|----------------|-----------------|
| **23** | Telnet | Unencrypted remote access | Use SSH (port 22) instead |
| **3306** | MySQL | Exposed database | Never expose to internet |
| **3389** | RDP | Remote desktop exposure | Restrict access, use strong passwords |
| **5432** | PostgreSQL | Exposed database | Never expose to internet |
| **27017** | MongoDB | Exposed NoSQL database | Never expose to internet |

### HIGH Severity

| Port | Service | Vulnerability | Recommendation |
|------|---------|----------------|-----------------|
| **21** | FTP | Unencrypted file transfer | Use SFTP (port 22) instead |
| **80** | HTTP | Unencrypted web traffic | Use HTTPS (port 443) |
| **110** | POP3 | Unencrypted email | Use TLS/SSL encryption |
| **143** | IMAP | Unencrypted email | Use TLS/SSL encryption |
| **445** | SMB | File sharing exposure | Restrict to internal networks |
| **5900** | VNC | Remote desktop unencrypted | Use SSH tunneling |

### MEDIUM Severity

| Port | Service | Vulnerability | Recommendation |
|------|---------|----------------|-----------------|
| **25** | SMTP | May allow relay abuse | Implement proper authentication |
| **53** | DNS | May allow enumeration | Restrict query types |
| **8080** | HTTP Proxy | Proxy exposure | Review firewall rules |

### LOW Severity

| Port | Service | Notes | Recommendation |
|------|---------|-------|-----------------|
| **443** | HTTPS | Secure but verify certificate | Ensure valid SSL/TLS certificate |
| **22** | SSH | Secure if properly configured | Use strong key pairs, not passwords |

---

## 📈 Understanding the Results

### Terminal Output Example

```
============================================================
     VULNERABILITY SCANNER - Port Scanner & Detector
     A Beginner-Friendly Security Tool
============================================================

[*] Starting port scan on 127.0.0.1...
[*] Scanning 10 ports...

[+] Port 80: Open
[+] Port 443: Open

[*] Analyzing vulnerabilities...

[!] Port 80 (HTTP) - Severity: HIGH
    ├─ Issue: Unencrypted web traffic - use HTTPS
    └─ Banner: Apache/2.4.41 (Ubuntu)

[!] Port 443 (HTTPS) - Severity: LOW
    ├─ Issue: Secure web traffic (needs certificate validation)
    └─ Banner: Not available
```

### Report Example

Generated report includes:
- **Scan metadata**: Date, time, duration, target
- **Statistics**: Number of open ports, vulnerabilities by severity
- **Detailed findings**: Each open port with service name and vulnerability description
- **Security recommendations**: Actionable advice for improvement

---

## 🛡️ Security Recommendations

### 1. Firewall Configuration
- **Close unnecessary ports** using firewall rules
- **Block by default**, allow only required ports
- **Use IP whitelisting** where possible
- Test rules: Run scanner from trusted network

### 2. Service Hardening
- **Disable unused services** completely
- **Update to latest versions** regularly
- **Remove default credentials**
- **Configure security settings** properly

### 3. Encryption & Protocols
| Old Method | Port | New Method | Port |
|-----------|------|-----------|------|
| Telnet | 23 | SSH | 22 |
| FTP | 21 | SFTP | 22 |
| HTTP | 80 | HTTPS | 443 |
| POP3 | 110 | POP3S | 995 |
| IMAP | 143 | IMAPS | 993 |
| SMTP | 25 | SMTPS | 465 |

### 4. Access Control
- **Use VPN** for remote connections
- **Enable MFA** on all admin accounts
- **Restrict database access** to application servers only
- **Monitor access logs** regularly

### 5. Network Segmentation
- **Separate zones**: DMZ, internal, management networks
- **Limit inter-zone communication**
- **Use network firewalls** between zones

### 6. Regular Monitoring
- **Scan regularly** (weekly or monthly)
- **Review logs** for suspicious activity
- **Use IDS/IPS** for threat detection
- **Set up alerts** for open port changes

---

## 🐛 Troubleshooting

### Problem: "Permission denied" or port access errors

**Solution 1: Administrator/Root Privileges**
```bash
# Windows (run as administrator)
python main.py

# macOS/Linux (use sudo for privileged ports)
sudo python3 main.py
```

**Solution 2: Use unprivileged ports**
- Select custom port range: 1024-65535
- These don't require elevated privileges

### Problem: "Hostname could not be resolved"

**Check:**
1. Is the hostname spelled correctly?
2. Is your network connection active?
3. Can you ping the host?
   ```bash
   ping example.com
   ```

**Solution:**
- Use IP address instead of hostname
- Check DNS settings
- Verify internet connectivity

### Problem: Scan is very slow

**Causes and Solutions:**
- Scanning too many ports? Use quick scan (option 1)
- Network latency? Reduce scan range
- Firewall blocking? Try from different network
- Target is slow? Increase timeout (edit main.py)

### Problem: Getting "Connection refused" for all ports

**Possible causes:**
1. Wrong target address
2. Target is offline
3. Firewall blocking all connections
4. Scanning localhost but service not running

**Solution:**
- Verify target is online: `ping target_address`
- Check if expected services are running
- Verify firewall settings

### Problem: Python command not found

**Solution:**
```bash
# Try python3 instead
python3 main.py

# Or add Python to PATH (Windows)
# On Windows, during Python installation, check "Add Python to PATH"
```

---

## 📁 Project Structure

```
Thiranex task 2/
├── main.py                              # Main vulnerability scanner application
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
└── sample_vulnerability_report.txt      # Example report output
```

### File Descriptions

**main.py**
- Complete vulnerability scanner implementation
- ~400+ lines of well-commented code
- Port scanning, vulnerability detection, report generation
- Colored terminal output for better readability

**requirements.txt**
- Lists all Python packages needed
- Currently uses only standard library
- Optional packages for advanced features commented out

**README.md**
- Comprehensive documentation (this file)
- Setup and installation instructions
- Usage examples and troubleshooting
- Security best practices

**sample_vulnerability_report.txt**
- Example output from a vulnerability scan
- Shows report format and information structure
- Reference for understanding results

---

## 📚 Learning Resources

### Understanding Network Security

1. **Ports & Protocols**
   - Ports 0-1023: Well-known/privileged ports
   - Ports 1024-49151: Registered ports
   - Ports 49152-65535: Dynamic/private ports

2. **Common Services**
   - Port 22: SSH (Secure Shell)
   - Port 80: HTTP (Web)
   - Port 443: HTTPS (Secure Web)
   - Port 3306: MySQL Database

3. **Security Concepts**
   - **Defense in Depth**: Multiple layers of security
   - **Least Privilege**: Only necessary permissions
   - **Security by Default**: Safe settings out of the box
   - **Zero Trust**: Don't trust, always verify

### Online Resources

- [OWASP Port Security](https://owasp.org/)
- [CIS Benchmarks](https://www.cisecurity.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Python Socket Documentation](https://docs.python.org/3/library/socket.html)

---

## ⚠️ Important Legal Notice

### Authorization Required

- **ONLY scan systems you own or have explicit permission to scan**
- Unauthorized scanning may be illegal in your jurisdiction
- Violating computer security laws can result in criminal charges
- Always have written authorization before scanning other systems

### Responsible Use

✅ **Allowed:**
- Test your own systems
- Security research with authorization
- Educational learning
- Authorized penetration testing

❌ **Not Allowed:**
- Scanning without permission
- Scanning employer's network without authorization
- Illegal security research
- Unauthorized access attempts

---

## 🚀 Getting Started (Quick Start)

For absolute beginners:

1. **Install Python 3.7+** from python.org
2. **Download this project**
3. **Open terminal/command prompt**
4. **Navigate to project directory**
5. **Run: `python main.py`**
6. **Enter: `localhost`** for your first scan
7. **Select: `1` for quick scan**
8. **View the report generated!**

---

## 📝 Sample Scan Output

```
Enter target IP address or hostname (or 'localhost' to scan local machine):
>>> localhost

[*] Resolving target address...
[✓] Target: localhost (127.0.0.1)

Select scan range:
1. Quick scan (common ports: 21-23, 80, 443, 3306, 3389, 5432)
2. Standard scan (ports 1-1024)
3. Full scan (ports 1-65535 - may take long!)
4. Custom port range

>>> 1

[*] Starting port scan on 127.0.0.1...
[*] Scanning 10 ports...

[+] Port 80: Open
[+] Port 443: Open

[*] Analyzing vulnerabilities...

[!] Port 80 (HTTP) - Severity: HIGH
    ├─ Issue: Unencrypted web traffic - use HTTPS
    └─ Banner: Apache/2.4.41 (Ubuntu)

[✓] Report saved to: vulnerability_report_20240115_143022.txt
```

---

## 💡 Tips for Best Results

1. **Start with localhost** to understand how it works
2. **Use quick scan** for initial assessment
3. **Run scans during off-peak hours** to minimize impact
4. **Compare scans over time** to track security improvements
5. **Read the security recommendations** in reports carefully
6. **Document all findings** for audit trails
7. **Act on high/critical findings** promptly

---

## 🤝 Contributing & Support

- Found a bug? Document steps to reproduce
- Have improvements? Submit suggestions
- Questions? Review the Troubleshooting section
- Want to learn more? Check Learning Resources

---

## 📄 License

This project is provided for educational and authorized security testing purposes.
Always ensure you have proper authorization before scanning any system.

---

## ✅ Version History

- **v1.0** (2024-01)
  - Initial release
  - Port scanning functionality
  - Vulnerability detection
  - Report generation
  - Colored output support

---

## 🎓 Educational Value

This project teaches:
- Python socket programming
- Network security concepts
- Vulnerability assessment basics
- Report generation and documentation
- Exception handling and error management
- Command-line application development

Perfect for learning:
- Cybersecurity fundamentals
- Python programming
- Network protocols
- Security awareness

---

**Disclaimer:** This tool is for educational and authorized testing only. Unauthorized network scanning is illegal. Always obtain proper authorization before scanning systems you don't own.

**Happy scanning! Stay secure! 🛡️**
