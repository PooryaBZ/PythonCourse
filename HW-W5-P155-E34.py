numbers_array = []

# 20 inputs with an array
for n in range(20):
    number = float(input("Please input a number: "))
    numbers_array.append(number)

print("numbers: ", numbers_array) # Printing numbers
print("min: ", (min(numbers_array))) # Calculating and printing minimum number
print("max: ", (max(numbers_array))) # Calculating and printing maximum number
print("sum: ", sum(numbers_array)) # Calculating and printing sum of numbers
print("average: ", sum(numbers_array)/len(numbers_array)) # Calculating and printing average of numbers