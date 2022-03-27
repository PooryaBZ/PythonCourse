
variable = 1

while variable < 10000:
    order = len(str(variable))
    result = 0
    temp = variable
    while temp > 0:
        digit = temp % 10
        result += digit ** order
        temp //= 10
    if variable == result:
        print(variable)
    variable = variable + 1
