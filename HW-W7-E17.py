lst = [99, 1993, 1771, 3]
def print_big_enough(num):
    lst.sort()
    if num > lst[-1]:
        a = "big enough"
    else:
        a = "not big enough"
    return a

input1 = int(input("please enter a number: "))

print(print_big_enough(input1))