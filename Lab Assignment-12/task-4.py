# Gradient Descent to approximate minimum of f(x) = 2x^3 + 4x + 5
def f(x):
    return 2*x**3 + 4*x + 5

def df(x):
    return 6*x**2 + 4  # derivative

# Initialization
x = 0.0             # starting point
learning_rate = 0.01
iterations = 1000
lower_bound = -1e6   # avoid overflow

# Gradient descent loop
for i in range(iterations):
    grad = df(x)
    x = x - learning_rate * grad
    if x < lower_bound:
        print("Reached lower bound to avoid overflow.")
        break

print("Approximate x at minimum (within bounds):", x)
print("Approximate minimum value of f(x):", f(x))
