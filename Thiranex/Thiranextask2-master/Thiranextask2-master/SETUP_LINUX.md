# SETUP GUIDE - Linux Installation

## 🐧 Setting Up on Linux

This guide walks you through installing Python and running the Vulnerability Scanner on Linux (Ubuntu, Debian, Fedora, etc.).

---

## Step 1: Check if Python is Installed

Open Terminal and type:
```bash
python3 --version
```

You should see: `Python 3.x.x` or similar

If Python is installed, skip to Step 3.

---

## Step 2: Install Python

### For Ubuntu/Debian-based Systems

```bash
# Update package list
sudo apt update

# Install Python3 and pip
sudo apt install python3 python3-pip

# Verify installation
python3 --version
```

### For Fedora/RHEL-based Systems

```bash
# Install Python3
sudo dnf install python3 python3-pip

# Verify installation
python3 --version
```

### For Arch Linux

```bash
# Install Python3
sudo pacman -S python

# Verify installation
python3 --version
```

---

## Step 3: Navigate to Project Folder

In Terminal, type:
```bash
cd /path/to/Thiranex\ task\ 2
```

Or if in Downloads:
```bash
cd ~/Downloads/Thiranex\ task\ 2
```

### Finding Your Path

If unsure of the path:
```bash
# Current directory
pwd

# List files in current folder
ls

# List all directories to find the project
find ~ -name "Thiranex*" -type d

# Navigate to found directory
cd /path/to/found/Thiranex\ task\ 2
```

---

## Step 4: Run the Scanner

In Terminal, type:
```bash
python3 main.py
```

---

## Troubleshooting

### "Python3 not found"

```bash
# Ubuntu/Debian
sudo apt install python3

# Fedora/RHEL
sudo dnf install python3

# Arch
sudo pacman -S python
```

### "Permission denied"

For ports below 1024, you need administrator privileges:
```bash
sudo python3 main.py
```

You'll be prompted for your sudo password.

### Scanning specific ports without sudo

```python
# In the custom port range, use ports above 1024
# Example: 1024-65535 instead of 1-1024
```

---

## Useful Linux Terminal Commands

```bash
# Show current directory
pwd

# List files
ls

# List with details
ls -la

# Change directory
cd /path

# Go back one folder
cd ..

# Go to home directory
cd ~

# Create directory
mkdir foldername

# Remove file
rm filename

# Show file content
cat filename

# Edit file
nano filename

# Clear terminal
clear

# Show date/time
date

# Show disk space
df -h

# Show system info
uname -a

# Stop running program
Ctrl + C
```

---

## Example: Complete Setup (Ubuntu)

```bash
# 1. Open Terminal (Ctrl + Alt + T)

# 2. Update package manager
sudo apt update

# 3. Install Python3
sudo apt install python3

# 4. Navigate to project
cd ~/Downloads/Thiranex\ task\ 2

# 5. Run scanner
python3 main.py

# 6. Enter: localhost
# Select: 1
```

---

## Running with Privileges

For standard port scanning (ports 1-1024):

```bash
# Method 1: With sudo
sudo python3 main.py

# Method 2: Scan privileged ports without full sudo
# Use custom port range with ports 1024+
python3 main.py
# Select option 4 (custom)
# Enter: 1024-65535
```

---

## Advanced: Using Virtual Environment (Recommended)

Create an isolated Python environment:

```bash
# Navigate to project folder
cd ~/Downloads/Thiranex\ task\ 2

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) in your terminal

# Run scanner
python3 main.py

# Deactivate when done
deactivate
```

---

## Running in Background

If you want to run and save output:

```bash
# Save output to file
python3 main.py > scan_output.txt 2>&1 &

# Check output later
cat scan_output.txt

# Or run in background with nohup
nohup python3 main.py &
```

---

## Setting Executable Permissions

Make the script executable:

```bash
# Add execute permission
chmod +x main.py

# Run directly
./main.py

# Note: First line in main.py should be:
# #!/usr/bin/env python3
```

---

## Creating an Alias (Optional)

For quick access:

```bash
# Add to ~/.bashrc
echo "alias vulnscan='python3 ~/Downloads/Thiranex\ task\ 2/main.py'" >> ~/.bashrc

# Reload bashrc
source ~/.bashrc

# Now you can run from anywhere
vulnscan
```

---

## Docker Setup (Advanced)

Run the scanner in a Docker container:

```bash
# Create Dockerfile in project directory
cat > Dockerfile << 'EOF'
FROM python:3.10-slim
WORKDIR /app
COPY main.py .
CMD ["python3", "main.py"]
EOF

# Build image
docker build -t vulnscan .

# Run container
docker run -it vulnscan
```

---

## ✅ Success Checklist

- [ ] Python 3.7+ installed (`python3 --version` works)
- [ ] Can navigate to project folder
- [ ] Can see main.py in folder (`ls main.py`)
- [ ] `python3 main.py` starts without errors
- [ ] Can enter target and run scan

---

## Firewall Notes

If behind a firewall:

```bash
# Check if port is accessible
nc -zv target.com port

# Example
nc -zv localhost 80

# Or use Python directly
python3 -c "import socket; s=socket.socket(); s.settimeout(2); print('Open' if s.connect_ex(('localhost', 80)) == 0 else 'Closed')"
```

---

## System-wide Installation (Optional)

To run from anywhere:

```bash
# Copy project to /opt
sudo cp -r ~/Downloads/Thiranex\ task\ 2 /opt/

# Create symlink
sudo ln -s /opt/Thiranex\ task\ 2/main.py /usr/local/bin/vulnscan

# Now run from anywhere
vulnscan
```

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
