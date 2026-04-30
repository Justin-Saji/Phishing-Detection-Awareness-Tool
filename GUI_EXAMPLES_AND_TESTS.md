# GUI Enhancement - Usage Examples & Test Cases

## 📋 Practical Examples

### Example 1: Simple Email Address Check

**Input:**
```
admin@suspicious-bank.com
```

**Mode:** Any (Auto-Detect recommended)

**Results:**
- Extracted: Email address
- Analysis: Checks for suspicious keywords in "admin", domain analysis
- Risk Level: Depends on domain reputation
- Can copy from email header directly

---

### Example 2: Suspicious URL Check

**Input:**
```
http://paypa1-verify.com/confirm
```

**Mode:** Any (Auto-Detect recommended)

**Results:**
- Detected Issue: "Uses insecure HTTP protocol instead of HTTPS"
- Detected Issue: Domain looks like PayPal but with slight variation (paypa1 = confused letter)
- Risk Level: High
- Recommendation: Don't click, verify through official PayPal website

---

### Example 3: Full Email Content Analysis

**Input:**
```
From: security@amazon-alert.com
To: customer@gmail.com
Subject: Urgent: Verify Your Account Immediately

Dear Customer,

Your Amazon account has been flagged for suspicious activity. 
You must verify your account immediately by clicking the link below:

http://amazon-account-verify.com/login?customer_id=12345

If you don't verify within 24 hours, your account will be permanently closed.

Click here: http://amazon-account-verify.com/login
Contact: support@amazon-alert.com

Thank you,
Amazon Security Team
```

**Mode:** Auto-Detect

**Results:**
- **Found 3 items:**
  1. Email: security@amazon-alert.com (suspicious keywords)
  2. Email: support@amazon-alert.com (suspicious keywords)
  3. URL: http://amazon-account-verify.com/login?customer_id=12345 (HTTP, domain similarity spoofing)

- **Analysis:**
  - Email 1: "verify account" keyword detected
  - Email 2: Security team impersonation
  - URL: Uses HTTP instead of HTTPS, domain looks like Amazon but isn't

- **Overall Risk:** HIGH

---

### Example 4: Legitimate Content Check

**Input:**
```
From: support@microsoft.com
Subject: Update Available

Hi User,

A new update for Windows is available. 
Please visit https://www.microsoft.com/en-us/windows/windows-update

Contact: support@microsoft.com for help.

Best regards,
Microsoft Support
```

**Mode:** Auto-Detect

**Results:**
- **Found 2 items:**
  1. Email: support@microsoft.com
  2. URL: https://www.microsoft.com/en-us/windows/windows-update

- **Analysis:**
  - Email: No suspicious keywords detected
  - URL: Uses HTTPS (secure), legitimate Microsoft domain
  - No @ spoofing detected

- **Overall Risk:** LOW ✅

---

### Example 5: Mixed Suspicious Content

**Input:**
```
I got emails from:
billing@paypa1.com
noreply@confirm-amazon.com
alert@update-apple.com

And they sent me these links:
http://195.45.67.89/login
www.fak3-bank.com/verify
https://secure-paypal-verify.com/confirm
```

**Mode:** Auto-Detect

**Results:**
- **Found 6 items:**
  - 3 suspicious emails (all with phishing-like domains)
  - 3 suspicious URLs (HTTP, IP address, domain spoofing, excessive hyphens)

- **Risk Assessment:** HIGH for all items

---

## 🧪 Test Cases

### Test Case 1: Single Email Address
```
Input: user@example.com
Mode: Email Only (or Auto-Detect)
Expected: Analyzes email, shows results
Status: ✓ Pass
```

### Test Case 2: Single URL
```
Input: https://www.google.com
Mode: URL Only (or Auto-Detect)
Expected: Analyzes URL, shows results
Status: ✓ Pass
```

### Test Case 3: Invalid Email Format
```
Input: user@
Mode: Email Only
Expected: Error message with format suggestion
Status: ✓ Pass - Shows helpful error
```

### Test Case 4: Invalid URL Format
```
Input: not-a-url
Mode: URL Only
Expected: Error message
Status: ✓ Pass - Shows helpful error
```

### Test Case 5: Empty Input
```
Input: (empty)
Mode: Any
Expected: Warning to enter content
Status: ✓ Pass - Shows warning
```

### Test Case 6: Multiple Emails (Auto-Detect)
```
Input: user1@domain.com user2@domain.com user3@domain.com
Mode: Auto-Detect
Expected: Extracts and analyzes all 3, shows count
Status: ✓ Pass
```

### Test Case 7: Multiple URLs (Auto-Detect)
```
Input: 
https://site1.com
http://site2.com
www.site3.com
Mode: Auto-Detect
Expected: Extracts and analyzes all 3, shows count
Status: ✓ Pass
```

### Test Case 8: Mixed Content (Auto-Detect)
```
Input: admin@phishing.com check https://malicious.com for details
Mode: Auto-Detect
Expected: Extracts email and URL, analyzes both
Status: ✓ Pass
```

### Test Case 9: Full Email with Formatting
```
Input: [Full email with From, To, Subject, Body, Links]
Mode: Auto-Detect
Expected: Extracts and analyzes all emails and URLs
Status: ✓ Pass
```

### Test Case 10: Report Generation
```
Input: Any analyzed content
Action: Click "Save Report"
Expected: Saves .txt file with analysis details
Status: ✓ Pass
```

### Test Case 11: Clear Function
```
Input: Any content
Action: Click "Clear"
Expected: All input and results cleared, ready for new analysis
Status: ✓ Pass
```

### Test Case 12: Long Content Paste
```
Input: Very long email message (> 1000 characters)
Mode: Auto-Detect
Expected: Processes without lag, extracts and analyzes
Status: ✓ Pass
```

---

## 🔍 Real-World Phishing Email Examples

### Real Example 1: PayPal Phishing
```
From: info@paypa1.com
Subject: Urgent Action Required on Your PayPal Account

We've detected unusual activity on your account. Please verify your account immediately:

Click here to verify: http://paypal-confirm.net/verify?id=1234

Regards,
PayPal Security
```
**Auto-Detect Result:** HIGH RISK
- Suspicious domain (paypa1 = confused l and 1)
- HTTP instead of HTTPS
- Phishing keyword: "verify account"

---

### Real Example 2: Amazon Phishing
```
From: security@amazon-alert.com
Subject: Action Required - Confirm Your Identity

Dear Valued Customer,

For your security, we need to confirm your identity. 
Your account will be closed if you don't respond within 24 hours.

Verify here: http://amazon-verify.tk/

Amazon Customer Service
```
**Auto-Detect Result:** HIGH RISK
- Suspicious domain (.tk domain, not .com)
- HTTP instead of HTTPS
- Urgent language designed to pressure
- Domain doesn't match amazon.com

---

### Real Example 3: Bank Phishing
```
From: banking@secure-update.com
Subject: Update Your Banking Information

Dear Customer,

Please update your banking credentials using the link below to maintain service:

https://bank.secure-update.com/login

Thank you,
Bank Support Team
Contact: support@secure-update.com
```
**Auto-Detect Result:** MEDIUM RISK
- Domain structure suspicious (bank.secure-update.com)
- Request for banking credentials
- But uses HTTPS (partial security)
- Modern phishing attempt with some legitimacy appearance

---

### Real Example 4: Legitimate Email
```
From: support@github.com
Subject: GitHub Account Security Alert

Hi user,

We detected a new sign-in to your GitHub account from:
- Location: New York, NY
- Browser: Chrome on macOS
- Time: 2024-02-18 10:30 AM

If this wasn't you, please review your settings:
https://github.com/settings/security

If you need help, contact support@github.com

GitHub Security Team
```
**Auto-Detect Result:** LOW RISK ✅
- Legitimate domain (github.com)
- Uses HTTPS
- No urgent pressure language
- Specific technical details
- Direct link to official settings page

---

## 📊 Typical Analysis Patterns

### Pattern 1: High Risk Email
- Suspicious domain variations
- Urgent action language
- Requests for verification/confirmation
- HTTP links
- Threats or account closure warnings

### Pattern 2: Medium Risk Email
- Some legitimate-looking elements
- Contains phishing keywords
- Mixed security signals
- Requests sensitive information

### Pattern 3: Low Risk Email
- Official domain
- Technical details
- HTTPS links
- Professional tone
- No pressure language

---

## 🎓 Learning Path

1. **Start with Example 1** - Simple email address
2. **Try Example 2** - Basic URL analysis
3. **Progress to Example 3** - Full email content
4. **Challenge with Example 5** - Mixed complex content
5. **Review Real Examples** - Understand actual phishing
6. **Test Edge Cases** - Empty, invalid, very long inputs

---

## ✅ Checklist for Users

When analyzing content, ask:
- [ ] Is the domain legitimate?
- [ ] Is the URL using HTTPS?
- [ ] Does the sender email match the organization?
- [ ] Is there urgent language pressuring action?
- [ ] Are they asking for credentials or sensitive info?
- [ ] Do links match the claimed organization?
- [ ] Is the email address properly formatted?
- [ ] Do multiple items have similar phishing patterns?

---

## 🚀 Advanced Usage

### Batch Analysis
1. Copy multiple emails
2. Select Auto-Detect
3. Paste all content
4. Analyze - finds all items automatically
5. Save report includes all findings

### Comparison Analysis
1. Analyze suspicious email
2. Save report
3. Analyze legitimate email from same sender
4. Compare findings
5. Document patterns

### Documentation
1. Analyze phishing attempt
2. Save detailed report
3. Share with colleagues
4. Archive for training
5. Report to appropriate authorities

---

*Use these examples to understand phishing patterns and improve your email security awareness.*
