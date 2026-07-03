"""
Secure Login System Web App
A beginner-friendly Flask application with user authentication,
password hashing, and session management.
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import re
import os
from datetime import datetime

app = Flask(__name__)

# Secret key for session management - Change this in production!
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['SESSION_TYPE'] = 'filesystem'

# Database configuration
DATABASE = 'database.db'


def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Uses isolation_level=None for automatic commits and Row factory for dict-like rows.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Initializes the database with required tables.
    Creates users table if it doesn't exist.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table with proper schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()


def validate_username(username):
    """
    Validates username format and length.
    Returns tuple (is_valid, error_message)
    """
    if not username or len(username) < 3:
        return False, "Username must be at least 3 characters long."
    if len(username) > 20:
        return False, "Username must not exceed 20 characters."
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores."
    return True, ""


def validate_email(email):
    """
    Validates email format using regex.
    Returns tuple (is_valid, error_message)
    """
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return False, "Please enter a valid email address."
    return True, ""


def validate_password(password):
    """
    Validates password strength.
    Password must be at least 6 characters with at least one number and one uppercase letter.
    Returns tuple (is_valid, error_message)
    """
    if not password or len(password) < 6:
        return False, "Password must be at least 6 characters long."
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."
    return True, ""


@app.route('/')
def index():
    """Home page - redirects to dashboard if logged in, otherwise to login."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    User registration page.
    GET: Shows registration form
    POST: Processes registration with validation and stores hashed password
    """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validate input
        is_valid_username, username_error = validate_username(username)
        if not is_valid_username:
            flash(username_error, 'error')
            return redirect(url_for('register'))
        
        is_valid_email, email_error = validate_email(email)
        if not is_valid_email:
            flash(email_error, 'error')
            return redirect(url_for('register'))
        
        is_valid_password, password_error = validate_password(password)
        if not is_valid_password:
            flash(password_error, 'error')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash("Passwords do not match.", 'error')
            return redirect(url_for('register'))
        
        # Check if user already exists (using parameterized query to prevent SQL injection)
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
            if cursor.fetchone():
                flash("Username already exists. Please choose a different username.", 'error')
                conn.close()
                return redirect(url_for('register'))
            
            cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
            if cursor.fetchone():
                flash("Email already registered. Please use a different email.", 'error')
                conn.close()
                return redirect(url_for('register'))
            
            # Hash password using bcrypt (generates salt automatically)
            password_hash = generate_password_hash(password)
            
            # Insert new user with parameterized query (prevents SQL injection)
            cursor.execute(
                'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                (username, email, password_hash)
            )
            conn.commit()
            conn.close()
            
            flash("Registration successful! You can now log in.", 'success')
            return redirect(url_for('login'))
            
        except sqlite3.IntegrityError as e:
            flash(f"Registration failed: {str(e)}", 'error')
            return redirect(url_for('register'))
        except Exception as e:
            flash(f"An unexpected error occurred: {str(e)}", 'error')
            return redirect(url_for('register'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    User login page.
    GET: Shows login form
    POST: Authenticates user and creates session
    """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        # Validate input
        if not username or not password:
            flash("Please enter both username and password.", 'error')
            return redirect(url_for('login'))
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Get user by username (parameterized query prevents SQL injection)
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            conn.close()
            
            # Check if user exists and password is correct
            if user and check_password_hash(user['password_hash'], password):
                # Create session
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['email'] = user['email']
                
                # Update last login time
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(
                    'UPDATE users SET last_login = ? WHERE id = ?',
                    (datetime.now(), user['id'])
                )
                conn.commit()
                conn.close()
                
                flash(f"Welcome back, {user['username']}!", 'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid username or password.", 'error')
                return redirect(url_for('login'))
                
        except Exception as e:
            flash(f"An error occurred during login: {str(e)}", 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    """
    Protected dashboard page - only accessible to logged-in users.
    Shows user information and provides logout option.
    """
    if 'user_id' not in session:
        flash("Please log in first.", 'error')
        return redirect(url_for('login'))
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
        user = cursor.fetchone()
        conn.close()
        
        if not user:
            flash("User not found.", 'error')
            return redirect(url_for('logout'))
        
        return render_template('dashboard.html', user=user)
        
    except Exception as e:
        flash(f"Error loading dashboard: {str(e)}", 'error')
        return redirect(url_for('logout'))


@app.route('/logout')
def logout():
    """
    Logout functionality - clears session and redirects to login page.
    """
    username = session.get('username', 'User')
    session.clear()
    flash(f"Goodbye, {username}! You have been logged out successfully.", 'success')
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors gracefully."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors gracefully."""
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Run Flask app in development mode
    # Change debug=False in production!
    app.run(debug=True, host='localhost', port=5000)
