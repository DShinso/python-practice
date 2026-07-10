username = "admin"
password = "1234"

entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

if username == entered_username:
    if password == entered_password:
        print("Welcome " + entered_username)
    else:
        print("Passwords do not match!")
else:
    print("User not found!")

