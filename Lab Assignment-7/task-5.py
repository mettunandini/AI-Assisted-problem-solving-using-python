numbers = [1, 2, 3]

index = 5

# Safe access check
if index < len(numbers):
    print(numbers[index])
else:
    print("Error: Index out of range. The list has only", len(numbers), "items.")