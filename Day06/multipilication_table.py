number = int(input("Enter a Number: "))

print("======= MULTIPLICATION TABLE =======")
print(" ")

for i in range(1, 11):
    a = number * i
    print(number, "*", i, "=", a)

print(" ")
print("================================")