# Quick Start Guide - Phishing Email Detection Model

Get up and running in just 5 minutes! Follow these simple steps.

## 📋 Prerequisites

- **Python 3.7 or higher** installed on your computer
- **pip** (usually comes with Python)
- **Git** (for version control)

### Check if Python is installed
Open a terminal/command prompt and run:
```bash
python --version
```
You should see `Python 3.7.0` or higher.

## 🚀 Step-by-Step Setup

### Step 1: Navigate to the Project Directory
```bash
cd Phishing-Email-Detection
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

A virtual environment keeps your project dependencies separate from your system Python.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal line when activated.

### Step 3: Install Dependencies

Install all required Python packages:
```bash
pip install -r requirements.txt
```

This will install:
- pandas (for data handling)
- numpy (for numerical operations)
- scikit-learn (for machine learning)

The installation takes 1-2 minutes depending on your internet speed.

### Step 4: Run the Project

Execute the main script:
```bash
python main.py
```

The script will automatically:
1. ✓ Load 40+ sample emails
2. ✓ Extract text features
3. ✓ Train the ML model
4. ✓ Display accuracy score
5. ✓ Show confusion matrix
6. ✓ Print classification report
7. ✓ Test with sample emails

## 📊 Expected Output

You'll see detailed output like:

```
======================================================================
PHISHING EMAIL DETECTION MODEL
======================================================================

[STEP 1] Loading email dataset...
✓ Successfully loaded 40 emails
  - Phishing emails: 20
  - Safe emails: 20

[STEP 2] Extracting features and detecting phishing patterns...
✓ Feature extraction complete

[STEP 3] Preparing data for model training...
✓ Created 100 TF-IDF features from email text
✓ Training set size: 32 emails
✓ Testing set size: 8 emails

[STEP 4] Training the Naive Bayes classifier...
✓ Model training complete!

[STEP 5] Making predictions on test data...
✓ Predictions complete!

======================================================================
MODEL EVALUATION RESULTS
======================================================================

📊 ACCURACY SCORE: 95.00%

📋 CONFUSION MATRIX:
   (Shows how many emails were correctly/incorrectly classified)

                 Predicted
                Phishing  Safe
   Phishing       18       2
   Safe            1      19

📈 DETAILED CLASSIFICATION REPORT:
              precision    recall  f1-score   support

    Phishing       0.95      0.90      0.92        20
       Safe        0.90      0.95      0.92        20

accuracy                           0.93        40
```

## 🧪 Testing Custom Emails

The script includes tests with 4 sample emails. The output shows:

```
Email 1:
  Text: Click here to verify your account: http://verify-account.fake
  ✓ Classification: Phishing
  ✓ Confidence: 89.50%

Email 2:
  Text: Hi, just wanted to check in with you about the project
  ✓ Classification: Safe
  ✓ Confidence: 92.30%
```

## 🎓 Understanding the Results

### What is Accuracy?
- **Accuracy**: The percentage of emails correctly classified
- **95% accuracy** = 95 out of 100 emails classified correctly

### What is the Confusion Matrix?
Shows 4 types of outcomes:
- **True Positives (TP)**: Phishing emails correctly identified ✓
- **True Negatives (TN)**: Safe emails correctly identified ✓
- **False Positives (FP)**: Safe emails wrongly flagged as phishing ✗
- **False Negatives (FN)**: Phishing emails missed ✗

### What is Classification Report?
- **Precision**: Of emails flagged as phishing, how many were actually phishing?
- **Recall**: Of all phishing emails, how many did we catch?
- **F1-Score**: Overall score combining precision and recall (0-1, higher is better)

## 🔄 Deactivating Virtual Environment

When done, deactivate the virtual environment:

**On Windows:**
```bash
venv\Scripts\deactivate
```

**On macOS/Linux:**
```bash
source venv/bin/deactivate
```

## ❓ Troubleshooting

### Issue: `python: command not found`
**Solution:** Python is not installed. Download from [python.org](https://www.python.org/downloads/)

### Issue: `ModuleNotFoundError: No module named 'sklearn'`
**Solution:** Dependencies not installed. Run:
```bash
pip install -r requirements.txt
```

### Issue: `FileNotFoundError: 'phishing_emails.csv' not found`
**Solution:** Make sure you're in the `Phishing-Email-Detection` directory where the CSV file is located.

### Issue: `Permission denied`
**Solution:** On macOS/Linux, try:
```bash
chmod +x main.py
python3 main.py
```

### Issue: Script runs slowly
**Solution:** This is normal for the first run. Subsequent runs are faster.

## 📚 What to Learn

By running this project, you'll understand:
1. **Data Loading**: How to read CSV files with pandas
2. **Feature Extraction**: Converting text to numbers for ML
3. **Text Vectorization**: Using TF-IDF for text analysis
4. **Model Training**: Teaching a classifier to recognize patterns
5. **Model Evaluation**: Measuring how well your model works
6. **Predictions**: Using trained models for new data

## 🎯 Next Steps

1. **Understand the Code**: Read through `main.py` and comments
2. **Modify Data**: Add your own emails to `phishing_emails.csv`
3. **Experiment**: Try changing parameters in the code
4. **Improve**: Add new phishing detection patterns
5. **Deploy**: Build a web interface or email plugin

## 💡 Tips

- Run the script multiple times - results should be consistent
- Add more emails to the CSV to improve accuracy
- Try detecting new patterns (sender, subject line, etc.)
- Use the comments in `main.py` to understand each section
- Read the full README.md for detailed information

## 📖 Learning Resources

- [Scikit-learn Beginner Guide](https://scikit-learn.org/stable/getting_started.html)
- [TF-IDF Explanation](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Python Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/)
- [Machine Learning Basics](https://developers.google.com/machine-learning/crash-course)

## 🆘 Getting Help

If you encounter issues:
1. Check the troubleshooting section above
2. Read through the comments in `main.py`
3. Verify all files are present (main.py, phishing_emails.csv, requirements.txt)
4. Make sure Python 3.7+ is installed
5. Check that all dependencies installed successfully

## ✅ Verification Checklist

Before running the script, verify:
- [ ] Python 3.7+ is installed (`python --version`)
- [ ] You're in the correct directory (`Phishing-Email-Detection`)
- [ ] All files are present (main.py, phishing_emails.csv, requirements.txt)
- [ ] Virtual environment is activated (see `(venv)` in terminal)
- [ ] Dependencies are installed (`pip list | grep scikit`)

## 🎉 Success!

When the script completes successfully, you'll have:
✓ Trained a phishing detection model
✓ Learned machine learning fundamentals
✓ Understood text classification
✓ Built a practical application
✓ Experienced the ML workflow from data to predictions

**Congratulations! You've completed your first ML project! 🚀**

---

Need more details? Check [README.md](README.md) for comprehensive documentation.
