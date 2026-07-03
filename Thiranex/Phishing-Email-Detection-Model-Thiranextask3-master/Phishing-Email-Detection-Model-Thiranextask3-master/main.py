"""
Phishing Email Detection Model
A beginner-friendly machine learning project to classify emails as phishing or safe.

This script:
1. Loads email data from a CSV file
2. Extracts features using TF-IDF vectorization
3. Trains a Naive Bayes classifier
4. Evaluates the model with accuracy, confusion matrix, and classification report
"""

# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import re
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# ============================================================================
# STEP 1: LOAD AND PREPARE DATA
# ============================================================================

print("=" * 70)
print("PHISHING EMAIL DETECTION MODEL")
print("=" * 70)
print("\n[STEP 1] Loading email dataset...")

try:
    # Load the CSV file containing emails and labels
    df = pd.read_csv('phishing_emails.csv')
    print(f"✓ Successfully loaded {len(df)} emails")
    print(f"  - Phishing emails: {len(df[df['label'] == 'Phishing'])}")
    print(f"  - Safe emails: {len(df[df['label'] == 'Safe'])}")
except FileNotFoundError:
    print("✗ Error: 'phishing_emails.csv' not found!")
    print("  Make sure the CSV file is in the same directory as this script.")
    exit(1)

# ============================================================================
# STEP 2: FEATURE EXTRACTION AND DETECTION
# ============================================================================

print("\n[STEP 2] Extracting features and detecting phishing patterns...")

def extract_phishing_patterns(text):
    """
    Extract suspicious features from email text.
    
    This function detects common phishing indicators:
    - URLs (especially suspicious ones)
    - Urgency keywords
    - Suspicious action words
    - Numbers that might indicate fake offers
    
    Args:
        text (str): The email text to analyze
    
    Returns:
        dict: Dictionary containing detected patterns
    """
    
    patterns = {
        'has_url': 0,
        'has_suspicious_url': 0,
        'urgency_keywords': 0,
        'action_keywords': 0,
        'offer_keywords': 0,
        'claim_keywords': 0
    }
    
    text_lower = text.lower()
    
    # Detect URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    if urls:
        patterns['has_url'] = 1
        # Check for suspicious URL patterns (fake domains)
        for url in urls:
            if any(word in url for word in ['fake', 'malicious', 'verify', 'confirm', 'update', 'xyz', 'suspicious']):
                patterns['has_suspicious_url'] = 1
    
    # Detect urgency keywords
    urgency_words = ['urgent', 'immediately', 'act now', 'alert', 'confirm', 'verify', 'claim', 'final notice']
    if any(word in text_lower for word in urgency_words):
        patterns['urgency_keywords'] = 1
    
    # Detect action keywords
    action_words = ['click here', 'click now', 'update password', 'confirm identity', 'verify account']
    if any(word in text_lower for word in action_words):
        patterns['action_keywords'] = 1
    
    # Detect offer keywords
    offer_words = ['free', 'bonus', '99% off', 'gift card', 'claim', '$', 'won', 'winner']
    if any(word in text_lower for word in offer_words):
        patterns['offer_keywords'] = 1
    
    # Detect claim keywords
    claim_words = ['congratulations', 'selected', 'inherited', 'claim', 'exclusive']
    if any(word in text_lower for word in claim_words):
        patterns['claim_keywords'] = 1
    
    return patterns

# Create new feature columns by detecting patterns in each email
print("  Analyzing email patterns...")
for pattern in ['has_url', 'has_suspicious_url', 'urgency_keywords', 'action_keywords', 'offer_keywords', 'claim_keywords']:
    df[pattern] = df['email_text'].apply(lambda x: extract_phishing_patterns(x)[pattern])

print("✓ Feature extraction complete")

# ============================================================================
# STEP 3: PREPARE DATA FOR MODEL TRAINING
# ============================================================================

print("\n[STEP 3] Preparing data for model training...")

# Separate features (email text) and labels (Phishing/Safe)
X = df['email_text']  # Input features (email text)
y = df['label']       # Output labels (Phishing or Safe)

# Convert text to numerical features using TF-IDF
# TF-IDF (Term Frequency-Inverse Document Frequency) converts text to numbers
# that the machine learning model can understand
print("  Creating TF-IDF vectors (converting text to numbers)...")
tfidf_vectorizer = TfidfVectorizer(
    max_features=100,      # Use top 100 words as features
    stop_words='english',  # Ignore common English words like 'the', 'a', 'is'
    lowercase=True,        # Convert all text to lowercase
    min_df=1,              # Include words that appear in at least 1 document
    max_df=0.9             # Include words that appear in at most 90% of documents
)

# Transform the email text into TF-IDF vectors
X_tfidf = tfidf_vectorizer.fit_transform(X)
print(f"✓ Created {X_tfidf.shape[1]} TF-IDF features from email text")

# Split data into training and testing sets
# Training set (80%) - used to train the model
# Testing set (20%) - used to evaluate how well the model performs
print("  Splitting data: 80% training, 20% testing...")
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, 
    y, 
    test_size=0.2,       # Use 20% of data for testing
    random_state=42,     # For reproducible results
    stratify=y           # Keep same proportion of classes in both sets
)

print(f"✓ Training set size: {X_train.shape[0]} emails")
print(f"✓ Testing set size: {X_test.shape[0]} emails")

# ============================================================================
# STEP 4: TRAIN THE MODEL
# ============================================================================

print("\n[STEP 4] Training the Naive Bayes classifier...")
print("  This may take a moment...\n")

# Create and train the Naive Bayes classifier
# Naive Bayes is a simple, fast, and effective classifier for text classification
model = MultinomialNB()

# Train the model on the training data
model.fit(X_train, y_train)
print("✓ Model training complete!")

# ============================================================================
# STEP 5: MAKE PREDICTIONS
# ============================================================================

print("\n[STEP 5] Making predictions on test data...")

# Use the trained model to predict labels for the test set
y_pred = model.predict(X_test)

print("✓ Predictions complete!")

# ============================================================================
# STEP 6: EVALUATE MODEL PERFORMANCE
# ============================================================================

print("\n" + "=" * 70)
print("MODEL EVALUATION RESULTS")
print("=" * 70)

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"\n📊 ACCURACY SCORE: {accuracy:.2%}")
print(f"   The model correctly classified {accuracy:.2%} of emails")

# Create confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred, labels=['Phishing', 'Safe'])
print("\n📋 CONFUSION MATRIX:")
print("   (Shows how many emails were correctly/incorrectly classified)\n")
print("                 Predicted")
print("                Phishing  Safe")
print(f"   Phishing       {conf_matrix[0][0]:3d}      {conf_matrix[0][1]:3d}")
print(f"   Safe           {conf_matrix[1][0]:3d}      {conf_matrix[1][1]:3d}")

# Interpretation
print("\n   ✓ True Positives (TP): Correctly identified phishing emails")
print(f"     {conf_matrix[0][0]} emails were correctly classified as Phishing")
print("\n   ✓ True Negatives (TN): Correctly identified safe emails")
print(f"     {conf_matrix[1][1]} emails were correctly classified as Safe")
print(f"\n   ✗ False Positives (FP): Safe emails classified as Phishing")
print(f"     {conf_matrix[0][1]} safe emails were incorrectly flagged as Phishing")
print(f"\n   ✗ False Negatives (FN): Phishing emails classified as Safe")
print(f"     {conf_matrix[1][0]} phishing emails were incorrectly marked as Safe")

# Generate detailed classification report
report = classification_report(y_test, y_pred, target_names=['Phishing', 'Safe'])
print("\n📈 DETAILED CLASSIFICATION REPORT:")
print("   (Precision, Recall, and F1-Score for each class)\n")
print(report)

print("   Definitions:")
print("   - Precision: Of emails flagged as Phishing, how many were actually Phishing?")
print("   - Recall: Of all actual Phishing emails, how many did we detect?")
print("   - F1-Score: Balance between Precision and Recall (higher is better)")

# ============================================================================
# STEP 7: TEST WITH CUSTOM EMAILS
# ============================================================================

print("\n" + "=" * 70)
print("TESTING MODEL WITH CUSTOM EMAILS")
print("=" * 70)

def predict_email(email_text):
    """
    Predict whether a given email is phishing or safe.
    
    Args:
        email_text (str): The email text to classify
    
    Returns:
        tuple: (prediction, confidence_score)
    """
    # Convert the email text to TF-IDF vector
    email_tfidf = tfidf_vectorizer.transform([email_text])
    
    # Get prediction
    prediction = model.predict(email_tfidf)[0]
    
    # Get probability scores
    probabilities = model.predict_proba(email_tfidf)[0]
    confidence = max(probabilities)
    
    return prediction, confidence

# Test with sample emails
test_emails = [
    "Click here to verify your account: http://verify-account.fake",
    "Hi, just wanted to check in with you about the project",
    "URGENT: Your account will be closed! Update password immediately at http://fake-bank.com",
    "Looking forward to meeting you next week"
]

print("\nTesting with custom emails:\n")
for i, email in enumerate(test_emails, 1):
    prediction, confidence = predict_email(email)
    print(f"Email {i}:")
    print(f"  Text: {email}")
    print(f"  ✓ Classification: {prediction}")
    print(f"  ✓ Confidence: {confidence:.2%}\n")

# ============================================================================
# SUMMARY
# ============================================================================

print("=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)
print(f"""
✓ Successfully trained a phishing email detection model!

Key Achievements:
  • Loaded {len(df)} email samples
  • Extracted TF-IDF features from email text
  • Trained a Naive Bayes classifier
  • Achieved {accuracy:.2%} accuracy on test data
  • Can classify emails as Phishing or Safe

How the Model Works:
  1. Converts email text into numerical features using TF-IDF
  2. Detects suspicious patterns (URLs, urgency keywords, etc.)
  3. Uses Naive Bayes algorithm to classify the email
  4. Returns prediction and confidence score

Next Steps:
  • Improve accuracy by adding more training data
  • Add more phishing detection patterns
  • Deploy as an email filter
  • Fine-tune model parameters

Note: This is a beginner-friendly model for learning purposes.
For production use, consider more advanced techniques.
""")
print("=" * 70)
