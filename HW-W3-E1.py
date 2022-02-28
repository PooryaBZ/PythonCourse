# Actually i think there is a mistake in question because there is no tax rate for income between 4000 and 6000
income = int(input("How much is your income ?? "))

if 0 < income < 1000:
    afterReduction = income
    print("net income after tax reduction is", end=" ")
    print(afterReduction)
elif 1000 < income <= 2500:
    afterReduction = income - (income * 0.1)
    print("net income after tax reduction is", end=" ")
    print(afterReduction)
elif 2500 < income <= 4000:
    afterReduction = income - (income * 0.15)
    print("net income after tax reduction is", end=" ")
    print(afterReduction)
elif 4000 < income <= 6000:
    afterReduction = income - (income * 0.2)
    print("net income after tax reduction is", end=" ")
    print(afterReduction)
elif 6000 < income <= 8000:
    afterReduction = income - (income * 0.25)
    print("net income after tax reduction is", end=" ")
    print(afterReduction)
elif  income < 8000:
    afterReduction = income - (income * 0.3)
    print("net income after tax reduction is", end=" ")
    print(afterReduction)
else:
    print("error")