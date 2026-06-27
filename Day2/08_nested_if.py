pizza = input("Do you want Pizza? ").lower()
if pizza == "yes":
    cheese = input("Do you want extra Cheese? ").lower()
    if cheese == "yes":
        print("1 Extra Cheese Pizza")
    else:
        print("Ok! 1 Regular Pizza")
else:
    print("No Pizza Ordered.")
print("Thank you! Visit Again")