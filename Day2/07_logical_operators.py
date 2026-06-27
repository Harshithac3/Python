#and operator
attendance = int(input("Enter Attendance: "))
cgpa = float(input("Enter CGPA: "))

if attendance >= 75 and cgpa >= 7.5:
    print("Eligible for Placements")
else:
    print("Not Eligible")
#or operator
sports = input("Are you a sports winner? (yes/no): ").lower()

if sports == "yes" or cgpa >= 9.0:
    print("Scholarship")
else:
    print("No Scholarship")
#not operator
account = input("Is your account active? (yes/no): ").lower()
account_active = (account == "yes")
if not account_active:
    print("Please activate your account")
else:
    print("Welcome!")