balance = 5000
choice = 0

while choice < 4:
    print("===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    selection = int(input("Enter your choice: "))
    choice = selection

    if choice == 1:
        print("Your Balance is: ","₹",balance)
    elif choice == 2:
        deposit_money = int(input("Enter your deposit amount: "))
        balance = balance + deposit_money
        print("New Balance is: ",balance)
    elif choice == 3:
        withdraw_money = int(input("Enter your withdraw amount: "))
        if withdraw_money <= balance:
            balance = balance - withdraw_money
            print("Withdraw Successful! ")
            print("Remaining Balance : ",balance)
        else:
            print("insufficient Balance")

print("Thank you for using our ATM!")