# INPUT VALIDATION DOCUMENTATION

## Overview

The Phishing Detection Awareness Tool now includes **robust input validation** for both Email and URL analysis. This ensures users provide properly formatted inputs before they are analyzed for phishing indicators.

---

## Validation Features

### Email Validation

#### What is Validated?
- ✅ Presence of `@` symbol
- ✅ Valid email format (user@domain.extension)
- ✅ Local part (before @) is not empty and ≤ 64 characters
- ✅ Domain part (after @) is not empty and ≤ 255 characters
- ✅ Domain doesn't start/end with dots
- ✅ No consecutive dots in domain
- ✅ Field is not empty

#### Email Validation Examples

**VALID EMAILS:**
- ✅ `user@example.com`
- ✅ `john.smith@company.co.uk`
- ✅ `support+tag@domain.org`
- ✅ `user.name+label@example.co.uk`

**INVALID EMAILS:**
- ❌ `notanemail` (missing @)
- ❌ `user@` (missing domain)
- ❌ `@example.com` (missing local part)
- ❌ `user@domain` (missing extension)
- ❌ `invalid email@domain.com` (spaces)
- ❌ `` (empty)

#### Error Messages
When an invalid email is provided, users receive specific error messages:
- "Email field cannot be empty."
- "Invalid email: Must contain '@' symbol."
- "Invalid email format. Expected: user@domain.com"
- "Invalid email: Local part cannot exceed 64 characters."
- "Invalid email: Domain cannot contain consecutive dots."

---

### URL Validation

#### What is Validated?
- ✅ Valid URL scheme (http, https, ftp, ftps)
- ✅ Presence of domain/netloc
- ✅ Valid URL format and structure
- ✅ No invalid characters in domain
- ✅ Field is not empty
- ✅ **Auto-completes with https:// if no scheme provided**

#### URL Validation Examples

**VALID URLS:**
- ✅ `https://www.example.com`
- ✅ `http://example.com`
- ✅ `example.com` (auto-converted to https://example.com)
- ✅ `ftp://files.example.com`
- ✅ `https://www.example.com/path?query=value`
- ✅ `https://192.168.1.1`

**INVALID URLS:**
- ❌ `not a url` (invalid format)
- ❌ `just random text` (no domain structure)
- ❌ `://no-domain.com` (missing scheme)
- ❌ `` (empty)
- ❌ `htp://example.com` (invalid protocol)

#### Error Messages
When an invalid URL is provided, users receive specific error messages:
- "URL field cannot be empty."
- "Invalid URL: Must include a protocol (http://, https://, etc.)."
- "Invalid URL format. Example: https://www.example.com"
- "Invalid URL: Domain must contain at least one dot."

---

## Where Validation Occurs

### 1. Console Mode
When running the tool in console mode (`python main.py`), validation happens:

```python
# User selects "email" or "url" mode
# User provides input
# Validation check occurs BEFORE analysis

if mode == "email":
    user_input = input("Paste the email text here:\n").strip()
    is_valid, error_message = validate_input(user_input, 'email')
    if not is_valid:
        print(f"❌ Invalid Email Input: {error_message}")
        return
    
    detected_issues = check_email(user_input)
```

### 2. GUI Mode
When running the tool in GUI mode (`python main.py` → select option 2), validation happens:

```python
# User selects radio button (Email or URL)
# User enters input in text box
# User clicks "Analyze" button
# Validation check occurs BEFORE analysis

def analyze(self):
    user_input = self.text_input.get("1.0", tk.END).strip()
    mode = self.mode.get()
    
    is_valid, error_message = validate_input(user_input, mode)
    if not is_valid:
        messagebox.showerror(
            "Invalid Input",
            f"The input is not a valid {mode}:\n\n{error_message}"
        )
        return
    
    detected_issues = check_email(user_input) if mode == "email" else check_url(user_input)
```

---

## Architecture

The validation system uses a dedicated module: `detector/validator.py`

### Functions

#### `is_valid_email(email_text) → tuple`
- **Input:** Email string to validate
- **Output:** `(is_valid: bool, error_message: str or None)`
- **Usage:** Validates email format before analysis

#### `is_valid_url(url_text) → tuple`
- **Input:** URL string to validate
- **Output:** `(is_valid: bool, error_message: str or None)`
- **Usage:** Validates URL format before analysis
- **Special:** Auto-adds `https://` prefix if no scheme provided

#### `validate_input(input_text, mode) → tuple`
- **Input:** User input and mode ('email' or 'url')
- **Output:** `(is_valid: bool, error_message: str or None)`
- **Usage:** Main validation router function

---

## Flow Diagram

```
USER INPUT
    ↓
┌─────────────────────────┐
│  validate_input()       │
├─────────────────────────┤
│ Check format            │
│ Check length            │
│ Check structure         │
└─────────────────────────┘
    ↓
[Valid?] 
    ↓YES              ↓NO
    ↓                 ↓
PROCEED TO        SHOW ERROR
ANALYSIS          MESSAGE
    ↓                 ↓
Detect Issues    User Corrects
Calculate Risk   Input
Display Results
```

---

## Security Benefits

1. **Input Validation**: Prevents malformed or suspicious input from being processed
2. **Error Guidance**: Clear messages help users understand what went wrong
3. **Injection Prevention**: Validates format before processing
4. **User Experience**: Fails fast with helpful feedback
5. **Consistency**: Same validation rules in both GUI and Console modes

---

## Testing

To test the validation system, run:

```bash
# Test email and URL validation
python test_validation.py

# Test realistic scenarios
python test_validation_realistic.py

# Test complete integration
python test_integration.py
```

---

## Usage Examples

### Example 1: Valid Email Analysis

**User selects:** Email mode
**User enters:** `support@paypal.com`
**Validation:** ✅ Passes
**Next step:** Analysis proceeds to check for phishing keywords

### Example 2: Invalid Email Rejection

**User selects:** Email mode
**User enters:** `notatvalidemail`
**Validation:** ❌ Fails
**Message:** "Invalid email: Must contain '@' symbol."
**Next step:** User is prompted to correct input

### Example 3: Valid URL with Auto-Completion

**User selects:** URL mode
**User enters:** `google.com`
**Validation:** ✅ Passes (auto-converted to `https://google.com`)
**Next step:** Analysis proceeds to check for phishing indicators

### Example 4: Invalid URL Rejection

**User selects:** URL mode
**User enters:** `not a website`
**Validation:** ❌ Fails
**Message:** "Invalid URL format. Example: https://www.example.com"
**Next step:** User is prompted to correct input

---

## Configuration

All validation rules are defined in `detector/validator.py`. To customize validation rules, modify:

- Email regex pattern in `is_valid_email()`
- URL regex pattern in `is_valid_url()`
- Character limits for email local/domain parts
- Supported URL schemes

---

## Summary

✅ **Input validation is now integrated into both console and GUI modes**
✅ **Invalid inputs are rejected BEFORE analysis**
✅ **Users receive clear, helpful error messages**
✅ **Validation protects the tool from malformed input**
✅ **Same validation rules in both interfaces for consistency**
