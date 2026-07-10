age = int(input("Enter your age: "))
has_id = input("Do you have an ID? y/n: ")

if age >= 18 and has_id == "y":
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")