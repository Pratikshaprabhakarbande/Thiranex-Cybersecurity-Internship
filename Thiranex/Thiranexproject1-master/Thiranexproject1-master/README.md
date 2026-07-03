# 🔐 Password Strength Analyzer

A beginner-friendly Python GUI application for analyzing password strength and providing security suggestions. Built with Tkinter, featuring password generation, hashing with SQLite database, and real-time analysis.

## 📋 Project Overview

The Password Strength Analyzer is an educational tool that demonstrates best practices for password security. It helps users create stronger passwords by:

- **Real-time Analysis**: Instantly analyzes password strength as you type
- **Detailed Feedback**: Provides specific suggestions for improvement
- **Secure Generation**: Creates cryptographically secure random passwords
- **Reuse Prevention**: Uses SQLite to store hashed passwords and prevent reuse
- **Visual Indicators**: Color-coded strength bars (Red/Orange/Green)

## ✨ Features

### 1. Password Analysis
- ✅ **Length Check**: Evaluates password length (6, 8, 12+ character thresholds)
- ✅ **Character Types**: Checks for uppercase, lowercase, numbers, and special characters
- ✅ **Common Password Detection**: Identifies commonly used weak passwords
- ✅ **Pattern Detection**: Detects keyboard patterns and repeating characters
- ✅ **Scoring System**: 0-100 point scale for strength rating

### 2. Strength Categories
- 🔴 **Weak** (0-20): Less than 3 character types or common password
- 🟠 **Medium** (20-50): Good length but missing some character types
- 🟢 **Strong** (50+): Excellent length with all character types

### 3. Password Generator
- 🔑 Generates 16-character secure passwords
- 🔀 Includes uppercase, lowercase, numbers, and special characters
- 🛡️ Uses Python's `secrets` module for cryptographic randomness

### 4. Security Features
- 🔐 Passwords hashed with SHA-256 before storage
- 💾 SQLite database prevents reuse of old passwords
- 🚫 No plain text passwords stored anywhere
- 🔒 Database automatically created and managed

### 5. User Interface
- 💻 Modern, intuitive Tkinter GUI
- 👁️ Show/Hide password toggle
- 🎨 Color-coded strength indicator
- 📊 Real-time score display (0-100)
- 💬 Detailed suggestions and feedback

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Tkinter (included with Python on Windows/Mac, may need separate installation on Linux)

### Installation Steps

1. **Clone or Download Project**
   ```bash
   # Clone from repository or download the files
   git clone <repository-url>
   cd password-analyzer
   ```

2. **Check Python Installation**
   ```bash
   python --version
   # Output should be Python 3.6 or higher
   ```

3. **Install Tkinter (if needed)**
   
   **Windows:**
   - Usually included with Python installation
   - If missing, reinstall Python and check "tcl/tk and IDLE"
   
   **Mac:**
   ```bash
   brew install python-tk
   ```
   
   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt-get install python3-tk
   ```
   
   **Linux (Fedora/RHEL):**
   ```bash
   sudo dnf install python3-tkinter
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

## 📖 Usage Guide

### Basic Usage

1. **Launch Application**: Run `python main.py`
2. **Enter Password**: Type or paste a password in the input field
3. **View Results**: Strength and feedback update in real-time
4. **Read Suggestions**: Check the feedback box for specific improvements
5. **Generate New**: Click "Generate Secure Password" for a strong suggestion

### Features Explained

#### Password Entry
- Type your password in the text field
- Analysis happens automatically as you type
- Toggle "Show" checkbox to display/hide password characters

#### Strength Indicator
- **Visual Bar**: Color-coded progress bar showing strength level
- **Percentage Score**: Numerical score from 0-100
- **Status Text**: "Weak", "Medium", or "Strong" label

#### Suggestions
- **Red indicators (❌)**: Required improvements
- **Yellow warnings (⚠️)**: Optional but recommended improvements
- **Green checkmarks (✓)**: Positive aspects of password

#### Generate Password
- Click "🔑 Generate Secure Password" to create a strong password
- Generated password is 16 characters with mixed character types
- Automatically loaded into the password field for analysis

#### Save Password
- Click "💾 Save Password (to history)" to store hashed password
- Prevents reuse of old passwords
- Password is stored as SHA-256 hash (not plain text)
- Database file created as `passwords.db`

#### Clear
- Click "🗑️ Clear" to reset all fields
- Clears password entry and feedback

## 🔒 Security Concepts Demonstrated

### 1. Password Hashing (SHA-256)
```python
# Passwords are hashed before storage
hashed = hashlib.sha256(password.encode()).hexdigest()
```
- One-way encryption (cannot be reversed)
- Same password always produces same hash
- Used to check for password reuse without storing plain text

### 2. Cryptographic Randomness
```python
# Uses secrets module for secure random password generation
password_list.append(secrets.choice(special))
```
- Better than `random` module for security
- Suitable for cryptographic purposes
- Provides unpredictable randomness

### 3. SQLite Database
- Stores hashed passwords locally
- Prevents password reuse detection
- Example schema:
  ```sql
  CREATE TABLE password_history (
      id INTEGER PRIMARY KEY,
      password_hash TEXT UNIQUE NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
  ```

## 📁 Project Structure

```
password-analyzer/
│
├── main.py                 # Main application file with all functionality
├── requirements.txt        # Project dependencies (standard library)
├── README.md              # This file
└── passwords.db           # SQLite database (created on first run)
```

## 🔧 Code Structure Explained

### Main Classes

#### 1. **PasswordDatabase**
```python
class PasswordDatabase:
    """Manages password hashes in SQLite database"""
    - create_table()          # Create database schema
    - hash_password()         # Hash with SHA-256
    - add_password_to_history()  # Store hashed password
    - is_password_reused()    # Check if password used before
```

#### 2. **PasswordAnalyzer**
```python
class PasswordAnalyzer:
    """Core password strength analysis logic"""
    - analyze()               # Main analysis method
    - _check_length()         # Length validation
    - _check_uppercase()      # Uppercase check
    - _check_lowercase()      # Lowercase check
    - _check_numbers()        # Number check
    - _check_special_chars()  # Special character check
    - _check_common_password()   # Common password detection
    - _check_uniqueness()     # Pattern detection
    - generate_password()     # Generate secure password
```

#### 3. **PasswordStrengthAnalyzerApp**
```python
class PasswordStrengthAnalyzerApp:
    """Main GUI application"""
    - setup_gui()            # Create all GUI elements
    - on_password_change()   # Real-time analysis trigger
    - toggle_password_visibility()  # Show/hide password
    - generate_password()    # Generate new password
    - clear_all()           # Reset all fields
    - save_password()       # Save to history
```

## 💡 Scoring System

| Criterion | Points | Details |
|-----------|--------|---------|
| Length < 6 | 0 | Too short |
| Length 6-8 | 10 | Acceptable minimum |
| Length 8-12 | 20 | Good length |
| Length 12+ | 30 | Excellent |
| Uppercase | 10 | A-Z present |
| Lowercase | 10 | a-z present |
| Numbers | 10 | 0-9 present |
| Special Chars | 10 | !@#$%^&* present |
| Common Password | -30 | Penalty if weak |
| **Maximum** | **100** | - |

## 🎓 Learning Outcomes

By using this application, you'll learn:

1. **Password Security**: Best practices for strong passwords
2. **Regular Expressions**: Pattern matching for validation
3. **Database Management**: SQLite basics for data persistence
4. **GUI Development**: Tkinter for desktop applications
5. **Cryptography**: Hashing and secure randomness
6. **Object-Oriented Programming**: Class design and architecture
7. **Error Handling**: Try-catch blocks and validation

## 🐛 Troubleshooting

### Issue: "No module named 'tkinter'"
**Solution**: Install tkinter for your OS (see Installation section)

### Issue: Database errors
**Solution**: Delete `passwords.db` file and restart application

### Issue: Password entry not showing text
**Solution**: Uncheck "Show" checkbox to hide password safely

### Issue: Application won't start
**Solution**: Verify Python version is 3.6+:
```bash
python --version
```

## 🔐 Best Practices for Strong Passwords

After analyzing passwords with this tool, remember:

✅ **DO:**
- Use at least 12 characters
- Mix uppercase and lowercase letters
- Include numbers and special characters
- Use unique passwords for different accounts
- Use a password manager for storage

❌ **DON'T:**
- Use personal information (names, birthdates)
- Reuse passwords across sites
- Use keyboard patterns (qwerty, asdfgh)
- Share passwords over unencrypted channels
- Store passwords in plain text

## 📝 Code Comments

The code includes detailed comments explaining:
- Function purposes and parameters
- Security implementation details
- GUI component setup
- Database operations
- Analysis logic

## 🛠️ Customization

### Change Password Length for Generation
In `PasswordAnalyzer.generate_password()`:
```python
def generate_password(self, length=16, use_special=True):  # Change 16 to desired length
```

### Add More Common Passwords
In `PasswordAnalyzer` class:
```python
COMMON_PASSWORDS = {
    'password', '123456',  # Add more here
}
```

### Adjust Color Scheme
In `PasswordStrengthAnalyzerApp` GUI setup:
```python
strength_label = tk.Label(..., bg="white", fg="#333333")  # Change hex colors
```

## 📊 Example Outputs

### Example 1: Weak Password
```
Password: abc123
Strength: Weak (15/100)
Feedback:
❌ Password too short (6 chars). Use at least 8 characters.
✓ Contains lowercase letters (a-z).
✓ Contains numbers (0-9).
❌ Add uppercase letters (A-Z) for better security.
❌ Add special characters (!@#$%^&*) for maximum security.
```

### Example 2: Strong Password
```
Password: MyP@ssw0rd2024!Secure
Strength: Strong (95/100)
Feedback:
✓ Excellent length (22 chars)!
✓ Contains uppercase letters (A-Z).
✓ Contains lowercase letters (a-z).
✓ Contains numbers (0-9).
✓ Contains special characters (!@#$%^&...).
```

## 📚 Resources

- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [OWASP Password Guidelines](https://owasp.org/www-community/authentication/password-policy)
- [Hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [Python Secrets Module](https://docs.python.org/3/library/secrets.html)
- [SQLite3 Tutorial](https://docs.python.org/3/library/sqlite3.html)

## 📄 License

This project is open-source and available for educational purposes.

## 👨‍💻 Contributing

Feel free to fork and improve this project! Some ideas:
- Add password strength meter animations
- Implement multi-language support
- Add password breach checking (API integration)
- Create web version with Flask
- Add export of password history (encrypted)

## ❓ FAQ

**Q: Is my password stored?**
A: No! Only the SHA-256 hash is stored, never the plain password.

**Q: Can I recover the hash to get the password back?**
A: No, SHA-256 is one-way encryption. It's intentionally irreversible.

**Q: Does this work offline?**
A: Yes! All features work without internet connection.

**Q: Is this secure enough for production?**
A: This is an educational tool. For production, use proper password managers like LastPass or 1Password.

**Q: Can I use generated passwords?**
A: Yes! The generator creates cryptographically secure passwords suitable for real use.

---

**Made with ❤️ for learning Python GUI and Security Concepts**

Happy password analyzing! 🔐
