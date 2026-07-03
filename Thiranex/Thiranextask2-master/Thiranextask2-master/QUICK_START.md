# VULNERABILITY SCANNER - QUICK START GUIDE

## ⚡ Get Started in 2 Minutes!

### Step 1: Open Terminal/Command Prompt

**Windows:**
- Press `Windows Key + R`
- Type `cmd` and press Enter
- Or search for "Command Prompt"

**macOS:**
- Press `Cmd + Space`
- Type `terminal` and press Enter

**Linux:**
- Press `Ctrl + Alt + T`

### Step 2: Navigate to Project Folder

```bash
cd "path/to/Thiranex task 2"
```

Replace "path/to" with where you saved the project. 

Example:
```bash
# Windows
cd C:\Users\YourName\Desktop\Thiranex task 2

# macOS/Linux  
cd ~/Downloads/Thiranex task 2
```

### Step 3: Run the Scanner

```bash
python main.py
```

If that doesn't work, try:
```bash
python3 main.py
```

### Step 4: Follow the Prompts

1. Enter target: `localhost` (for first test)
2. Select scan type: `1` (Quick scan)
3. Review results
4. Check generated report file

**That's it! Your first scan is complete!** ✓

---

## 🎯 Common First Scans

### Scan Your Own Computer
```
Enter target: localhost
Select: 1 (Quick scan)
```

### Scan a Website (by hostname)
```
Enter target: example.com
Select: 1 (Quick scan)
```

### Scan an IP Address
```
Enter target: 192.168.1.1
Select: 2 (Standard scan)
```

### Scan Specific Ports
```
Enter target: localhost
Select: 4 (Custom range)
Enter: 80,443,3306 or 1000-2000
```

---

## 📋 What to Expect

### During Scan:
```
[+] Port 80: Open      ← This shows open ports
[!] Port 80 (HTTP)     ← This shows vulnerabilities
    ├─ Issue: Unencrypted web traffic
    └─ Banner: Apache/2.4.41
```

### Color Meanings:
- 🟢 GREEN = Open port (good connectivity)
- 🔴 RED = Error/Critical issue
- 🟡 YELLOW = Warning/Closed port
- 🔵 BLUE = Information/Action in progress

### After Scan:
- Full report printed to terminal
- Report file saved automatically
- Example: `vulnerability_report_20240115_143022.txt`

---

## ✅ Verification Checklist

- [ ] Python 3.7+ installed (`python --version`)
- [ ] Project files present (main.py, README.md)
- [ ] Terminal open and in project directory
- [ ] Internet connection available
- [ ] Network access to target (if remote)

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "python: command not found" | Use `python3` instead |
| "Permission denied" | Run as admin (Windows) or use `sudo` (Mac/Linux) |
| "Hostname not resolved" | Use IP address instead |
| "Connection refused" | Target may be offline or firewall blocks |
| "Takes too long" | Use option 1 (quick scan) instead |

---

## 📖 Next Steps

1. ✅ Run first scan on localhost
2. 📖 Read README.md for full documentation
3. 🔍 Scan your website or server
4. 💾 Review generated reports
5. 🛡️ Follow security recommendations
6. 📅 Schedule regular scans

---

## ❓ Need Help?

1. Check README.md for detailed documentation
2. Review sample_vulnerability_report.txt for example output
3. Check Troubleshooting section in README
4. Verify Python installation: `python --version`

---

## ⚖️ Important

⚠️ **LEGAL NOTICE**

Only scan systems you own or have written permission to scan.
Unauthorized scanning may be illegal.

✅ Allowed: Your own systems, authorized testing
❌ Not Allowed: Scanning without permission

---

**Ready? Run `python main.py` now!** 🚀

For full documentation, see: README.md
