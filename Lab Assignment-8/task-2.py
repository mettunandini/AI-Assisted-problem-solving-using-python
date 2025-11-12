def assign_grade(score):
    """
    Assign a grade based on numeric score.
    90-100: A
    80-89:  B
    70-79:  C
    60-69:  D
    <60:    F
    Handles invalid and out-of-range inputs.
    """
    # Validate input type
    if not isinstance(score, (int, float)):
        return "Invalid Input"

    # Validate score range
    if score < 0 or score > 100:
        return "Invalid Input"

    # Assign grade based on range
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"


# --- AI-GENERATED TEST CASES (Including Boundary and Invalid Inputs) ---
test_cases = {
    # ✅ Valid typical cases
    95: "A",   # within A range
    85: "B",   # within B range
    75: "C",   # within C range
    65: "D",   # within D range
    50: "F",   # below 60

    # 🧩 Boundary cases
    100: "A",  # upper boundary
    90: "A",   # lower A boundary
    89: "B",   # upper B boundary
    80: "B",   # lower B boundary
    79: "C",   # upper C boundary
    70: "C",   # lower C boundary
    69: "D",   # upper D boundary
    60: "D",   # lower D boundary
    59: "F",   # just below D range
    0: "F",    # lower extreme

    # ❌ Invalid / unexpected inputs
    -5: "Invalid Input",         # negative score
    105: "Invalid Input",        # above 100
    "eighty": "Invalid Input",   # string input
    None: "Invalid Input",       # NoneType
    72.5: "C",                   # valid float in range
}


def run_tests():
    print("=== Running Grade Assignment Tests ===\n")
    passed = 0
    failed = 0
    for score, expected in test_cases.items():
        result = assign_grade(score)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"{status}: Input: {score} -> Expected: {expected}, Got: {result}")
        if result == expected:
            passed += 1
        else:
            failed += 1
    print(f"\nSummary: {passed} Passed, {failed} Failed\n")


if __name__ == "__main__":
    run_tests()
