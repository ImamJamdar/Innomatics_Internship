# problem 9: Check if a key exists in a dictionary

# test dictionary
employee_id = {
    "Ironman": 101,
    "Spiderman": 102,
    "Hulk": 103,
    "Thor": 104
}

# taking input from user to check if the employee name exists in the dictionary
employee_name = input("Enter the employee name: ")

# checking if the employee name exists in the dictionary keys
for name in employee_id.keys():
    if name == employee_name:
        print(f"{employee_name} exists in the dictionary with employee ID: {employee_id[name]}")
        break
else:
    print(f"{employee_name} does not exist in the dictionary.")