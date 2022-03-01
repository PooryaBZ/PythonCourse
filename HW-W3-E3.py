input1 = int(input("please enter a number : "))
input2 = int(input("please enter a number : "))
input3 = int(input("please enter a number : "))
input4 = int(input("please enter a number : "))
input5 = int(input("please enter a number : "))

if input1 == input2 or input1 == input3 or input1 == input4 or input1 == input5:
    print("Duplicate")
elif input2 == input3 or input2 == input4 or input2 == input5 or input3 == input4 or input3 ==input5 or input4 == input5:
    print("Duplicate")
else:
    print("All unique")