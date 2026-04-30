# VALIDATION TESTING GUIDE

## How to Test Input Validation

This guide shows you how to test the new input validation feature in both GUI and Console modes.

---

## 🧪 Automated Tests

### Run All Tests
```bash
# Test 1: Basic validation
python test_validation.py

# Test 2: Realistic scenarios  
python test_validation_realistic.py

# Test 3: Complete integration
python test_integration.py
```

### Expected Results
All tests should show ✅ checkmarks for valid inputs and ❌ rejection messages for invalid inputs.

---

## 🎮 Manual Testing - GUI Mode

### How to Launch GUI
```bash
python main.py
# Select: [2] GUI Mode
```

### Test Case 1: Valid Email
1. Click "📧 Check Email" radio button
2. Enter: `support@paypal.com`
3. Click "🔍 ANALYZE"
4. **Expected:** Analysis proceeds, shows risk level

### Test Case 2: Invalid Email (No @)
1. Click "📧 Check Email" radio button  
2. Enter: `notanemail.com`
3. Click "🔍 ANALYZE"
4. **Expected:** Error dialog shows: "Invalid email: Must contain '@' symbol."

### Test Case 3: Invalid Email (Empty)
1. Click "📧 Check Email" radio button
2. Leave text box empty
3. Click "🔍 ANALYZE"
4. **Expected:** Error dialog shows: "Email field cannot be empty."

### Test Case 4: Valid URL
1. Click "🔗 Check URL" radio button
2. Enter: `https://www.google.com`
3. Click "🔍 ANALYZE"
4. **Expected:** Analysis proceeds, shows risk level

### Test Case 5: Invalid URL (Random Text)
1. Click "🔗 Check URL" radio button
2. Enter: `not a website`
3. Click "🔍 ANALYZE"
4. **Expected:** Error dialog shows: "Invalid URL format. Example: https://www.example.com"

### Test Case 6: URL Auto-Completion
1. Click "🔗 Check URL" radio button
2. Enter: `google.com`
3. Click "🔍 ANALYZE"
4. **Expected:** 
   - Analysis proceeds
   - URL is auto-completed to `https://google.com`

### Test Case 7: Invalid Email (Missing Domain)
1. Click "📧 Check Email" radio button
2. Enter: `user@`
3. Click "🔍 ANALYZE"
4. **Expected:** Error dialog shows: "Invalid email format. Expected: user@domain.com"

### Test Case 8: Invalid URL (Empty)
1. Click "🔗 Check URL" radio button
2. Leave text box empty
3. Click "🔍 ANALYZE"
4. **Expected:** Error dialog shows: "URL field cannot be empty."

### Test Case 9: Valid Complex Email
1. Click "📧 Check Email" radio button
2. Enter: `john.smith+noreply@company.co.uk`
3. Click "🔍 ANALYZE"
4. **Expected:** Analysis proceeds, shows risk level

### Test Case 10: Valid URL with Path
1. Click "🔗 Check URL" radio button
2. Enter: `https://www.example.com/page?query=value`
3. Click "🔍 ANALYZE"
4. **Expected:** Analysis proceeds, shows risk level

---

## 💻 Manual Testing - Console Mode

### How to Launch Console
```bash
python main.py
# Select: [1] Console Mode
```

### Test Case 1: Valid Email
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): email
Paste the email text here:
verify@bankname.com

Expected: Analysis proceeds, shows risk level
```

### Test Case 2: Invalid Email (No @)
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): email
Paste the email text here:
notanemail

Expected: "❌ Invalid Email Input: Invalid email: Must contain '@' symbol."
Returns to menu
```

### Test Case 3: Invalid Email (Incomplete)
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): email
Paste the email text here:
user@

Expected: "❌ Invalid Email Input: Invalid email format. Expected: user@domain.com"
Returns to menu
```

### Test Case 4: Valid URL
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): url
Enter the URL: https://www.example.com

Expected: Analysis proceeds, shows risk level
```

### Test Case 5: Invalid URL (Random Text)
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): url
Enter the URL: just random text

Expected: "❌ Invalid URL Input: Invalid URL format. Example: https://www.example.com"
Returns to menu
```

### Test Case 6: URL Auto-Completion
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): url
Enter the URL: example.com

Expected: Analysis proceeds (URL auto-converted to https://example.com)
```

### Test Case 7: Valid URL with HTTP
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): url
Enter the URL: http://example.com

Expected: Analysis proceeds, may show phishing warning for HTTP
```

### Test Case 8: Valid Complex Email
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): email
Paste the email text here:
support+tag@company.co.uk

Expected: Analysis proceeds, shows risk level
```

### Test Case 9: Spaces in Email
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): email
Paste the email text here:
user @example.com

Expected: "❌ Invalid Email Input: Invalid email format. Expected: user@domain.com"
```

### Test Case 10: Empty Input
```
Do you want to check an Email or a URL? (Enter 'email' or 'url'): email
Paste the email text here:
(just press Enter)

Expected: "❌ Invalid Email Input: Email field cannot be empty."
```

---

## 📋 Test Results Table

| Test Case | Input | Mode | Expected Result |
|-----------|-------|------|-----------------|
| Valid email | support@paypal.com | Email | ✅ Analysis |
| Missing @ | notanemail | Email | ❌ Error |
| No domain | user@ | Email | ❌ Error |
| Empty email | (blank) | Email | ❌ Error |
| Valid URL | https://www.google.com | URL | ✅ Analysis |
| Invalid format | not a website | URL | ❌ Error |
| Empty URL | (blank) | URL | ❌ Error |
| Auto-complete | google.com | URL | ✅ Analysis (auto-converted) |
| Complex email | john.smith+tag@co.uk | Email | ✅ Analysis |
| URL with path | site.com/page?q=val | URL | ✅ Analysis |

---

## ✨ What to Look For

### GUI Mode ✅
- Error dialogs appear for invalid input
- Error messages are clear and specific
- Valid input proceeds to analysis
- Clear button resets the form
- Save button is available after analysis

### Console Mode ✅
- Error messages start with "❌ Invalid"
- Specific error description follows
- Program returns to menu after error
- Valid input shows "=" analysis report
- Report is saved to output/report.txt

---

## 🐛 Troubleshooting

### Issue: GUI won't open
**Solution:** Ensure tkinter is installed
```bash
# For Windows
python -m pip install tk
```

### Issue: Error messages don't appear
**Solution:** Check Python version (requires 3.6+)
```bash
python --version
```

### Issue: Validation too strict
**Solution:** Email must have @ symbol, URL must have domain
- Email example: `user@domain.com`
- URL example: `https://domain.com`

### Issue: URL won't accept www without https
**Solution:** Enter `www.example.com` and it auto-converts to `https://www.example.com`

---

## 📊 Validation Performance

- Email validation: < 1ms
- URL validation: < 1ms
- No network calls
- Local validation only
- Works offline

---

## 🎓 Learning Points

Testing validation teaches you about:
1. Input validation best practices
2. Error handling and user experience
3. Regular expressions
4. User-friendly error messages
5. Defensive programming

---

## ✅ Validation Checklist

- [ ] Tested valid emails
- [ ] Tested invalid emails (no @, incomplete, empty)
- [ ] Tested valid URLs
- [ ] Tested invalid URLs (random text, empty)
- [ ] Tested URL auto-completion
- [ ] Tested in GUI mode
- [ ] Tested in Console mode
- [ ] Verified error messages are helpful
- [ ] Ran automated test suite
- [ ] Analysis works after valid input

---

## 🚀 Next Steps

Once validation is confirmed working:
1. Start using the tool for real analysis
2. Try different phishing examples
3. Generate and save reports
4. Check output/report.txt
5. Explore both GUI and Console modes

---

## 📞 Support

For detailed information:
- See [VALIDATION_DOCUMENTATION.md](VALIDATION_DOCUMENTATION.md)
- See [VALIDATION_QUICK_REFERENCE.md](VALIDATION_QUICK_REFERENCE.md)
- Run tests: `python test_*.py`

---

Happy testing! 🎉
