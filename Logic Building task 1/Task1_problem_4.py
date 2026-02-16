# Task 4: Message Length Analyzer

# Given message
msg = ["Hi", "Welcome to the platform", "OK"]

# Logic for checking the the length of each message and filteration
for m in msg:
    length = len(m)
    print("Message:",m, "\n Length:", length)

    # filtering messages having more than 10 characters
    if length > 10:
        print("Flag: Message is longer than 10 Characters")