# The function
def f(x):
    return x ** 3 - x ** 2 + 2

# Derivative of the function
def df(x):
    return 3 * x ** 2 - 2 * x

# Finding and printing the root
def nr(x):
    h = f(x) / df(x)
    while abs(h) >= 0.000000001:
        h = f(x) / df(x)
        x = x - h
    print(x)

# Test
x0 = 12
nr(x0)