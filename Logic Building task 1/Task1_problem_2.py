# Task 2: Pass / Fail Analyzer

# Given list of marks
marks = [45,78,90,33,60]

# Logic
pass_count = 0
fail_count = 0

for m in marks:
    if m >= 50:
        pass_count += 1
    else:
        fail_count += 1

# Printing the result
print("Total Pass Students: ", pass_count)
print("Total Fail Students: ", fail_count)