"""
calculator_module.py

This module provides basic calculator operations:
addition, subtraction, multiplication, and division.

You can use this module directly or import its functions
into another Python file.
"""

# -----------------------------
# Manual NumPy-style docstrings
# -----------------------------

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Sum of a and b.

    Examples
    --------
    >>> add(2, 3)
    5
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from the first.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Result of a - b.

    Examples
    --------
    >>> subtract(5, 3)
    2
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Product of a and b.

    Examples
    --------
    >>> multiply(2, 3)
    6
    """
    return a * b


def divide(a, b):
    """
    Divide first number by the second.

    Parameters
    ----------
    a : float
        Numerator.
    b : float
        Denominator.

    Returns
    -------
    float
        Result of a / b.

    Raises
    ------
    ValueError
        If b is zero.

    Examples
    --------
    >>> divide(6, 2)
    3.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# -----------------------------
# Example usage / Test section
# -----------------------------
if __name__ == "__main__":
    print("Add:       ", add(5, 3))
    print("Subtract:  ", subtract(5, 3))
    print("Multiply:  ", multiply(5, 3))
    print("Divide:    ", divide(6, 3))


# -----------------------------
# Example AI-generated docstring (for comparison)
# -----------------------------
"""
Calculator Module

This module provides arithmetic operations: add, subtract, multiply, and divide.

Functions
---------
add(a, b): Return the sum of two numbers.
subtract(a, b): Return the result of subtracting b from a.
multiply(a, b): Return the product of two numbers.
divide(a, b): Return the result of dividing a by b.
"""
