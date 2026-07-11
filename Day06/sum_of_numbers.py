number = int(input("Enter a number: "))

total = 0

for i in range(1, number + 1):

    total += i

    if i == number:
        print(i, end="")

    else:
        print(i, "+ ", end="")

print(" =", total)