# Question 1 - Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
    if age >= 25:
        print("Eligible to contest election")
else:
    print("Not eligible to vote")  


# ----------------------------

# Question 2 - Login System

username = input("Enter Username:")

if username == "admin":
    password = input("Enter Password:")
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")


# ----------------------------

# Question 3 - Marks Checker

marks = int(input("enter your marks:"))
if marks >= 35:
    print("Pass")
    if marks >= 90:
        print("Outstanding")
    else:
        print("Good Job")
else:
    print("Better Luck Next Time")


# ----------------------------

# Question 4 - ATM Withdrawal

pin = 1234
balance = 5000
entered_pin = int(input("Enter Pin: "))
if entered_pin == pin:
    amount = int(input("Enter the withdrawal amount: "))
    if amount <= balance:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Wrong PIN")


# ----------------------------