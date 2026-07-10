mark = int(input("Enter your mark: "))

if mark > 100:
    print("invaild mark")
elif mark < 0:
    print("invaild mark")
elif mark >= 90:
    print("A+")
elif mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 50:
    print("D")
else:
    print("Fail! ")