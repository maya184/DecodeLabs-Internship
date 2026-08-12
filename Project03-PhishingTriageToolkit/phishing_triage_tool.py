"""
DecodeLabs Cyber Security - Project 3
Phishing Awareness Analysis: Email/Message Triage Tool

Goal: Analyze a sample email or message to detect common phishing
red flags, and classify it as Safe, Suspicious, or Malicious
using the decision tree model taught in the training material:

    Incoming Message -> Safe   -> Close
                      -> Suspicious -> Warn User
                      -> Malicious  -> Block & Escalate

Key Skills demonstrated: threat analysis, pattern recognition,
security decision-making logic.
"""

import re

# --- Red Flag Keyword Banks (based on the DecodeLabs training slides) ---

URGENCY_PHRASES = [
    "act now", "immediate action required", "urgent", "account locked",
    "24 hours", "expires today", "final notice", "verify immediately",
    "suspended", "click immediately", "within 30 minutes",
]

AUTHORITY_PHRASES = [
    "it security", "human resources", "law enforcement", "irs",
    "strictly confidential", "ceo", "executive", "do not discuss",
    "bypass standard procedure",
]

SENSITIVE_INFO_REQUESTS = [
    "verify your password", "confirm your ssn", "enter your otp",
    "mfa code", "update billing", "payment details", "wire transfer",
    "bank account number", "social security number", "one-time code",
]

DANGEROUS_ATTACHMENT_EXTENSIONS = [".exe", ".scr", ".js", ".iso", ".vbs", ".bat"]

# Common brand names often impersonated (used to detect lookalike domains)
COMMONLY_SPOOFED_BRANDS = ["amazon", "paypal", "microsoft", "google", "apple", "netflix"]


def find_matches(text: str, phrase_list: list) -> list:
    """Return the phrases from phrase_list that appear in text (case-insensitive)."""
    text_lower = text.lower()
    return [phrase for phrase in phrase_list if phrase in text_lower]


def extract_urls(text: str) -> list:
    """Extract URLs / domain-like strings from the message text."""
    url_pattern = r'(?:https?://)?(?:www\.)?[\w-]+\.[a-z]{2,}(?:/[^\s]*)?'
    return re.findall(url_pattern, text, flags=re.IGNORECASE)


def check_lookalike_domain(url: str) -> bool:
    """
    Basic typosquatting/lookalike check: flags a URL if it contains a
    known brand name but is NOT that brand's actual official domain.
    (A real triage tool would use a verified domain allow-list; this is
    a simplified version for demonstration/training purposes.)
    """
    url_lower = url.lower()
    official_domains = {
        "amazon": "amazon.com",
        "paypal": "paypal.com",
        "microsoft": "microsoft.com",
        "google": "google.com",
        "apple": "apple.com",
        "netflix": "netflix.com",
    }
    for brand in COMMONLY_SPOOFED_BRANDS:
        if brand in url_lower and official_domains[brand] not in url_lower:
            return True
    return False


def check_attachment(filename: str) -> bool:
    """Return True if the attachment has a dangerous file extension."""
    return any(filename.lower().endswith(ext) for ext in DANGEROUS_ATTACHMENT_EXTENSIONS)


def analyze_message(text: str, sender_email: str = "", attachment: str = "") -> dict:
    """
    Run the full triage analysis on a message.
    Returns a dict with the verdict, red flags found, and recommended action.
    """
    red_flags = []

    # --- Check 1: Urgency / fear triggers ---
    urgency_hits = find_matches(text, URGENCY_PHRASES)
    if urgency_hits:
        red_flags.append(f"Urgency/fear language detected: {', '.join(urgency_hits)}")

    # --- Check 2: Authority impersonation ---
    authority_hits = find_matches(text, AUTHORITY_PHRASES)
    if authority_hits:
        red_flags.append(f"Authority impersonation language: {', '.join(authority_hits)}")

    # --- Check 3: Requests for sensitive information ---
    sensitive_hits = find_matches(text, SENSITIVE_INFO_REQUESTS)
    if sensitive_hits:
        red_flags.append(f"Sensitive info request detected: {', '.join(sensitive_hits)}")

    # --- Check 4: Suspicious/lookalike URLs ---
    urls = extract_urls(text)
    suspicious_urls = [u for u in urls if check_lookalike_domain(u)]
    if suspicious_urls:
        red_flags.append(f"Lookalike/spoofed domain(s) found: {', '.join(suspicious_urls)}")

    # --- Check 5: Sender-domain mismatch (very basic heuristic) ---
    if sender_email:
        display_name_brands = [b for b in COMMONLY_SPOOFED_BRANDS if b in text.lower()[:200]]
        for brand in display_name_brands:
            official = brand + ".com"
            if official not in sender_email.lower():
                red_flags.append(
                    f"Sender domain mismatch: message references '{brand}' "
                    f"but sender is '{sender_email}'"
                )
                break

    # --- Check 6: Dangerous attachment ---
    if attachment and check_attachment(attachment):
        red_flags.append(f"Dangerous attachment type: {attachment}")

    # --- Decision Tree: classify based on number/severity of red flags ---
    has_critical_flag = any(
        "attachment" in f or "domain" in f.lower() or "mismatch" in f.lower()
        for f in red_flags
    )

    if not red_flags:
        verdict = "Safe"
        action = "Close (no action needed)"
    elif has_critical_flag:
        verdict = "Malicious"
        action = "Block & Escalate to IT/Security team"
    else:
        verdict = "Suspicious"
        action = "Warn User -- advise caution, do not click links or reply"

    return {
        "verdict": verdict,
        "action": action,
        "red_flags": red_flags,
    }


def print_report(result: dict) -> None:
    """Pretty-print the triage result."""
    print("\n--- Triage Report ---")
    print(f"Verdict        : {result['verdict']}")
    print(f"Recommended Action: {result['action']}")
    if result["red_flags"]:
        print("Red Flags Found:")
        for flag in result["red_flags"]:
            print(f"  - {flag}")
    else:
        print("Red Flags Found: None")
    print("----------------------\n")


def main():
    print("=== DecodeLabs Phishing Triage Tool ===")
    print("Paste the message text to analyze it for phishing red flags.\n")

    while True:
        text = input("Enter message text (or 'exit' to quit): ")
        if text.lower() == "exit":
            print("Goodbye!")
            break
        if text == "":
            print("Please enter some message text.\n")
            continue

        sender = input("Enter sender email (optional, press Enter to skip): ")
        attachment = input("Enter attachment filename (optional, press Enter to skip): ")

        result = analyze_message(text, sender, attachment)
        print_report(result)


if __name__ == "__main__":
    main()
