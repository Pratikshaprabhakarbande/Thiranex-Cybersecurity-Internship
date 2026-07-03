# Installation and Setup Verification Script
# This script helps verify Python, Tkinter, and project setup

import sys
import subprocess
import os

def print_header(text):
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)

def print_status(status, message):
    symbol = "✅" if status else "❌"
    print(f"{symbol} {message}")

def check_python_version():
    print_header("PYTHON VERSION CHECK")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 6:
        print_status(True, f"Python {version.major}.{version.minor} is compatible")
        return True
    else:
        print_status(False, f"Python {version.major}.{version.minor} is too old (need 3.6+)")
        return False

def check_tkinter():
    print_header("TKINTER CHECK")
    try:
        import tkinter
        print_status(True, "Tkinter is installed and available")
        print(f"  Location: {tkinter.__file__}")
        return True
    except ImportError as e:
        print_status(False, f"Tkinter not found: {e}")
        print("\n  To install Tkinter:")
        if sys.platform == "win32":
            print("    - Reinstall Python and check 'tcl/tk and IDLE'")
        elif sys.platform == "darwin":
            print("    - brew install python-tk")
        else:
            print("    - sudo apt install python3-tk")
        return False

def check_standard_modules():
    print_header("STANDARD LIBRARY MODULES CHECK")
    modules = ['re', 'secrets', 'string', 'hashlib', 'sqlite3', 'datetime', 'os']
    all_good = True
    
    for module in modules:
        try:
            __import__(module)
            print_status(True, f"Module '{module}' available")
        except ImportError:
            print_status(False, f"Module '{module}' not found")
            all_good = False
    
    return all_good

def check_project_files():
    print_header("PROJECT FILES CHECK")
    project_path = os.path.dirname(os.path.abspath(__file__))
    required_files = ['main.py', 'README.md', 'requirements.txt']
    all_found = True
    
    for filename in required_files:
        filepath = os.path.join(project_path, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print_status(True, f"File '{filename}' found ({size} bytes)")
        else:
            print_status(False, f"File '{filename}' not found")
            all_found = False
    
    return all_found

def check_python_syntax():
    print_header("PYTHON SYNTAX CHECK")
    try:
        import py_compile
        import tempfile
        
        main_py_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'main.py')
        
        with tempfile.NamedTemporaryFile(suffix='.pyc', delete=True) as tmp:
            py_compile.compile(main_py_path, cfile=tmp.name, doraise=True)
        
        print_status(True, "main.py has valid Python syntax")
        return True
    except py_compile.PyCompileError as e:
        print_status(False, f"Syntax error in main.py: {e}")
        return False
    except Exception as e:
        print_status(False, f"Error checking syntax: {e}")
        return False

def main():
    print_header("PASSWORD STRENGTH ANALYZER - SETUP VERIFICATION")
    print(f"Python: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    results = {
        "Python Version": check_python_version(),
        "Tkinter": check_tkinter(),
        "Standard Modules": check_standard_modules(),
        "Project Files": check_project_files(),
        "Python Syntax": check_python_syntax(),
    }
    
    print_header("VERIFICATION SUMMARY")
    all_passed = True
    for check_name, result in results.items():
        print_status(result, check_name)
        if not result:
            all_passed = False
    
    print_header("NEXT STEPS")
    if all_passed:
        print("✅ All checks passed! You can now run:")
        print("   python main.py")
    else:
        print("❌ Some checks failed. Please:")
        print("   1. Check error messages above")
        print("   2. Install missing components")
        print("   3. Rerun this script to verify")
    
    print("\n" + "="*70)
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit(main())
