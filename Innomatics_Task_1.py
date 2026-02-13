#Task-1: User Login Check

#Given Credentials for login
username = "admin"
password = "1234"

#User inputs
entered_username = input("Enter Username: ")
entered_password = input("Enter Password: ")

#Logic in checking whether login credentials are correct or not
if username == entered_username and password == entered_password:
    print("Login Successful")
else:
    print("Invalid Credentials")