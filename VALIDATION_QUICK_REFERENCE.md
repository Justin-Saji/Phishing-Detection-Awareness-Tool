# QUICK START GUIDE - INPUT VALIDATION

## What's New?

Your Phishing Detection Tool now validates all inputs before analysis to ensure:
- ✅ Emails are in proper format
- ✅ URLs have correct structure
- ✅ Invalid input is rejected with helpful messages
- ✅ Analysis only proceeds with valid input

---

## Email Mode - What to Enter

### ✅ DO ENTER EMAIL ADDRESSES:
```
user@example.com
john.smith@company.co.uk
support+help@domain.org
```

### ❌ DON'T ENTER:
```
The user@example.com     (extra text)
user@                    (incomplete)
@example.com             (no user part)
just_some_text           (no @ symbol)
```

---

## URL Mode - What to Enter

### ✅ DO ENTER URLS:
```
https://www.example.com
http://website.org
example.com              (auto-converts to https://example.com)
https://site.com/path?query=value
```

### ❌ DON'T ENTER:
```
not a website            (no domain structure)
just random text         (invalid format)
www.example              (missing extension)
://example.com           (missing protocol)
```

---

## Common Error Messages & Fixes

### Email Mode

| Error Message | What It Means | Solution |
|---|---|---|
| "Email field cannot be empty." | You didn't enter anything | Enter an email address |
| "Must contain '@' symbol." | Missing @ | Add @ between user and domain |
| "Invalid email format. Expected: user@domain.com" | Wrong format | Use format: name@domain.com |
| "Domain cannot contain consecutive dots." | Double dots detected | Remove consecutive dots |

### URL Mode

| Error Message | What It Means | Solution |
|---|---|---|
| "URL field cannot be empty." | You didn't enter anything | Enter a URL |
| "Invalid URL format. Example: https://www.example.com" | Wrong format | Use format: https://domain.com |
| "Must include a protocol" | No https://, http://, etc. | Add protocol or tool will auto-add https:// |
| "Domain must contain at least one dot" | Missing domain extension | Use format: domain.com or domain.co.uk |

---

## Examples

### Example 1: Analyzing a Suspicious Email Address

1. Click on **"Check Email"** radio button
2. Enter: `verify.security@paypa1.com`
3. Click **"Analyze"**
4. ✅ Input is valid, analysis proceeds
5. See risk level and detected issues

### Example 2: Analyzing a Website URL

1. Click on **"Check URL"** radio button
2. Enter: `amazon-account-verify.com`
3. Click **"Analyze"**
4. ✅ Input is valid (auto-converted to https://amazon-account-verify.com)
5. See risk level and detected issues

### Example 3: Invalid Input Rejection

1. Click on **"Check Email"** radio button
2. Enter: `not a valid email`
3. Click **"Analyze"**
4. ❌ Error message appears: "Invalid email: Must contain '@' symbol."
5. Correct your input and try again

---

## Pro Tips

🔹 **URLs without "https://"?** No problem! The tool automatically adds it.

🔹 **Copy-paste support:** Works with full URLs including paths and query strings.

🔹 **Email validation:** Checks format first, then analyzes for phishing keywords.

🔹 **Error messages:** Always tell you exactly what's wrong.

---

## Getting Help

If you get an error message:
1. Read the error carefully
2. Use the table above to understand what's wrong
3. Correct your input
4. Try again

The validation is there to **protect you** by ensuring only proper input is analyzed.

---

## Summary

| Mode | Valid Input | Auto-Correction |
|---|---|---|
| **Email** | user@domain.com | None |
| **URL** | https://domain.com | Adds https:// if missing |

**Remember:** Valid format = ✅ Analysis proceeds
**Invalid format = ❌ Clear error message**
