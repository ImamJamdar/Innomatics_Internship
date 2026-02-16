# Task 3: Simple Data Cleaner

# Given list 
names = [" Alice ", "bob", " CHARLIE "]

# Empty list to store cleaned list 
cleaned_names = []

for name in names:
    cleaned_name = name.strip().lower()
    cleaned_names.append(cleaned_name)

# printing cleaned list of names
print(cleaned_names)

