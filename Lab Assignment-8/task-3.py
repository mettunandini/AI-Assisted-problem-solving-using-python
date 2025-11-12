import string

def is_sentence_palindrome(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.
    Ignores case, punctuation, and spaces.
    """
    if not isinstance(sentence, str):
        return False

    # Remove spaces and punctuation, convert to lowercase
    cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())

    # Check palindrome
    return cleaned == cleaned[::-1]


# --- 🤖 AI-GENERATED TEST CASES ---

test_cases = {
    # ✅ True (Valid Palindromes)
    "A man a plan a canal Panama": True,            # classic example
    "Was it a car or a cat I saw": True,            # phrase palindrome
    "No lemon, no melon": True,                     # punctuation ignored
    "Able was I ere I saw Elba": True,              # case insensitive
    "Madam In Eden, I’m Adam": True,                # punctuation + case ignored
    "Step on no pets": True,                        # simple palindrome
    "": True,                                       # empty string counts as palindrome
    "  ": True,                                     # spaces only

    # ❌ False (Not Palindromes)
    "Hello World": False,                           # normal text
    "Python Programming": False,                    # non-palindrome
    "Was it a dog or a cat I saw": False,           # slight change breaks it
    "No lemon, just melon": False,                  # close but not palindrome
    "This is not a palindrome": False,

    # 🧩 Edge & invalid cases
    None: False,                                    # invalid type
    12321: False,                                   # non-string input
    "12321": True,                                  # numeric string palindrome
    "123421": False,                                # numeric string not palindrome
    "Madam!": True,                                 # punctuation ignored
}


def run_tests():
    print("=== Running Sentence Palindrome Tests ===\n")
    passed = 0
    failed = 0
    for sentence, expected in test_cases.items():
        result = is_sentence_palindrome(sentence)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"{status}: Input: {repr(sentence)} -> Expected: {expected}, Got: {result}")
        if result == expected:
            passed += 1
        else:
            failed += 1

    print(f"\nSummary: {passed} Passed, {failed} Failed\n")


if __name__ == "__main__":
    run_tests()
