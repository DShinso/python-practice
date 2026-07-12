secret = 4

user_guess = int(input("Guess a number: "))

while user_guess != secret:
    if user_guess < secret:
        user_guess = int(input("Guess a number: "))

    elif user_guess > secret:
        user_guess = int(input("Guess a number: "))

print("Congratulations! You guessed the number!")