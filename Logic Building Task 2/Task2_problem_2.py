# problem 2: Highest Salary from Employee Data

# given input

employees = {
    "Ironman": 75000,
    "Spiderman": 68000,
    "Hulk": 72000
}

highest_employee = None
highest_salary = 0

# logic for finding the employee with the highest salary
for name, salary in employees.items():
    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

print(f"The employee with the highest salary is {highest_employee} with a salary of {highest_salary}.")