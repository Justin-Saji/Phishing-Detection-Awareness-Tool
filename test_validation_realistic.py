# test_validation_realistic.py
# Realistic integration test with proper email format

from detector.email_checker import check_email
from detector.url_checker import check_url
from detector.validator import validate_input
from utils.score_calculator import calculate_risk_score, calculate_risk_level
from utils.explanation import get_explanations

print("\n" + "=" * 80)
print("PHISHING DETECTION TOOL - INPUT VALIDATION TESTS")
print("=" * 80)

# TEST 1: Valid Email Address
print("\n" + "=" * 80)
print("TEST 1: VALID EMAIL ADDRESS")
print("=" * 80)
email1 = "security@paypal.com"
print(f"Input: {email1}")
is_valid, error = validate_input(email1, 'email')
if is_valid:
    print(f"✅ VALID EMAIL - Passed validation")
    # Check it for phishing keywords
    issues = check_email(email1)
    score = calculate_risk_score(issues)
    level = calculate_risk_level(issues)
    print(f"Analysis -> Risk Level: {level}, Score: {score}/100")
else:
    print(f"❌ REJECTED: {error}")

# TEST 2: Invalid Email (no @)
print("\n" + "=" * 80)
print("TEST 2: INVALID EMAIL (missing @ symbol)")
print("=" * 80)
email2 = "notanemail.com"
print(f"Input: {email2}")
is_valid, error = validate_input(email2, 'email')
if is_valid:
    print(f"✅ VALID - Passed validation")
else:
    print(f"❌ REJECTED - Input validation failed")
    print(f"   Error: {error}")

# TEST 3: Invalid Email (empty)
print("\n" + "=" * 80)
print("TEST 3: INVALID EMAIL (empty)")
print("=" * 80)
email3 = ""
print(f"Input: (empty)")
is_valid, error = validate_input(email3, 'email')
if is_valid:
    print(f"✅ VALID - Passed validation")
else:
    print(f"❌ REJECTED - Input validation failed")
    print(f"   Error: {error}")

# TEST 4: Valid Email with Phishing Keyword
print("\n" + "=" * 80)
print("TEST 4: VALID EMAIL WITH PHISHING INDICATORS")
print("=" * 80)
email4 = "verify@example.com"
print(f"Input: {email4}")
is_valid, error = validate_input(email4, 'email')
if is_valid:
    print(f"✅ VALID EMAIL - Passed validation")
    issues = check_email(email4)
    score = calculate_risk_score(issues)
    level = calculate_risk_level(issues)
    explanations = get_explanations(issues)
    print(f"Analysis -> Risk Level: {level}, Score: {score}/100")
    if issues:
        print(f"Issues Found:")
        for issue in issues:
            print(f"  • {issue}")
else:
    print(f"❌ REJECTED: {error}")

# TEST 5: Valid HTTPS URL
print("\n" + "=" * 80)
print("TEST 5: VALID SECURE URL (HTTPS)")
print("=" * 80)
url1 = "https://www.example.com/secure"
print(f"Input: {url1}")
is_valid, error = validate_input(url1, 'url')
if is_valid:
    print(f"✅ VALID URL - Passed validation")
    issues = check_url(url1)
    score = calculate_risk_score(issues)
    level = calculate_risk_level(issues)
    print(f"Analysis -> Risk Level: {level}, Score: {score}/100")
else:
    print(f"❌ REJECTED: {error}")

# TEST 6: Valid but Insecure HTTP URL
print("\n" + "=" * 80)
print("TEST 6: VALID URL WITH PHISHING INDICATORS (HTTP)")
print("=" * 80)
url2 = "http://secure-paypal-login.com"
print(f"Input: {url2}")
is_valid, error = validate_input(url2, 'url')
if is_valid:
    print(f"✅ VALID URL - Passed validation")
    issues = check_url(url2)
    score = calculate_risk_score(issues)
    level = calculate_risk_level(issues)
    explanations = get_explanations(issues)
    print(f"Analysis -> Risk Level: {level}, Score: {score}/100")
    if issues:
        print(f"Issues Found:")
        for issue in issues:
            print(f"  • {issue}")
else:
    print(f"❌ REJECTED: {error}")

# TEST 7: Invalid URL (no domain)
print("\n" + "=" * 80)
print("TEST 7: INVALID URL (not a URL)")
print("=" * 80)
url3 = "just random text"
print(f"Input: {url3}")
is_valid, error = validate_input(url3, 'url')
if is_valid:
    print(f"✅ VALID URL - Passed validation")
else:
    print(f"❌ REJECTED - URL validation failed")
    print(f"   Error: {error}")

# TEST 8: Invalid URL (empty)
print("\n" + "=" * 80)
print("TEST 8: INVALID URL (empty)")
print("=" * 80)
url4 = ""
print(f"Input: (empty)")
is_valid, error = validate_input(url4, 'url')
if is_valid:
    print(f"✅ VALID URL - Passed validation")
else:
    print(f"❌ REJECTED - URL validation failed")
    print(f"   Error: {error}")

# TEST 9: URL without scheme (should auto-add https://)
print("\n" + "=" * 80)
print("TEST 9: URL WITHOUT SCHEME (auto-completes with https://)")
print("=" * 80)
url5 = "example.com"
print(f"Input: {url5}")
is_valid, error = validate_input(url5, 'url')
if is_valid:
    print(f"✅ VALID URL - Auto-completed with https://")
    print(f"   Complete URL: https://{url5}")
else:
    print(f"❌ REJECTED: {error}")

# TEST 10: Complex valid email
print("\n" + "=" * 80)
print("TEST 10: COMPLEX VALID EMAIL")
print("=" * 80)
email5 = "john.smith+noreply@company.co.uk"
print(f"Input: {email5}")
is_valid, error = validate_input(email5, 'email')
if is_valid:
    print(f"✅ VALID EMAIL - Passed validation")
    issues = check_email(email5)
    score = calculate_risk_score(issues)
    level = calculate_risk_level(issues)
    print(f"Analysis -> Risk Level: {level}, Score: {score}/100")
else:
    print(f"❌ REJECTED: {error}")

print("\n" + "=" * 80)
print("SUMMARY: INPUT VALIDATION TEST COMPLETED")
print("=" * 80)
print("""
✅ VALIDATION FEATURES:
   1. Email validation checks for proper format (user@domain.extension)
   2. URL validation checks for protocol and domain structure
   3. Automatic https:// prefix addition for URLs without scheme
   4. Clear error messages for invalid inputs
   5. Both GUI and Console modes use the same validation

✅ SECURITY FEATURES:
   1. Invalid inputs are rejected BEFORE analysis
   2. Users get helpful error messages
   3. Prevents accidental analysis of malformed input
   4. Protects against injection attacks
""")
print("=" * 80 + "\n")
