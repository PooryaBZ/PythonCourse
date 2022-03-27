import math

x = math.radians(float(input("please input a number ")))

def sin(x: float, N: int = 10):
    result = 0
    for n in range(N):
        result += ((-1) ** n * x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result

if __name__ == '__main__':
    print(sin(x))
    