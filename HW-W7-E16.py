def count_evens(lst):
    lst2 = []
    for i in lst:
        if i % 2 == 0:
            lst2 += [i]
    return len(lst2)
lst = [1 , 2, 4, 5, 6, 8]
print(count_evens(lst))