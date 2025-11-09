# Function to calculate the sum of first n natural numbers using a for loop

# sum_to_n.py
# Program to calculate the sum of first n natural numbers using loops

def sum_to_n(n):
    """
    Calculate the sum of the first n natural numbers using a for loop.
    Example: n=5 → 1+2+3+4+5 = 15
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def main():
    print("=== Sum of First N Natural Numbers ===")
    try:
        n = int(input("Enter a positive integer (n): "))
        if n <= 0:
            print("Please enter a number greater than zero.")
            return

        result = sum_to_n(n)
        print(f"\nSum of first {n} natural numbers is: {result}")

    except ValueError:
        print("Invalid input! Please enter an integer value.")


if __name__ == "__main__":
    main()

