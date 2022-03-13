
# the problem of the code was the gap line 10 the operation of this line belongs to 2nd while loop not if clause

# here is the true code:

MAX = 24
n = 1

while n <= MAX:
    factor = 1
    print(end=str(n) + ': ')
    while factor <= n:
        if n % factor == 0:
            print(factor, end=' ')
        factor += 1
    print()
    n += 1
