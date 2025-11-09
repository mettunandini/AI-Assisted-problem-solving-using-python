def is_palindrome(text):
    """
    Checks if the given text is a palindrome.
    A palindrome reads the same backward as forward.
    """
    # Remove spaces and convert to lowercase for comparison
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


# ===== Example Usage =====
if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")

    if is_palindrome(user_input):
        print(" It's a palindrome!")
    else:
        print(" Not a palindrome.")