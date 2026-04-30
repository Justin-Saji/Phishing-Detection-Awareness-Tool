# main.py
# Entry point for Phishing Detection Awareness Tool
# Supports both console and GUI interfaces

from detector.email_checker import check_email
from detector.url_checker import check_url
from detector.validator import validate_input
from utils.score_calculator import calculate_risk_score, calculate_risk_level
from utils.explanation import get_explanations
from utils.statistics import global_stats
import sys
import re


def console_mode():
    """
    Console-based interface for phishing detection.
    This is the original command-line interface.
    """
    print("\n" + "=" * 50)
    print("Welcome to the Phishing Detection Awareness Tool!")
    print("This tool helps you identify potential phishing emails or URLs.")
    print("=" * 50 + "\n")

    # Ask user what to check
    choice = input("Do you want to check an Email or a URL? (Enter 'email' or 'url'): ").strip().lower()

    if choice == 'email':
        email_text = input("\nPaste the email text here (address or full message):\n").strip()

        # If the user pasted a full email message (contains newlines, headers, or links),
        # treat it as email content and analyze for suspicious keywords and links.
        looks_like_full_email = (
            '\n' in email_text or
            'subject:' in email_text.lower() or
            'from:' in email_text.lower() or
            'http' in email_text.lower() or
            'www.' in email_text.lower()
        )

        def extract_emails(text):
            pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            return re.findall(pattern, text)

        def extract_urls(text):
            pattern = r'https?://[^\s]+|www\.[^\s]+'
            return re.findall(pattern, text)

        if looks_like_full_email:
            # Prefer analyzing full message content directly
            detected_issues = check_email(email_text)
            # If no obvious suspicious keywords were found, also scan any URLs present
            urls_found = extract_urls(email_text)
            if urls_found:
                for u in urls_found:
                    detected_issues.extend(check_url(u))
        else:
            # The user likely provided a single email address.
            # Try to sanitize common paste issues (e.g. ' at ' -> '@') then validate.
            sanitized = email_text.replace(' at ', '@').replace('(at)', '@').replace('[at]', '@')
            is_valid, error_message = validate_input(sanitized, 'email')
            if not is_valid:
                # If validation fails but we can extract an email from the text, use that.
                extracted = extract_emails(email_text)
                if extracted:
                    detected_issues = check_email('\n'.join(extracted))
                else:
                    print(f"\n❌ Invalid Email Input: {error_message}")
                    print("Please ensure you enter a valid email address (e.g., user@domain.com) or paste the full email content.")
                    return
            else:
                detected_issues = check_email(sanitized)
        
    elif choice == 'url':
        url = input("\nEnter the URL: ").strip()
        
        # Validate URL input
        is_valid, error_message = validate_input(url, 'url')
        if not is_valid:
            print(f"\n❌ Invalid URL Input: {error_message}")
            print("Please ensure you enter a valid URL (e.g., https://www.example.com)")
            return
        
        detected_issues = check_url(url)
        
    else:
        print("❌ Invalid choice. Please enter 'email' or 'url'.")
        return

    # Calculate risk score and level
    risk_score = calculate_risk_score(detected_issues)
    risk_level = calculate_risk_level(detected_issues)

    # Track this analysis in statistics
    global_stats.add_analysis(risk_level)

    # Get explanations
    explanations = get_explanations(detected_issues)

    # Display results
    print("\n" + "=" * 50)
    print("📊 PHISHING DETECTION REPORT")
    print("=" * 50)
    print(f"🔍 Risk Score: {risk_score}/100")
    print(f"⚠️  Risk Level: {risk_level}")
    print("=" * 50)

    if detected_issues:
        print("\n🚨 Detected Issues:")
        for issue in detected_issues:
            print(f"  • {issue}")
        
        print("\n📚 Explanations:")
        for explanation in explanations:
            print(f"  {explanation}")
    else:
        print("\n✅ No suspicious indicators detected!")
        print("   This content appears safe, but always stay cautious.")

    # Display statistics
    print(global_stats.generate_ascii_chart())

    # Save to report
    with open("output/report.txt", "w") as f:
        f.write("=" * 50 + "\n")
        f.write("PHISHING DETECTION REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(f"Risk Score: {risk_score}/100\n")
        f.write(f"Risk Level: {risk_level}\n")
        f.write("=" * 50 + "\n")
        if detected_issues:
            f.write("\nDetected Issues:\n")
            for issue in detected_issues:
                f.write(f"  • {issue}\n")
            f.write("\nExplanations:\n")
            for explanation in explanations:
                f.write(f"  {explanation}\n")
        else:
            f.write("\nNo suspicious indicators detected.\n")

    print("\n" + "=" * 50)
    print("💡 Safety Tips:")
    print("  • Never click links from unsolicited emails")
    print("  • Verify sender identity through official channels")
    print("  • Check for HTTPS and security indicators")
    print("  • Be suspicious of urgent requests for sensitive info")
    print("=" * 50)
    print("\n✅ Analysis saved to output/report.txt\n")


def gui_mode():
    """Launch the GUI interface."""
    try:
        from gui import main
        main()
    except ImportError as e:
        print("❌ Error: Could not import GUI module.")
        print(f"   Details: {e}")
        sys.exit(1)


def main():
    """Main entry point - allow user to choose interface mode."""
    print("\n" + "=" * 50)
    print("🔒 PHISHING DETECTION AWARENESS TOOL")
    print("=" * 50)
    print("\nChoose your interface:")
    print("  [1] Console Mode (original)")
    print("  [2] GUI Mode (Tkinter interface) 🖥️")
    print("  [0] Exit")
    print("=" * 50)
    
    choice = input("\nEnter your choice (0-2): ").strip()
    
    if choice == "1":
        console_mode()
    elif choice == "2":
        gui_mode()
    elif choice == "0":
        print("👋 Goodbye! Stay safe online!")
        sys.exit(0)
    else:
        print("❌ Invalid choice. Please enter 0, 1, or 2.")
        sys.exit(1)

if __name__ == "__main__":
    main()
