# Problem 5: Calculate attendance percentage

# list of attendance records where "P" stands for present and "A" stands for absent
attendance = ["P","A","P","P","A","P","P","P","A","P"]

present_count = 0
total_days = len(attendance)

for status in attendance:
    if status == "P":
        present_count += 1

attendance_percentage = (present_count / total_days) * 100

print(f"Total attendance: {total_days}")
print(f"Present count: {present_count}")
print(f"Attendance percentage: {attendance_percentage:.2f}%")