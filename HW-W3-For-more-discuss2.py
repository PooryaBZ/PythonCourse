i = int(input("Please insert the first number "))
j = int(input("Please insert the second number "))
k = int(input("Please insert the third number "))

if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k :
        j = i
    else:
        i = k

print("i = ", i, "j = ", j, "k = ", k)







