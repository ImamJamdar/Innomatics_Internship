# Task 5: Error message Detector

logs = ["INFO", "ERROR", "WARNING", "ERROR",]

error_count = 0

# logic for checking and counting error msg
for log in logs:
    if log == "ERROR":
        error_count +=1

print("Total ERROR Count:", error_count)