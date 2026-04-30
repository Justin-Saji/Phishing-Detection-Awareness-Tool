
#  Phishing Detection Awareness Tool

## 📌 Overview

The **Phishing Detection Awareness Tool** is a Python-based cybersecurity application designed to help users identify and understand phishing attacks in emails and URLs.

This project focuses on **user awareness and education**, by not only detecting suspicious patterns but also explaining *why* the input may be malicious.

It features a **Graphical User Interface (GUI)** for easy interaction and demonstrates real-world phishing detection techniques using rule-based analysis.

---

## 🎯 Objectives

* Detect potential phishing attempts in emails and URLs
* Educate users about common phishing techniques
* Provide risk analysis with clear explanations
* Simulate real-world cybersecurity detection mechanisms

---

## ⚙️ Features

### 🧪 Input Analysis

* Analyze **email content** for phishing indicators
* Analyze **URLs** for suspicious patterns

### 🔍 Detection Techniques

* Keyword-based detection (e.g., *urgent, verify, click now*)
* URL structure analysis (HTTP, IP-based URLs, special characters)
* Regex-based pattern detection
* Domain reputation checking using:

  * 🔴 Blacklist (known malicious domains)
  * 🟢 Whitelist (trusted domains)

### 📊 Risk Assessment

* Generates a **risk score (0–100)**
* Classifies input as:

  * 🟢 Low Risk
  * 🟡 Medium Risk
  * 🔴 High Risk

### 🖥️ GUI Interface

* User-friendly interface built using Tkinter
* Input box for email/URL
* Analyze button for instant results
* Visual risk indicator
* Explanation panel

### 📈 Additional Features

* Domain reputation display (Trusted / Unknown / Blacklisted)
* Detailed explanation of detected threats
* Report generation (stored in output file)

---

## 🧠 How It Works

1. User enters email text or URL
2. System analyzes input using:

   * Keyword detection
   * Pattern matching
   * URL structure analysis
   * Domain reputation check
3. A **rule-based scoring system** calculates risk
4. The system displays:

   * Risk level
   * Risk score
   * Reasons for detection
   * Security recommendations

---

## 🏗️ Project Structure

```
phishing_detection_tool/
│
├── main.py
├── gui.py
│
├── detector/
│   ├── email_checker.py
│   ├── url_checker.py
│   └── keyword_list.py
│
├── utils/
│   ├── explanation.py
│   └── score_calculator.py
│
├── database/
│   ├── blacklist.txt
│   └── whitelist.txt
│
├── output/
│   └── report.txt
│
└── README.md
```

---

##  Technologies Used

* Python
* Tkinter (GUI)
* Regular Expressions (Regex)
* File Handling

---

##  How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/phishing_detection_tool.git
```

2. Navigate to the project folder:

```bash
cd phishing_detection_tool
```

3. Run the application:

```bash
python main.py
```

---

##  Example Output

```
Risk Score: 78/100
Risk Level: HIGH

Reasons:
- Urgency-based language detected
- Suspicious URL structure
- Domain found in blacklist

Recommendation:
Do not click the link and verify the source.

##  Cybersecurity Concepts Covered

* Phishing attacks and social engineering
* URL manipulation techniques
* Domain impersonation
* Rule-based threat detection
* Risk scoring systems

##  Future Enhancements

* Machine Learning-based phishing detection
* Real-time domain reputation API integration
* Browser extension version
* Web-based dashboard (Flask)
* Bulk email/URL scanning
* Data visualization and analytics

## 🎓 Academic Value

This project demonstrates:

* Practical application of cybersecurity concepts
* Secure coding practices
* Modular software design
* User-focused awareness tools

## 📄 License

This project is developed for educational purposes.
********
