pin = 1234
balance = 50000

entered_pin = int(input("Enter PIN: "))

if entered_pin == pin:
    print("Login Successful")

    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your Balance is ₹",balance)

    elif choice == 2:
        print("Withdraw Selected")
        amount = int(input("Enter Amount:"))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Succesful!")
            print("Remaining Balance:", balance)
        else:
            print("insufficient Balance")

    elif choice == 3:
        print("Deposit Selected")
        amount = int(input("Enter Amount:"))
        balance = balance + amount
        print("Deposit Successful!")
        print("Current Balance is ₹",balance)

    elif choice == 4:
        print("Thank You! Visit Again.")

    else:
        print("Invalid Choice")

else:
    print("Wrong PIN")