def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

num = int(input("Enter a number: "))

print("Iterative:", factorial_iterative(num))
print("Recursive:", factorial_recursive(num))