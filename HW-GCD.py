# First we need two inputs

Num1 = int(input("Enter the First number "))
Num2 = int(input("Enter the Second number "))
# Then we need Third variable for GCD
GCD = 0
# Now we should compare our inputs to find the small one between them and if they are same print one of inputs as result

if Num1 > Num2:
    GCD = Num2
elif Num2 > Num1:
    GCD = Num1
elif Num2 == Num1:
    print("GCD =", end=" ")
    print(Num2)

# Finally , we should write a loop with downward trend to find the Greatest common divisor

while GCD >= 1:
    if Num1 % GCD == 0 and Num2 % GCD == 0:
        print("GCD =", end=" ")
        print(GCD)
        break
    GCD = GCD - 1
