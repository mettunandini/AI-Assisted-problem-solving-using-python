
# age_classification.py
# Program to classify age groups using nested if-elif-else conditionals

def classify_age(age):
    """
    Classify a person's age into categories using nested conditionals.
    Categories:
      - Child (0–12)
      - Teenager (13–19)
      - Adult (20–59)
      - Senior Citizen (60+)
    """
    if age >= 0:  # outer condition to ensure valid input
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior Citizen"
    else:
        return "Invalid age entered. Age cannot be negative."


def main():
    print("=== Age Group Classification ===")
    try:
        age = int(input("Enter your age: "))
        category = classify_age(age)
        print(f"\nYou are classified as: {category}")
    except ValueError:
        print("Invalid input! Please enter a numeric value for age.")


if __name__ == "__main__":
    main()
