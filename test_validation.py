# test_validation.py
# Test script to verify input validation

from detector.validator import is_valid_email, is_valid_url

print("=" * 60)
print("TESTING EMAIL VALIDATION")
print("=" * 60)

test_emails = [
    "user@example.com",
    "invalid.email",
    "user@",
    "@example.com",
    "user@domain",
    "user.name+tag@example.co.uk",
    "invalid email@example.com",
    "",
]

for email in test_emails:
    is_valid, error = is_valid_email(email)
    status = "✅ VALID" if is_valid else "❌ INVALID"
    print(f"\n{status}: '{email}'")
    if error:
        print(f"   Error: {error}")

print("\n" + "=" * 60)
print("TESTING URL VALIDATION")
print("=" * 60)

test_urls = [
    "https://www.example.com",
    "http://example.com",
    "example.com",  # Should add https:// prefix
    "not a url",
    "ftp://files.example.com",
    "htp://invalid.com",  # Wrong protocol
    "https://192.168.1.1",
    "https://www.example.com/path?query=value",
    "",
    "://no-domain.com",
]

for url in test_urls:
    is_valid, error = is_valid_url(url)
    status = "✅ VALID" if is_valid else "❌ INVALID"
    print(f"\n{status}: '{url}'")
    if error:
        print(f"   Error: {error}")

print("\n" + "=" * 60)
print("VALIDATION TESTS COMPLETED")
print("=" * 60)
