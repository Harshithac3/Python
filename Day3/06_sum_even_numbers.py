number = int(input("Enter a number:"))
sum = 0
for i in range (1, number + 1):
    if i % 2 == 0:
        sum = sum + i
print("Sum of Even numbers:",sum)