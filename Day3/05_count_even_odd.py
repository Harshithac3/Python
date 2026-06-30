number = int(input("Enter a number:"))
even = 0
odd = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even count=",even)
print("Odd count=",odd)