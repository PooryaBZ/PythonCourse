lst = [-1, 7, 4, 6, 8, 0]

def sum_positive():
        result = 0
        for item in lst:
            if item > 0:
                result += item
        return result

print(sum_positive())