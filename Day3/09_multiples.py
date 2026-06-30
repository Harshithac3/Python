limit = int(input("Enter the limit:"))
multiple = int(input("Enter a number for which you need to find multiples:"))
for i in range(multiple, limit + 1, multiple):
    print(i)
