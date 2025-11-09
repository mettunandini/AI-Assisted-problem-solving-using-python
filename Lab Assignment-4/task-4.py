def count_vowels(text):
    """
    Counts the number of vowels (a, e, i, o, u) in a string.
    The function is case-insensitive.
    Example: 'Hello World' -> 3
    """
    vowels = "aeiou"
    count = 0
    
    # Convert text to lowercase to make it case-insensitive
    for char in text.lower():
        if char in vowels:
            count += 1
            
    return count


# Example usage:
print(count_vowels("Hello World"))     # Output: 3
print(count_vowels("Python"))          # Output: 1
print(count_vowels("AEIOU"))           # Output: 5
print(count_vowels("ChatGPT"))         # Output: 1

