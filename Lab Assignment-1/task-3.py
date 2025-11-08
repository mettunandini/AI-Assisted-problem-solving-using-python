def reverse_string(input_string: str) -> str:
	"""
	Reverses the given input string.
    
	Args:
		input_string (str): The string to be reversed
        
	Returns:
		str: The reversed string
        
	Examples:
		>>> reverse_string("hello")
		'olleh'
		>>> reverse_string("Python")
		'nohtyP'
	"""
	return input_string[::-1]

def main():
	user_string = input("Enter a string to reverse: ")
	result = reverse_string(user_string)
	print(f"Original string: {user_string}")
	print(f"Reversed string: {result}")

if __name__ == "__main__":
	main()