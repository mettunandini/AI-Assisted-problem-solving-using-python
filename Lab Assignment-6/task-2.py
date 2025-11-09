# multiples.py
# This program prints the first 10 multiples of a number using a for loop.

def print_multiples(number):
    """
    Prints the first 10 multiples of a given number using a for loop.
    Example: If number = 5, prints 5, 10, 15, 20, ..., 50
    """
    print(f"First 10 multiples of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Example usage
num = int(input("Enter a number: "))
print_multiples(num)
