# Phishing Email Detection Model

A beginner-friendly machine learning project that detects phishing emails using Python and Scikit-learn.

## 📋 Project Overview

This project demonstrates how to build a practical machine learning model that classifies emails as either **"Phishing"** or **"Safe"** using natural language processing and the Naive Bayes classifier.

### What is Phishing?
Phishing is a type of cybercrime where attackers send fraudulent emails pretending to be legitimate sources to trick users into revealing sensitive information (passwords, credit card numbers, etc.).

### How Does This Model Work?
1. **Data Loading**: Loads a dataset of phishing and legitimate emails
2. **Feature Extraction**: Converts email text into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency)
3. **Pattern Detection**: Identifies suspicious patterns like:
   - Suspicious URLs
   - Urgency keywords (URGENT, ACT NOW, etc.)
   - Action keywords (Click here, Verify, etc.)
   - Unrealistic offers (Free gifts, Cash prizes, etc.)
4. **Model Training**: Trains a Naive Bayes classifier on the extracted features
5. **Classification**: Predicts whether new emails are phishing or safe
6. **Evaluation**: Reports accuracy, confusion matrix, and detailed metrics

## 🎯 Project Features

✅ **Easy to Understand**: Beginner-friendly code with detailed comments
✅ **Well-Documented**: Comprehensive docstrings and explanations
✅ **Sample Dataset**: 40+ pre-labeled phishing and safe emails
✅ **Feature Extraction**: Detects suspicious patterns and keywords
✅ **Model Evaluation**: Shows accuracy, confusion matrix, and classification report
✅ **Custom Predictions**: Test the model with your own emails
✅ **Professional Code**: Clean, organized, and error-handled

## 📊 Results

The model produces:
- **Accuracy Score**: Percentage of correctly classified emails
- **Confusion Matrix**: Shows true positives, false positives, etc.
- **Classification Report**: Precision, Recall, and F1-Score for each class
- **Custom Predictions**: Test with user-provided emails

## 📁 Project Structure

```
Phishing-Email-Detection/
├── main.py                      # Main script - run this to train and test the model
├── phishing_emails.csv          # Sample dataset with emails and labels
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation (this file)
└── QUICKSTART.md                # Quick start guide
```

## 🚀 Quick Start

See [QUICKSTART.md](QUICKSTART.md) for step-by-step setup and running instructions.

## 💻 System Requirements

- **Python 3.7+**
- **pip** (Python package manager)
- **Windows, macOS, or Linux**

## 📦 Dependencies

The project uses the following Python libraries:

| Library | Version | Purpose |
|---------|---------|---------|
| pandas | 2.0.3 | Data manipulation and CSV file handling |
| numpy | 1.24.3 | Numerical computing |
| scikit-learn | 1.3.0 | Machine learning algorithms |

## 🔧 Installation

### 1. Install Python
Download and install Python 3.7 or higher from [python.org](https://www.python.org/downloads/)

### 2. Clone or Download the Project
```bash
cd Phishing-Email-Detection
```

### 3. Create a Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Simply run the main script:

```bash
python main.py
```

The script will:
1. Load the email dataset
2. Extract features from emails
3. Train the machine learning model
4. Display model performance metrics
5. Test with custom sample emails
6. Show detailed classification results

## 📈 Understanding the Output

### Accuracy Score
```
ACCURACY SCORE: 95.00%
```
This means the model correctly classified 95% of the test emails.

### Confusion Matrix
```
                 Predicted
                Phishing  Safe
   Phishing       18       2
   Safe            1      19
```
- **18 phishing emails** were correctly identified ✓
- **19 safe emails** were correctly identified ✓
- **2 safe emails** were incorrectly flagged as phishing (False Positive)
- **1 phishing email** was missed (False Negative)

### Classification Report
Shows precision, recall, and F1-score for each class:
- **Precision**: How many emails flagged as phishing were actually phishing?
- **Recall**: How many actual phishing emails did we detect?
- **F1-Score**: Balance between precision and recall

## 🎓 Learning Concepts

This project teaches:
- **Text Processing**: Converting text to machine learning features
- **Feature Extraction**: Using TF-IDF for text analysis
- **Classification**: Binary classification problems
- **Model Evaluation**: Metrics for assessing model performance
- **Machine Learning Workflow**: Train-test split, model training, and evaluation

## 🔍 Key Phishing Indicators Detected

The model detects these suspicious patterns:
1. **URLs**: Presence of links in emails
2. **Suspicious URLs**: Links with suspicious domain names
3. **Urgency Keywords**: "URGENT", "ACT NOW", "IMMEDIATELY", "FINAL NOTICE"
4. **Action Keywords**: "Click here", "Verify account", "Update password"
5. **Offer Keywords**: "FREE", "BONUS", "GIFT CARD", "WON"
6. **Claim Keywords**: "CONGRATULATIONS", "SELECTED", "INHERITED"

## 📝 Dataset Format

The `phishing_emails.csv` file has two columns:
- **email_text**: The email content
- **label**: Either "Phishing" or "Safe"

Example:
```csv
email_text,label
"Click here to confirm your account http://malicious-bank.com verify now",Phishing
"Hi John, just checking in about the project.",Safe
```

## 🛠️ Customization Ideas

You can extend this project by:
1. **Adding More Data**: Collect real phishing emails and add to the dataset
2. **More Patterns**: Detect additional suspicious patterns (sender address, attachments, etc.)
3. **Different Algorithms**: Try Random Forest, SVM, or Neural Networks
4. **Web Interface**: Build a Flask/Django app for email classification
5. **Email Integration**: Connect to an email client for real-time filtering
6. **Hyperparameter Tuning**: Optimize model performance
7. **Cross-Validation**: Better model evaluation techniques

## ⚠️ Limitations

- **Small Dataset**: The sample dataset is small; production models need much more data
- **Pattern-Based**: Currently uses simple keyword detection; could be improved with deep learning
- **False Positives**: May occasionally flag legitimate emails as phishing
- **Language**: Primarily optimized for English emails
- **Evolving Threats**: Phishing techniques evolve; model needs regular updates

## 🧪 Testing

The script includes built-in tests with 4 sample emails:
1. A phishing email with suspicious URL
2. A legitimate work-related email
3. An urgent phishing attempt
4. A casual safe email

Results are shown for each test case.

## 🤝 Contributing

This is a beginner learning project. To improve it:
1. Add more emails to the dataset
2. Implement additional phishing detection patterns
3. Try different machine learning algorithms
4. Write unit tests for functions
5. Add command-line arguments for customization

## 📚 Resources

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [TF-IDF Explanation](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Naive Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
- [Phishing Education](https://www.phishing.org/)
- [Python Official Documentation](https://docs.python.org/3/)

## 📄 License

This is a beginner learning project. Feel free to use, modify, and distribute.

## 🎯 Project Goals

✓ Learn machine learning fundamentals
✓ Understand text classification
✓ Practice Python programming
✓ Build a practical application
✓ Deploy and evaluate ML models

## ❓ FAQ

**Q: Why Naive Bayes?**
A: It's a simple, fast, and effective algorithm for text classification, perfect for beginners.

**Q: Can I improve the accuracy?**
A: Yes! Add more training data, detect more patterns, or try different algorithms.

**Q: How do I use this in production?**
A: This is a learning project. For production, consider using mature email security services.

**Q: Can I run this on Windows/Mac/Linux?**
A: Yes! Python runs on all major operating systems.

**Q: What if I get an error?**
A: Check that Python 3.7+ is installed and all dependencies are installed via requirements.txt

## 👨‍💻 Author

Created as a beginner-friendly machine learning tutorial project.

## 📞 Support

If you encounter issues:
1. Check that all dependencies are installed
2. Ensure Python 3.7+ is being used
3. Verify that `phishing_emails.csv` is in the same directory
4. Check the [Python documentation](https://docs.python.org/3/) for additional help

---

**Happy Learning! 🚀**
