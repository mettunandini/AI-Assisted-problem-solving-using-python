def is_leap_year(year: int) -> bool:
    """
    Returns True if the given year is a leap year, otherwise False.
    A leap year is:
      - divisible by 4
      - but not divisible by 100, unless it is also divisible by 400
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    print("Leap Year Checker\n")
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("Invalid input! Please enter a valid year (e.g., 2024).")
        return

    if is_leap_year(year):
        print(f"{year} is a leap year ✅")
    else:
        print(f"{year} is not a leap year ❌")


if __name__ == "__main__":
    main()
