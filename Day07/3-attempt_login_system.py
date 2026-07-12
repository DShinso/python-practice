username = "admin"
password = "1234"

attempt = 0
while attempt < 3:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    if entered_username == username and entered_password == password:
        print("Welcome")
        attempt = 4
    else:
        attempt += 1
        print("Wrong!")
        print("Attempts left: ", 3-attempt)

if attempt == 3:
    print("Account locked")