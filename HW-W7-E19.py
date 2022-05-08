lst = [9, 5, 6, 'apple']
def reverse():
    reverseLST = lst[::-1]
    return reverseLST

def reverse2():
    lst.reverse()
    return lst

print(reverse())
print(reverse2())