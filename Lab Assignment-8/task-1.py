def is_valid_email(email: str) -> bool:
    """
    Validate email based on:
    1. Must contain @ and .
    2. Must not start or end with special characters.
    3. Should not allow multiple @.
    """
    special_chars = "@._-"

    # Check basic requirements
    if '@' not in email or '.' not in email:
        return False

    # Must not start or end with special characters
    if email[0] in special_chars or email[-1] in special_chars:
        return False

    # Should not allow multiple '@'
    if email.count('@') != 1:
        return False

    # Split username and domain
    username, domain = email.split('@')
    
    # Username and domain should not be empty
    if not username or not domain:
        return False

    # Domain must contain a dot and not start/end with dot
    if '.' not in domain or domain[0] == '.' or domain[-1] == '.':
        return False

    # Ensure only valid characters are used
    for ch in email:
        if not (ch.isalnum() or ch in special_chars):
            return False

    return True


# --- AI-generated test cases ---
test_cases = {
    # ✅ Valid
    "alex.smith@domain.com": True,
    "user_99@sub.domain.co": True,
    "john-doe@company.io": True,
    "example@data.net": True,

    # ❌ Invalid
    "noatsymbol.com": False,        # Missing @
    "nodot@domain": False,          # Missing .
    ".start@domain.com": False,     # Starts with special
    "end.@domain.com": False,       # Ends with special
    "two@@domain.com": False,       # Multiple @
    "user@.domain.com": False,      # Domain starts with dot
    "user@domain.com.": False,      # Domain ends with dot
    "@missinguser.com": False,      # Missing username
    "missingdomain@": False,        # Missing domain
    "bad space@domain.com": False,  # Invalid space char
}


def run_tests():
    print("=== Running Email Validator Tests ===\n")
    passed = 0
    failed = 0
    for email, expected in test_cases.items():
        result = is_valid_email(email)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"{status}: {email} -> Expected: {expected}, Got: {result}")
        if result == expected:
            passed += 1
        else:
            failed += 1
    print(f"\nSummary: {passed} Passed, {failed} Failed\n")


if __name__ == "__main__":
    run_tests()
