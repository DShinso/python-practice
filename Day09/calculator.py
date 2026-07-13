def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b
    elif operator == '%':
        return a % b
    elif operator == '**':
        return a ** b
    else:
        return "Error: Invalid operator"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 0, "/"))
print(calculator(10, 3, "%"))
print(calculator(2, 5, "**"))