# Problem 6: Remove Duplicate Phone Numbers

# list of phone numbers with duplicates

phone_numbers = ["1234567890", "9876543210", "1234567890", "5555555555", "5276543210","5555555555"]

# converting list into set because set does not allow duplicates
unique_phone_numbers = set(phone_numbers)

print("Unique phone numbers:", unique_phone_numbers)