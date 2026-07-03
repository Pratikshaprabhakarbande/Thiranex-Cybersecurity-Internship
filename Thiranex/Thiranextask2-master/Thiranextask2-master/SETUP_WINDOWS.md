# SETUP GUIDE - Windows Installation

## 🪟 Setting Up on Windows

This guide walks you through installing Python and running the Vulnerability Scanner on Windows.

---

## Step 1: Install Python

### Option A: Download from python.org (Recommended)

1. Go to **https://www.python.org/downloads/**
2. Click **"Download Python 3.10"** (or latest version)
3. Run the installer
4. **IMPORTANT:** Check ☑️ **"Add Python to PATH"**
5. Click **"Install Now"**
6. Wait for installation to complete

### Option B: Install from Microsoft Store

1. Press `Windows Key` and search "Microsoft Store"
2. Search for "Python 3.10" or "Python 3.11"
3. Click "Get" to install
4. Python will be automatically added to PATH

### Verify Python Installation

1. Press `Windows Key + R`
2. Type `cmd` and press Enter
3. In the command prompt, type:
   ```
   python --version
   ```
4. You should see: `Python 3.x.x` or similar
5. If not found, restart your computer and try again

---

## Step 2: Navigate to Project Folder

1. Press `Windows Key + R`
2. Type `cmd` and press Enter
3. In the command prompt, type the following (replace with your path):
   ```
   cd C:\Users\YourName\Desktop\Thiranex task 2
   ```

### Finding Your Path

If you're not sure of the path:
1. Open File Explorer
2. Navigate to the "Thiranex task 2" folder
3. Click the address bar and copy the path
4. Replace `C:\Users\YourName\Desktop\Thiranex task 2` with your copied path

---

## Step 3: Run the Scanner

In the command prompt, type:
```
python main.py
```

If that doesn't work, try:
```
python3 main.py
```

---

## Troubleshooting

### "Python is not recognized"

**Solution 1:** Restart computer
- Python might not be in PATH until restart
- Restart and try again

**Solution 2:** Check Python location
```
# In Command Prompt, try:
py --version
# If this works, use:
py main.py
```

**Solution 3:** Add Python to PATH manually
1. Find Python installation folder (usually `C:\Users\YourName\AppData\Local\Programs\Python\Python310`)
2. Press `Windows Key + X`
3. Select "System"
4. Click "Advanced system settings"
5. Click "Environment Variables"
6. Under "System variables", select "Path" and click "Edit"
7. Click "New" and paste your Python folder path
8. Click "OK" and restart Command Prompt

### "Module not found"

The project uses only Python standard library. If you get module errors:
1. Ensure Python 3.7+ is installed
2. Try reinstalling Python

### Scanner runs but exits immediately

1. Make sure you're in the correct directory
2. Check that `main.py` is in that folder
3. Try running again - it should wait for your input

---

## Example: Complete Setup

```
# 1. Download and install Python from python.org
#    (Check "Add Python to PATH")

# 2. Open Command Prompt (Windows Key + R, type cmd)

# 3. Navigate to project folder
cd C:\Users\JohnDoe\Desktop\Thiranex task 2

# 4. Run the scanner
python main.py

# 5. Enter target (try localhost for first test)
localhost

# 6. Select quick scan
1

# 7. View results!
```

---

## Using Advanced Options (Optional)

If you want to use optional advanced features:

```
# Install optional dependencies
pip install python-nmap requests colorama

# Then run normally
python main.py
```

---

## Command Prompt Tips

```
# Show current directory
cd

# List files in current directory
dir

# Go back one folder
cd ..

# Go to specific folder
cd C:\path\to\folder

# Clear screen
cls

# Stop running program
Ctrl + C
```

---

## 🆘 Still Having Issues?

1. **Python won't install?**
   - Try Microsoft Store version
   - Restart after installation
   - Check Windows Updates

2. **Can't find folder?**
   - Use File Explorer to navigate
   - Copy the path from address bar
   - Paste into command prompt

3. **Scanner starts but exits?**
   - Make sure all files are in folder
   - Check folder name doesn't have special characters
   - Try running from different location

4. **Getting permission errors?**
   - Run Command Prompt as Administrator
   - Right-click cmd.exe → "Run as administrator"

---

## ✅ Success Checklist

- [ ] Python 3.7+ installed
- [ ] Python is in PATH (`python --version` works)
- [ ] Can navigate to project folder
- [ ] Can see main.py in folder (`dir` command)
- [ ] `python main.py` starts without errors
- [ ] Can enter target and run scan

---

## Next Steps

1. Scan localhost (safe for learning)
2. Review generated report
3. Read README.md for full documentation
4. Scan your website/server
5. Follow security recommendations

---

**You're all set! Ready to run your first vulnerability scan! 🛡️**

For more help, see: README.md and QUICK_START.md
