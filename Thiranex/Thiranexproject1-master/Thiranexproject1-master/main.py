"""
Password Strength Analyzer - Main Application
A beginner-friendly GUI application to analyze password strength and provide suggestions.
Uses Tkinter for GUI and includes password generation and hashing with SQLite storage.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import re
import secrets
import string
import hashlib
import sqlite3
from datetime import datetime
import os

# ============================================================================
# DATABASE SETUP - SQLite for storing hashed passwords
# ============================================================================

class PasswordDatabase:
    """Manages password hashes in SQLite database to prevent reuse."""
    
    def __init__(self, db_name="passwords.db"):
        """Initialize database connection and create table if needed."""
        self.db_name = db_name
        self.create_table()
    
    def create_table(self):
        """Create password history table if it doesn't exist."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS password_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    password_hash TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def hash_password(self, password):
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def add_password_to_history(self, password):
        """Add hashed password to history."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            hashed = self.hash_password(password)
            cursor.execute('INSERT INTO password_history (password_hash) VALUES (?)', (hashed,))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False  # Password already used
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
    
    def is_password_reused(self, password):
        """Check if password has been used before."""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            hashed = self.hash_password(password)
            cursor.execute('SELECT id FROM password_history WHERE password_hash = ?', (hashed,))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False


# ============================================================================
# PASSWORD ANALYZER ENGINE
# ============================================================================

class PasswordAnalyzer:
    """Core password strength analysis logic."""
    
    # Common weak passwords to check against
    COMMON_PASSWORDS = {
        'password', '123456', '123456789', 'password123', 'admin', 'letmein',
        'welcome', 'monkey', '1234567', 'dragon', 'master', 'qwerty',
        'abc123', '123123', '111111', 'iloveyou', 'sunshine', 'princess',
        'login', 'soccer', 'starwars', 'trustno1', 'batman', 'shadow'
    }
    
    def __init__(self):
        """Initialize the analyzer with scoring thresholds."""
        self.db = PasswordDatabase()
        self.score = 0
        self.feedback = []
    
    def analyze(self, password):
        """
        Perform complete password analysis and return results.
        Returns dictionary with score, strength, and feedback.
        """
        # Reset for new analysis
        self.score = 0
        self.feedback = []
        
        if not password:
            return self._get_result()
        
        # Check if password has been used before (optional security feature)
        if self.db.is_password_reused(password):
            self.feedback.append("⚠️ Warning: This password has been used before!")
        
        # Length check (0-30 points)
        self._check_length(password)
        
        # Character type checks (10 points each)
        self._check_uppercase(password)
        self._check_lowercase(password)
        self._check_numbers(password)
        self._check_special_chars(password)
        
        # Common password check (penalty)
        self._check_common_password(password)
        
        # Uniqueness check
        self._check_uniqueness(password)
        
        return self._get_result()
    
    def _check_length(self, password):
        """Analyze password length."""
        length = len(password)
        if length < 6:
            self.feedback.append(f"❌ Password too short ({length} chars). Use at least 8 characters.")
        elif length < 8:
            self.score += 10
            self.feedback.append(f"⚠️ Length acceptable ({length} chars), but 8+ is recommended.")
        elif length < 12:
            self.score += 20
            self.feedback.append(f"✓ Good length ({length} chars).")
        else:
            self.score += 30
            self.feedback.append(f"✓ Excellent length ({length} chars)!")
    
    def _check_uppercase(self, password):
        """Check for uppercase letters."""
        if re.search(r'[A-Z]', password):
            self.score += 10
            self.feedback.append("✓ Contains uppercase letters (A-Z).")
        else:
            self.feedback.append("❌ Add uppercase letters (A-Z) for better security.")
    
    def _check_lowercase(self, password):
        """Check for lowercase letters."""
        if re.search(r'[a-z]', password):
            self.score += 10
            self.feedback.append("✓ Contains lowercase letters (a-z).")
        else:
            self.feedback.append("❌ Add lowercase letters (a-z) for better security.")
    
    def _check_numbers(self, password):
        """Check for numeric characters."""
        if re.search(r'[0-9]', password):
            self.score += 10
            self.feedback.append("✓ Contains numbers (0-9).")
        else:
            self.feedback.append("❌ Add numbers (0-9) to strengthen your password.")
    
    def _check_special_chars(self, password):
        """Check for special characters."""
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
            self.score += 10
            self.feedback.append("✓ Contains special characters (!@#$%^&*...).")
        else:
            self.feedback.append("❌ Add special characters (!@#$%^&*) for maximum security.")
    
    def _check_common_password(self, password):
        """Check if password is in common passwords list."""
        if password.lower() in self.COMMON_PASSWORDS:
            self.score = max(0, self.score - 30)
            self.feedback.insert(0, "⛔ This is a very common password! DO NOT USE.")
        elif password.lower() in [p[:3] for p in self.COMMON_PASSWORDS]:
            # Partial match with common passwords
            self.feedback.append("⚠️ Password contains a common pattern.")
    
    def _check_uniqueness(self, password):
        """Check password uniqueness (repeating characters)."""
        if re.search(r'(.)\1{2,}', password):
            self.feedback.append("⚠️ Contains repeating characters (aaa, 111, etc.). Vary your characters.")
        
        # Check if it's a keyboard pattern
        if self._is_keyboard_pattern(password):
            self.feedback.append("⚠️ Avoid keyboard patterns (qwerty, asdfgh, etc.).")
    
    def _is_keyboard_pattern(self, password):
        """Detect common keyboard patterns."""
        patterns = ['qwerty', 'asdfgh', 'zxcvbn', 'qazwsx', 'qweasd', '12345']
        password_lower = password.lower()
        for pattern in patterns:
            if pattern in password_lower or pattern[::-1] in password_lower:
                return True
        return False
    
    def _get_result(self):
        """Determine strength level and return complete result."""
        # Normalize score to 0-100
        score = min(100, max(0, self.score))
        
        # Determine strength level
        if score < 20:
            strength = "Weak"
            color = "#FF6B6B"  # Red
        elif score < 50:
            strength = "Medium"
            color = "#FFA500"  # Orange
        else:
            strength = "Strong"
            color = "#51CF66"  # Green
        
        return {
            'score': score,
            'strength': strength,
            'color': color,
            'feedback': self.feedback
        }
    
    def generate_password(self, length=16, use_special=True):
        """
        Generate a secure random password.
        Uses secrets module for cryptographically secure randomness.
        """
        # Define character sets
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        special = "!@#$%^&*()_+-=[]{}:;<>,.?/"
        
        # Build character pool
        char_pool = uppercase + lowercase + digits
        if use_special:
            char_pool += special
        
        # Generate password with at least one from each category
        password_list = [
            secrets.choice(uppercase),
            secrets.choice(lowercase),
            secrets.choice(digits),
        ]
        
        if use_special:
            password_list.append(secrets.choice(special))
        
        # Fill remaining length with random characters
        remaining_length = length - len(password_list)
        password_list.extend(secrets.choice(char_pool) for _ in range(remaining_length))
        
        # Shuffle to avoid predictable patterns
        secrets.SystemRandom().shuffle(password_list)
        return ''.join(password_list)


# ============================================================================
# TKINTER GUI APPLICATION
# ============================================================================

class PasswordStrengthAnalyzerApp:
    """Main GUI application for Password Strength Analyzer."""
    
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Password Strength Analyzer")
        self.root.geometry("650x800")
        self.root.resizable(False, False)
        
        # Set background color
        self.root.configure(bg="#F5F5F5")
        
        # Initialize analyzer
        self.analyzer = PasswordAnalyzer()
        
        # Setup GUI
        self.setup_gui()
    
    def setup_gui(self):
        """Create and arrange all GUI elements."""
        # Title
        title_frame = tk.Frame(self.root, bg="#F5F5F5")
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🔐 Password Strength Analyzer",
            font=("Helvetica", 24, "bold"),
            bg="#F5F5F5",
            fg="#333333"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Check your password strength and get improvement suggestions",
            font=("Helvetica", 10),
            bg="#F5F5F5",
            fg="#666666"
        )
        subtitle_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg="white", relief=tk.RAISED, bd=1)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Password input section
        input_frame = tk.Frame(main_frame, bg="white")
        input_frame.pack(padx=20, pady=20, fill=tk.X)
        
        input_label = tk.Label(
            input_frame,
            text="Enter Password:",
            font=("Helvetica", 12, "bold"),
            bg="white",
            fg="#333333"
        )
        input_label.pack(anchor=tk.W)
        
        # Password entry with show/hide toggle
        entry_container = tk.Frame(input_frame, bg="white")
        entry_container.pack(fill=tk.X, pady=10)
        
        self.password_entry = tk.Entry(
            entry_container,
            font=("Helvetica", 12),
            show="*",
            relief=tk.FLAT,
            bd=2,
            bg="#F0F0F0"
        )
        self.password_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        self.password_entry.bind('<KeyRelease>', self.on_password_change)
        
        self.show_password_var = tk.BooleanVar()
        self.show_button = tk.Checkbutton(
            entry_container,
            text="Show",
            font=("Helvetica", 10),
            bg="white",
            fg="#333333",
            variable=self.show_password_var,
            command=self.toggle_password_visibility
        )
        self.show_button.pack(side=tk.LEFT)
        
        # Strength indicator section
        strength_frame = tk.Frame(main_frame, bg="white")
        strength_frame.pack(padx=20, pady=10, fill=tk.X)
        
        strength_label = tk.Label(
            strength_frame,
            text="Strength:",
            font=("Helvetica", 11, "bold"),
            bg="white",
            fg="#333333"
        )
        strength_label.pack(anchor=tk.W)
        
        # Strength bar
        bar_frame = tk.Frame(strength_frame, bg="#E0E0E0", height=20, relief=tk.FLAT, bd=1)
        bar_frame.pack(fill=tk.X, pady=10)
        bar_frame.pack_propagate(False)
        
        self.strength_bar = tk.Label(
            bar_frame,
            text="",
            bg="#CCCCCC",
            fg="white",
            font=("Helvetica", 10, "bold")
        )
        self.strength_bar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Strength text and score
        info_frame = tk.Frame(strength_frame, bg="white")
        info_frame.pack(fill=tk.X)
        
        self.strength_text = tk.Label(
            info_frame,
            text="No password entered",
            font=("Helvetica", 11, "bold"),
            bg="white",
            fg="#999999"
        )
        self.strength_text.pack(side=tk.LEFT)
        
        self.score_label = tk.Label(
            info_frame,
            text="(0/100)",
            font=("Helvetica", 11),
            bg="white",
            fg="#666666"
        )
        self.score_label.pack(side=tk.RIGHT)
        
        # Feedback section
        feedback_label = tk.Label(
            main_frame,
            text="Suggestions & Feedback:",
            font=("Helvetica", 11, "bold"),
            bg="white",
            fg="#333333"
        )
        feedback_label.pack(padx=20, pady=(20, 10), anchor=tk.W)
        
        # Feedback text box (read-only)
        feedback_scroll = tk.Scrollbar(main_frame)
        feedback_scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 20))
        
        self.feedback_text = tk.Text(
            main_frame,
            font=("Courier", 10),
            bg="#F9F9F9",
            fg="#333333",
            height=10,
            relief=tk.FLAT,
            bd=2,
            yscrollcommand=feedback_scroll.set,
            wrap=tk.WORD
        )
        self.feedback_text.pack(padx=20, pady=(0, 20), fill=tk.BOTH, expand=True)
        self.feedback_text.configure(state=tk.DISABLED)
        feedback_scroll.config(command=self.feedback_text.yview)
        
        # Button section
        button_frame = tk.Frame(main_frame, bg="white")
        button_frame.pack(padx=20, pady=20, fill=tk.X)
        
        # Generate password button
        generate_button = tk.Button(
            button_frame,
            text="🔑 Generate Secure Password",
            font=("Helvetica", 11, "bold"),
            bg="#2196F3",
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=10,
            pady=10,
            command=self.generate_password
        )
        generate_button.pack(side=tk.LEFT, padx=5)
        
        # Reset/Clear button
        clear_button = tk.Button(
            button_frame,
            text="🗑️ Clear",
            font=("Helvetica", 11, "bold"),
            bg="#FF9800",
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=10,
            pady=10,
            command=self.clear_all
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Save password button (to history)
        save_button = tk.Button(
            button_frame,
            text="💾 Save Password (to history)",
            font=("Helvetica", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=10,
            pady=10,
            command=self.save_password
        )
        save_button.pack(side=tk.LEFT, padx=5)
    
    def on_password_change(self, event=None):
        """Analyze password when user types."""
        password = self.password_entry.get()
        
        if not password:
            # Reset display
            self.strength_text.config(text="No password entered", fg="#999999")
            self.score_label.config(text="(0/100)")
            self.strength_bar.config(text="", bg="#CCCCCC")
            self.feedback_text.config(state=tk.NORMAL)
            self.feedback_text.delete(1.0, tk.END)
            self.feedback_text.config(state=tk.DISABLED)
            return
        
        # Analyze password
        result = self.analyzer.analyze(password)
        
        # Update strength display
        strength = result['strength']
        score = result['score']
        color = result['color']
        
        self.strength_text.config(text=strength, fg=color)
        self.score_label.config(text=f"({score}/100)")
        
        # Update strength bar
        bar_width = int((score / 100) * 600)  # Approximate width
        self.strength_bar.config(
            text=f"{score}%",
            bg=color,
            width=max(1, bar_width // 8)  # Approximate character width
        )
        
        # Update feedback
        self.feedback_text.config(state=tk.NORMAL)
        self.feedback_text.delete(1.0, tk.END)
        
        if result['feedback']:
            feedback_text = '\n'.join(result['feedback'])
        else:
            feedback_text = "No issues found. Password looks good!"
        
        self.feedback_text.insert(1.0, feedback_text)
        self.feedback_text.config(state=tk.DISABLED)
    
    def toggle_password_visibility(self):
        """Toggle password visibility (show/hide)."""
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
    
    def generate_password(self):
        """Generate and display a secure password."""
        generated = self.analyzer.generate_password(length=16)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, generated)
        self.password_entry.event_generate('<KeyRelease>')
        messagebox.showinfo(
            "Generated Password",
            f"✅ Secure password generated and loaded!\n\nPassword: {generated}\n\n"
            "Click 'Save Password (to history)' to save it."
        )
    
    def clear_all(self):
        """Clear all fields and reset display."""
        self.password_entry.delete(0, tk.END)
        self.password_entry.event_generate('<KeyRelease>')
        self.show_password_var.set(False)
        messagebox.showinfo("Cleared", "✓ All fields cleared!")
    
    def save_password(self):
        """Save password to history (as hash for security)."""
        password = self.password_entry.get()
        
        if not password:
            messagebox.showwarning("Empty Password", "Please enter a password first.")
            return
        
        if len(password) < 6:
            messagebox.showwarning("Weak Password", "Password is too weak to save.")
            return
        
        result = self.analyzer.analyze(password)
        if result['score'] < 30:
            response = messagebox.askyesno(
                "Weak Password",
                "This password is weak. Are you sure you want to save it?"
            )
            if not response:
                return
        
        # Try to save
        if self.analyzer.db.add_password_to_history(password):
            messagebox.showinfo(
                "Saved",
                "✅ Password saved to history (as hash).\n"
                "This prevents reuse of old passwords."
            )
        else:
            messagebox.showwarning(
                "Already Used",
                "⚠️ This password has been used before!\n"
                "Please choose a different password."
            )


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Launch the application."""
    root = tk.Tk()
    app = PasswordStrengthAnalyzerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
