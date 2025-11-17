#Function docstrings (AI-generated examples):

def add(a, b):
    """
    Return the sum of two numbers.

    Parameters:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: Sum of a and b.
    """
    return a + b
def divide(a, b):
    """
    Return the result of dividing a by b.

    Parameters:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: Result of division.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
      #example Usage
     if __name__ == "__main__":
    print("Add: ", add(5, 3))
    print("Subtract: ", subtract(5, 3))