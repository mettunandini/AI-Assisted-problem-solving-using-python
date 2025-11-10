def divide_numbers(a, b):
    try:
         return a / b
    except ZeroDivisionError:
         print("Error: Division by Zero is not allowed.")
         return None # or any safe deafault value
 
# Example usage
result = divide_numbers(10, 0)  #  safe handling
print(result)# Output: None



 

