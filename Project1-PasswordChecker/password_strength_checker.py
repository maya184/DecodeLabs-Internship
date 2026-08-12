"""
DecodeLabs Cyber Security - Project 1
Password Strength Checker

Goal: Check whether a password is Weak, Medium, or Strong
based on length, character variety, and common-password checks.

Key Skills demonstrated: string handling, condition checks, security basics.
"""

# A small sample list of extremely common / leaked passwords.
# In a real-world tool this would come from a large breached-password
# database (e.g. "rockyou.txt" or the "Have I Been Pwned" API).
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "123123", "letmein", "iloveyou",
    "admin", "welcome", "monkey", "dragon", "football",
}


def check_password_strength(password: str) -> dict:
    """
    Analyze a password and return a dictionary with:
      - strength: "Weak", "Medium", or "Strong"
      - reasons: list of feedback messages explaining the score
    """
    reasons = []

    # --- Rule 1: Reject known common/leaked passwords immediately ---
    if password.lower() in COMMON_PASSWORDS:
        return {
            "strength": "Weak",
            "reasons": ["This password appears in a list of commonly leaked passwords."]
        }

    # --- Rule 2: Length check ---
    length = len(password)
    if length < 8:
        reasons.append("Too short (minimum 8 characters recommended).")
    elif length >= 12:
        reasons.append("Good length (12+ characters).")
    else:
        reasons.append("Acceptable length (8-11 characters).")

    # --- Rule 3: Character variety checks (Pythonic style, per the slides) ---
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    if not has_upper:
        reasons.append("Add at least one uppercase letter.")
    if not has_lower:
        reasons.append("Add at least one lowercase letter.")
    if not has_digit:
        reasons.append("Add at least one number.")
    if not has_symbol:
        reasons.append("Add at least one symbol (e.g. !@#$%).")

    # --- Score calculation ---
    variety_score = sum([has_lower, has_upper, has_digit, has_symbol])

    if length < 8:
        strength = "Weak"
    elif length >= 12 and variety_score == 4:
        strength = "Strong"
    elif length >= 8 and variety_score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return {"strength": strength, "reasons": reasons}


def print_result(password: str) -> None:
    """Pretty-print the result for a single password."""
    result = check_password_strength(password)
    print(f"\nPassword: {'*' * len(password)}")
    print(f"Strength: {result['strength']}")
    print("Feedback:")
    for reason in result["reasons"]:
        print(f"  - {reason}")


def main():
    print("=== DecodeLabs Password Strength Checker ===")
    print("Type a password to check its strength (type 'exit' to quit).\n")

    while True:
        pwd = input("Enter password: ")
        if pwd.lower() == "exit":
            print("Goodbye!")
            break
        if pwd == "":
            print("Please enter a non-empty password.")
            continue
        print_result(pwd)


if __name__ == "__main__":
    main()
