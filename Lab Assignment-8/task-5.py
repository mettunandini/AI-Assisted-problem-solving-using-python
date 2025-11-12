from datetime import datetime

def convert_date_format(date_str: str) -> str:
    """Convert 'YYYY-MM-DD' to 'DD-MM-YYYY', or return 'Invalid Date'."""
    if not isinstance(date_str, str):
        return "Invalid Date"
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        return "Invalid Date"

# 🤖 AI-Generated Test Cases
test_cases = {
    "2023-10-15": "15-10-2023",
    "2000-01-01": "01-01-2000",
    "2024-02-29": "29-02-2024",
    "2023-13-01": "Invalid Date",
    "15-10-2023": "Invalid Date",
    "abcd-ef-gh": "Invalid Date",
    "9999-12-31": "31-12-9999",
    None: "Invalid Date"
}

def run_tests():
    print("=== Date Conversion Tests ===")
    passed, failed = 0, 0
    for d, expected in test_cases.items():
        result = convert_date_format(d)
        print(f"{'✅ PASS' if result == expected else '❌ FAIL'}: {repr(d)} -> {result}")
        if result == expected: passed += 1
        else: failed += 1
    print(f"\nSummary: {passed} Passed, {failed} Failed\n")

if __name__ == "__main__":
    run_tests()
