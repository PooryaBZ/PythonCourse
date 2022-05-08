lst = [1, 30, 16, 127]
def next_number():
    maximum = 0
    variable = 0
    for i in lst:
        if i > maximum:
            maximum = i

    for i in range(1 , maximum +1):
        if i not in lst:
            return i


print(next_number())