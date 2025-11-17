# Manual docstring version
def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a list.

    This function takes a list of integers and returns a tuple containing
    the sum of even numbers and the sum of odd numbers.

    Args:
        numbers (list of int): A list containing integer values.

    Returns:
        tuple: A tuple of two integers:
            - sum_even (int): Sum of all even numbers in the list.
            - sum_odd (int): Sum of all odd numbers in the list.

    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)
    """
    sum_even = sum(num for num in numbers if num % 2 == 0)
    sum_odd = sum(num for num in numbers if num % 2 != 0)
    return sum_even, sum_odd


# Example usage
numbers = [10, 15, 20, 25, 30]
even_sum, odd_sum = sum_even_odd(numbers)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")


# Example AI-generated docstring for comparison (you can use Copilot to generate this)
"""
Returns the sum of even and odd numbers from a list.

Given a list of integers, this function separates the numbers into
even and odd, computes their sums, and returns both sums as a tuple.

Args:
    numbers (list): List of integers to process.

Returns:
    tuple: (sum_of_even_numbers, sum_of_odd_numbers)
"""
