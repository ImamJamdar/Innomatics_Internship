# Prbolem 3: Find Maximum and Minimum values

# Given list

numbers = [45,50,60,13,15,39,69,100]

maximum = numbers[0]
minimum = numbers[0]

# logic for finding the maximum and minimum values in the list
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(f"Numbers in the list: {numbers}")
print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")