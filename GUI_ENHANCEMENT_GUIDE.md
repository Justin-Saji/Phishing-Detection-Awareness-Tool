# GUI Enhancement Guide - Phishing Detection Awareness Tool

## Overview
The GUI has been significantly enhanced to be more flexible and user-friendly, allowing you to easily copy and paste email content or URLs to check for phishing threats.

## New Features

### 1. **Auto-Detect Mode (Recommended)** 🤖
- **What it does**: Automatically detects and extracts all emails and URLs from pasted content
- **Best for**: 
  - Full email content (with body, headers, links)
  - Mixed content with multiple emails and URLs
  - Quick analysis without manual selection

#### How to use:
1. Select **"🤖 Auto-Detect (Recommended)"** radio button
2. Paste any content:
   - Single email address: `user@example.com`
   - Single URL: `https://suspicious-site.com`
   - Full email content with sender info and links
   - Multiple emails separated by spaces or newlines
3. Click **"🔍 ANALYZE"**
4. The tool will automatically:
   - Extract all emails and URLs found
   - Analyze each one for phishing indicators
   - Display results for the first item
   - Show count of total items found

### 2. **Manual Modes**
- **📧 Email Only**: Analyze a single email address
- **🔗 URL Only**: Analyze a single URL

#### How to use:
1. Select the appropriate mode
2. Paste your content
3. Click **"🔍 ANALYZE"**

## What You Can Paste

### Email Content Examples:
```
user@example.com
admin@company.com
sender@domain.co.uk
```

### URL Examples:
```
https://www.example.com
http://insecure-site.com
www.domain.com
https://suspicious-domain-123.com/login?id=user
```

### Full Email Examples:
```
From: support@bank.com
Subject: Urgent: Verify Your Account
Body:
Click here to verify: http://banking-secure.com/verify
Contact: admin@bank.com
```

### Mixed Content:
```
I received an email from user@phishing-site.com asking me to click https://malicious-url.com
The legitimate contact is support@real-company.com
```

## Analysis Results

### Risk Levels:
- 🟢 **Low**: Content appears safe, but always exercise caution
- 🟡 **Medium**: Some suspicious indicators detected
- 🔴 **High**: Multiple phishing indicators detected

### Risk Score:
- **0-33**: Low Risk
- **34-66**: Medium Risk  
- **67-100**: High Risk

### Detected Issues:
The tool checks for:
- **Emails**: Suspicious keywords commonly used in phishing (verify account, confirm identity, etc.)
- **URLs**: 
  - Insecure HTTP instead of HTTPS
  - IP addresses instead of domain names
  - @ symbols (URL spoofing)
  - Excessive hyphens in domain

## Features

### Save Report 💾
- Saves a detailed analysis report as a text file
- Includes risk assessment, detected issues, and safety tips
- Default filename: `phishing_report_YYYYMMDD_HHMMSS.txt`

### Clear 🗑️
- Clears all input and results
- Ready for new analysis

### Copy-Paste Workflow
1. **Copy** from email client or webpage (Ctrl+C)
2. **Click** in the input text area
3. **Paste** (Ctrl+V)
4. **Select** analysis mode
5. **Click** ANALYZE
6. **Review** results

## Tips & Best Practices

### For Email Analysis:
- Paste the full email content including sender address
- Include subject line and body text
- The tool will extract the sender email automatically

### For URL Analysis:
- Paste complete URLs including the protocol (http:// or https://)
- For shortened URLs, use the full expanded URL
- Multiple URLs can be pasted separately

### Auto-Detect Tips:
- Works best when analyzing multiple items at once
- Automatically separates emails from URLs
- Provides count of total items analyzed
- Shows which item is currently being analyzed

### Using Multiple Items:
- Auto-Detect mode finds all emails and URLs in your pasted content
- Each item is analyzed individually
- Results show the specific item analyzed
- Can save reports for each analysis

## Common Scenarios

### Scenario 1: Email from Unknown Sender
```
From: security-alert@bank-update.com
Subject: URGENT: Verify Your Account
Body: Your account has been compromised. Click here immediately:
https://bank-secure-verify.com/login
```
**Action**: Paste the entire email content, select Auto-Detect, click Analyze

### Scenario 2: Suspicious Link in Message
```
https://paypa1.com/confirm-payment
```
**Action**: Paste the URL, select URL mode or Auto-Detect, click Analyze

### Scenario 3: Multiple Suspicious Emails
```
support@fake-amazon.com
noreply@suspicious-bank.com
alert@confirm-identity.com
```
**Action**: Paste all addresses, select Auto-Detect, click Analyze (will analyze each)

## Keyboard Shortcuts
- **Ctrl+A**: Select all text in input area
- **Ctrl+V**: Paste content
- **Ctrl+X**: Cut text
- **Enter**: Can be used to add multiple lines

## Troubleshooting

### No Items Found Message:
- Ensure the content contains at least one valid email or URL
- Email format: `something@domain.com`
- URL format: `https://domain.com` or `www.domain.com`

### Invalid Input Error:
- Switch to Auto-Detect mode for better flexibility
- Ensure proper formatting without typos
- Try pasting the complete content including all parts

### Unclear Results:
- Check the "Detected Issues & Explanations" section
- Review the Risk Score and Risk Level
- Save the report for detailed documentation

## Safety Tips (Displayed in Tool)
- ✋ Never click links from unsolicited emails
- 🔍 Verify sender identity through official channels
- 🔒 Check for HTTPS and security indicators in URLs
- ⚠️ Be suspicious of urgent requests for sensitive information

## Report Generation
Click **"💾 Save Report"** to save:
- Analysis timestamp
- Analysis type (Email/URL)
- Risk assessment
- Analyzed content
- Detected issues
- Detailed explanations
- Safety recommendations

---

**Remember**: While this tool helps identify potential phishing attempts, always use additional judgment. When in doubt, contact the organization directly through known official channels.
