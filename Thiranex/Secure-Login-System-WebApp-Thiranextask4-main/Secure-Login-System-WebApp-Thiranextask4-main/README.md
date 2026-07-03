# 🔐 Secure Login System Web App

A beginner-friendly, professional-grade Flask web application demonstrating secure user authentication with password hashing, SQL injection protection, and session management.

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green)

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Security Features](#security-features)
- [Usage Guide](#usage-guide)
- [File Descriptions](#file-descriptions)
- [Environment Variables](#environment-variables)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Features
- ✅ **User Registration** - Create new accounts with validation
- ✅ **Secure Login** - Password-protected access with session management
- ✅ **Logout** - Safe session termination
- ✅ **Dashboard** - Protected user dashboard with profile information
- ✅ **Professional UI** - Clean, modern, and responsive interface
- ✅ **Flash Messages** - User feedback for success and error scenarios

### Security Features
- 🔒 **Password Hashing** - bcrypt for secure password storage
- 🛡️ **SQL Injection Protection** - Parameterized queries throughout
- 🔐 **Input Validation** - Comprehensive validation on all user inputs
- 📝 **Session Management** - Secure Flask session handling
- ✓ **Error Handling** - Graceful error pages and messages
- 🔄 **CSRF Protection** - Built-in Flask security

### Technical Features
- 💾 **SQLite Database** - Lightweight, file-based database
- 🎨 **Responsive Design** - Mobile-friendly interface
- 📊 **Audit Trail** - User creation and login timestamps
- 🚀 **Production-Ready** - Clean, documented code

## 📁 Project Structure

```
Secure-Login-System-WebApp/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── database.db            # SQLite database (auto-created)
├── README.md              # Project documentation
├── QUICKSTART.md          # Quick start guide
├── templates/             # HTML templates
│   ├── base.html          # Base template with navbar
│   ├── register.html      # Registration page
│   ├── login.html         # Login page
│   ├── dashboard.html     # User dashboard
│   ├── 404.html           # 404 error page
│   └── 500.html           # 500 error page
└── static/                # Static files
    └── style.css          # Application styling
```

## 📦 Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🔧 Installation

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/Pratikshaprabhakarbande/Secure-Login-System-WebApp-Thiranextask4.git
cd Secure-Login-System-WebApp-Thiranextask4
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 🚀 Quick Start

1. **Register** - Click "Register" and create a new account
   - Username: 3-20 characters (letters, numbers, underscores)
   - Email: Valid email address
   - Password: At least 6 characters with uppercase and number

2. **Login** - Use your credentials to log in
   - You'll see your secure dashboard
   - Account info and security highlights are displayed

3. **Dashboard** - View your profile and security information
   - See account creation and last login times
   - Learn about security features
   - Click Logout to end your session

4. **Logout** - Click the logout button to securely end your session

## 🔐 Security Features Explained

### Password Hashing with bcrypt
- Passwords are never stored in plain text
- bcrypt automatically generates and uses salt
- Even database compromises don't expose passwords
- Each password is unique due to salt randomization

### SQL Injection Protection
- All database queries use parameterized queries
- User input is never directly concatenated into SQL
- Example: `cursor.execute('SELECT * FROM users WHERE username = ?', (username,))`

### Input Validation
- **Username**: 3-20 characters, alphanumeric + underscores
- **Email**: RFC-compliant email validation
- **Password**: Minimum 6 characters, requires uppercase and number
- All inputs are sanitized before database operations

### Session Management
- Flask sessions are used for secure authentication
- Sessions timeout for security
- Logout clears all session data
- Change the SECRET_KEY in production!

### Error Handling
- Graceful 404 and 500 error pages
- No sensitive information in error messages
- User-friendly error notifications

## 📖 Usage Guide

### Registering a New Account

1. Navigate to the application homepage
2. Click "Register" in the navigation
3. Fill in the registration form:
   - **Username**: Choose a unique username
   - **Email**: Enter a valid email address
   - **Password**: Create a strong password
   - **Confirm Password**: Re-enter your password
4. Click "Create Account"
5. Success message appears - you can now login

### Logging In

1. Click "Login" in the navigation
2. Enter your credentials:
   - Username or email
   - Password
3. Click "Sign In"
4. You'll be redirected to your dashboard

### Dashboard Access

Once logged in, you can:
- View your profile information
- See account creation date and last login
- Read about security features
- Learn about SQL injection and password protection
- Click "Logout" to exit securely

### Logging Out

1. Click "Logout" button in navbar or dashboard
2. Session is cleared
3. You're redirected to login page

## 📄 File Descriptions

### app.py
Main Flask application file containing:
- Flask app initialization
- Database setup and connection management
- User registration and login endpoints
- Input validation functions
- Password hashing and verification
- Session management
- Error handlers

### requirements.txt
Python dependencies:
- **Flask 2.3.0** - Web framework
- **Flask-Session 0.5.0** - Session management
- **Werkzeug 2.3.0** - WSGI utilities
- **bcrypt 4.0.1** - Password hashing

### templates/base.html
Base HTML template with:
- Navigation bar
- Flash message display
- Footer
- Responsive layout

### templates/register.html
Registration page featuring:
- Registration form
- Input validation hints
- Security information
- Link to login page

### templates/login.html
Login page featuring:
- Login form
- Security information
- Link to registration

### templates/dashboard.html
Protected dashboard featuring:
- User profile card
- Account information
- Security highlights
- Feature showcase
- Logout button

### static/style.css
Professional styling with:
- Modern color scheme
- Responsive grid layouts
- Smooth animations
- Mobile optimization

## 🔑 Environment Variables

### Production Setup

Create a `.env` file (don't commit to git):

```
FLASK_ENV=production
SECRET_KEY=your-very-secure-random-key-here
DEBUG=False
```

**IMPORTANT**: In `app.py`, change these settings for production:

```python
# Change from:
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.run(debug=True)

# To:
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.run(debug=False)
```

## 💾 Database Schema

### Users Table

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
)
```

**Columns:**
- `id`: Unique user identifier
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: bcrypt hashed password (never plain text)
- `created_at`: Account creation timestamp
- `last_login`: Last login timestamp

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📝 License

This project is open source and available under the MIT License.

## 🎓 Learning Resources

This project demonstrates:
- Flask web framework basics
- Database design and management
- Password security best practices
- Input validation and sanitization
- SQL injection prevention
- Session management
- HTML/CSS responsive design
- User authentication flows

## 🆘 Troubleshooting

### Port 5000 Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

### Database Locked Error
Delete `database.db` and restart - it will be recreated

### Module Not Found Error
Make sure virtual environment is activated and requirements are installed:
```bash
pip install -r requirements.txt
```

## 📞 Support

For issues and questions:
1. Check the Troubleshooting section
2. Review code comments
3. Open an issue on GitHub

## 🎉 Credits

Created as a beginner-friendly secure login system demonstration using Flask, SQLite, and bcrypt.

---

**Happy Coding! 🚀**
