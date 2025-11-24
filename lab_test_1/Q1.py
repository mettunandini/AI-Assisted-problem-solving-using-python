import time

# Implementations
def reverse_slicing(lst):
    return lst[::-1]

def reverse_builtin(lst):
    return list(reversed(lst))

def reverse_loop(lst):
    result = []
    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    return result

def reverse_recursion(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_recursion(lst[:-1])

# Test data
large_list = list(range(10000))

# Performance comparison for large list
functions = [reverse_slicing, reverse_builtin, reverse_loop]

for func in functions:
    start = time.time()
    func(large_list)
    end = time.time()
    print(f"{func.__name__}: {end - start:.6f} seconds")

# Recursion is inefficient for large lists, so test with smaller list
small_list = list(range(100))
start = time.time()
reverse_recursion(small_list)
end = time.time()
print(f"reverse_recursion (small list): {end - start:.6f} seconds")
