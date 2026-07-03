# SETUP GUIDE - macOS Installation

## 🍎 Setting Up on macOS

This guide walks you through installing Python and running the Vulnerability Scanner on macOS.

---

## Step 1: Check if Python is Installed

1. Open Terminal (Press `Cmd + Space`, type `terminal`)
2. Type the following command:
   ```
   python3 --version
   ```
3. You should see: `Python 3.x.x` or similar

If Python is installed, skip to Step 3.

---

## Step 2: Install Python

### Option A: Using Homebrew (Recommended)

If you don't have Homebrew, install it first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Python:
```bash
brew install python3
```

### Option B: Direct Download

1. Go to **https://www.python.org/downloads/macos/**
2. Download the latest macOS installer
3. Run the installer
4. Follow the installation wizard

### Option C: Using MacPorts

```bash
sudo port install python310
```

---

## Step 3: Navigate to Project Folder

1. Open Terminal (Cmd + Space, type `terminal`)
2. Type the following command:
   ```bash
   cd ~/Downloads/Thiranex\ task\ 2
   ```

   Or use the full path:
   ```bash
   cd /path/to/Thiranex\ task\ 2
   ```

### Finding Your Path

If you're unsure:
1. Open Finder
2. Navigate to "Thiranex task 2" folder
3. Right-click folder → "Copy as Pathname"
4. In Terminal, type `cd ` and paste the path
5. Press Enter

---

## Step 4: Run the Scanner

In Terminal, type:
```bash
python3 main.py
```

---

## Troubleshooting

### "Python3 not found"

**Solution 1:** Install Python with Homebrew
```bash
# Install Homebrew first (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install Python
brew install python3
```

**Solution 2:** Check Python location
```bash
which python3
```

If it shows a path, Python is installed.

### "Permission denied"

Some ports require administrator privileges:
```bash
sudo python3 main.py
```

You'll be prompted for your Mac password.

### "Module not found"

The project uses only Python standard library:
```bash
# Verify Python installation
python3 -c "import socket; print('Python is working!')"
```

---

## Example: Complete Setup

```bash
# 1. Open Terminal (Cmd + Space, type terminal)

# 2. Install Homebrew (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 3. Install Python
brew install python3

# 4. Navigate to project
cd ~/Downloads/Thiranex\ task\ 2

# 5. Run scanner
python3 main.py

# 6. Try first scan
# Enter: localhost
# Select: 1 (Quick scan)
```

---

## Helpful Terminal Commands

```bash
# Show current directory
pwd

# List files
ls

# List files with details
ls -la

# Navigate to home directory
cd ~

# Go back one folder
cd ..

# Go to specific folder
cd /path/to/folder

# Create a new folder
mkdir foldername

# Remove a file
rm filename

# Show file contents
cat filename

# Clear terminal
clear

# Stop running program
Ctrl + C
```

---

## Using Non-Standard Port Numbers

If scanning ports below 1024 fails:

```bash
# Run with administrator privileges
sudo python3 main.py

# Then use options 2-4 for port selection
```

---

## M1/M2 Mac Issues

If you have an Apple Silicon Mac (M1, M2, M3):

```bash
# Install Homebrew for Apple Silicon
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Homebrew will auto-detect M1/M2
# Install Python3
brew install python3

# Should work normally
python3 main.py
```

---

## Advanced: Using Virtual Environment (Optional)

For a clean setup:

```bash
# Navigate to project folder
cd ~/Downloads/Thiranex\ task\ 2

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Now run scanner
python3 main.py

# Deactivate when done
deactivate
```

---

## ✅ Success Checklist

- [ ] Python 3.7+ installed (`python3 --version` works)
- [ ] Can navigate to project folder using `cd`
- [ ] Can see main.py in folder (`ls` command)
- [ ] `python3 main.py` starts without errors
- [ ] Can enter target and run scan

---

## Next Steps

1. Scan localhost (safe for learning)
2. Review generated report
3. Read README.md for full documentation
4. Scan your website/server (with permission)
5. Follow security recommendations

---

**You're all set! Ready to run your first vulnerability scan! 🛡️**

For more help, see: README.md and QUICK_START.md
