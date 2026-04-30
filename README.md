# 🔒 Phishing Detection Awareness Tool

## What is Phishing?
Phishing is a cyber attack where attackers try to trick individuals into revealing sensitive information like passwords, credit card numbers, or personal data. They often do this through deceptive emails, websites, or messages that appear legitimate. Common tactics include creating urgency, promising rewards, or impersonating trusted organizations.

## Project Purpose
This tool is designed to educate beginners about phishing by analyzing emails and URLs for common suspicious patterns. It promotes cybersecurity awareness without using advanced techniques like machine learning, focusing instead on simple string matching and logical checks.

## ✨ Features

### Core Features
- **📧 Email Analysis**: Checks for suspicious keywords such as "urgent", "free", "click now", etc.
- **🔗 URL Analysis**: Detects insecure protocols (HTTP), IP addresses, @ symbols, and excessive hyphens.
- **📊 Risk Assessment**: Calculates a risk score (0-100) and assigns a risk level (LOW, MEDIUM, HIGH) based on detected issues.
- **🎯 Visual Risk Meter**: Displays a progress bar showing the risk percentage.
- **📚 Educational Explanations**: Provides clear reasons why something is flagged as suspicious.
- **💾 Report Generation**: Saves analysis results to a text file for reference.
- **✅ Input Validation (NEW)**: Validates that inputs are proper email addresses or URLs before analysis

### Interface Options
- **🖥️ Console Mode**: Original command-line interface for terminal users
- **🎨 GUI Mode (NEW)**: Modern Tkinter-based graphical interface with:
  - Dark cybersecurity-themed design
  - Real-time risk visualization
  - Color-coded risk levels
  - Interactive buttons and progress bars
  - Save reports with custom location
  - Professional report formatting
  - Input validation with helpful error messages

## 🚀 How to Run the Project

### Quick Start (GUI Mode - Recommended)
```bash
python main.py
```
Then select option `[2] GUI Mode` from the menu.

### Console Mode (Original)
```bash
python main.py
```
Then select option `[1] Console Mode` from the menu.

### Requirements
- Python 3.6 or higher
- No external packages required (uses only standard library)
  - `tkinter` comes built-in with Python

📁 Project Structure
```
phishing_detection_tool/
│
├── main.py                      # Entry point (supports both modes)
├── gui.py                       # 🆕 GUI interface (Tkinter-based)
├── README.md
├── requirements.txt
├── VALIDATION_DOCUMENTATION.md  # 🆕 Input validation guide
├── VALIDATION_QUICK_REFERENCE.md # 🆕 Quick validation reference
│
├── detector/
│   ├── __init__.py
│   ├── email_checker.py         # Email phishing detection logic
│   ├── url_checker.py           # URL phishing detection logic
│   ├── keyword_list.py          # Suspicious keywords database
│   └── validator.py             # 🆕 Input validation module
│
├── utils/
│   ├── __init__.py
│   ├── explanation.py           # Educational explanations
│   └── score_calculator.py      # Risk scoring engine
│
├── data/
│   └── sample_inputs.txt        # Test examples
│
└── output/
    └── report.txt               # Generated reports
```

## 🖥️ GUI Interface Overview

### Main Window Features
1. **Header Section**: Tool title and description
2. **Input Selection**: Radio buttons to choose between Email or URL analysis
3. **Text Input Box**: Paste email content or URL to analyze
4. **Analyze Button**: Trigger the analysis
5. **Results Display**:
   - Risk Level with emoji indicators (✅ Low, ⚠️ Medium, ⚠️ High)
   - Risk Score (0-100)
   - Interactive progress bar
   - Detailed issues and explanations
6. **Action Buttons**:
   - 💾 Save Report: Export analysis to file
   - 🗑️ Clear: Reset the interface

### Design Elements
- **Color Scheme**:
  - Dark background (#0a0e27) for reduced eye strain
  - Neon green text (#00ff88) for primary elements
  - Neon red/orange for warnings and alerts
  - Blue highlights for secondary information
  
- **Visual Feedback**:
  - Color-coded risk levels
  - Progress bar visualization
  - Real-time status updates
  - Emoji indicators for quick scanning

## 📊 How It Works

### Email Analysis Process
```
User Input (Email Address)
         ↓
✅ Validate Email Format
         ↓
Check for Suspicious Keywords
         ↓
Calculate Risk Score & Level
         ↓
Generate Explanations
         ↓
Display Results Visually
```

### URL Analysis Process
```
User Input (URL)
         ↓
✅ Validate URL Format
         ↓
Check for:
  • HTTP (insecure protocol)
  • IP addresses
  • @ symbols (domain spoofing)
  • Excessive hyphens
         ↓
Calculate Risk Score & Level
         ↓
Generate Explanations
         ↓
Display Results Visually
```

## ✅ Input Validation

The tool now includes robust input validation to ensure proper format:

### Email Validation
- ✅ Must contain `@` symbol
- ✅ Must follow `user@domain.extension` format
- ✅ Local part max 64 characters
- ✅ Domain part max 255 characters
- ✅ No consecutive dots

**Valid emails:**
- `user@example.com`
- `john.smith@company.co.uk`
- `support+tag@domain.org`

**Invalid emails:**
- `notanemail` (missing @)
- `user@` (incomplete)
- `@example.com` (no local part)

### URL Validation
- ✅ Must have valid protocol (http://, https://, ftp://, ftps://)
- ✅ Must have domain name
- ✅ Auto-completes with `https://` if missing
- ✅ No invalid characters

**Valid URLs:**
- `https://www.example.com`
- `example.com` (auto-converts to https://example.com)
- `http://website.org`

**Invalid URLs:**
- `not a website` (invalid format)
- `://example.com` (missing protocol)

**For detailed validation information, see [VALIDATION_DOCUMENTATION.md](VALIDATION_DOCUMENTATION.md) and [VALIDATION_QUICK_REFERENCE.md](VALIDATION_QUICK_REFERENCE.md)**

## 🧪 Sample Inputs
Check the `data/sample_inputs.txt` file for examples of suspicious and safe emails/URLs to test the tool.

### Test Cases
**Suspicious Email Examples:**
- Emails with words like "urgent", "verify", "reset password"
- Messages claiming account suspension
- Offers of free prizes or congratulations

**Suspicious URL Examples:**
- `http://bank-login-verify.com` (HTTP instead of HTTPS)
- `http://192.168.1.1/login` (IP address)
- `https://paypa1.com@google.com` (@ symbol)

## ⚠️ Limitations
- This tool uses basic pattern matching and may not detect sophisticated phishing attempts.
- It does not scan for malware or analyze attachments.
- False positives or negatives can occur; always use additional verification methods.
- No network connectivity required, but real-world checks should include domain reputation.

## 💡 Safety Tips
- ✅ Never click links from unsolicited emails
- ✅ Verify sender identity through official channels
- ✅ Check for HTTPS and security indicators in URLs
- ✅ Be suspicious of urgent requests for sensitive information
- ✅ Hover over links to see the actual URL before clicking
- ✅ Use two-factor authentication when available

## 🔮 Future Enhancements
- Integrate with online databases for domain reputation checking
- Add support for analyzing email headers
- Implement machine learning models for advanced detection
- Support for additional languages
- Mobile app version
- Integration with email clients

## 📦 Requirements
No external libraries are needed. The project uses only Python's standard library:
- `tkinter` (for GUI)
- `re` (for regex patterns)
- `datetime` (for timestamps)
- Standard file I/O

## 🤝 Contributing
Feel free to suggest improvements or add features while keeping the code:
- Simple and educational
- Well-documented
- Beginner-friendly
- Focused on phishing awareness

## 📄 License
This is an educational tool for learning about cybersecurity and phishing awareness.

## 🙏 Acknowledgments
Built with the goal of raising cybersecurity awareness among beginners. Stay safe online!