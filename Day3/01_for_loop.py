#for loop

# Syntax:
# for variable in range():
#     statement

# range(stop)
# Starts from 0
# Stops before stop

# range(start, stop)
# Starts from start
# Stops before stop

# range(start, stop, step)
# Starts from start
# Stops before stop
# Increases or decreases by step


# ----------------------------
# Program 1 - Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

print("----------------------------")


# ----------------------------
# Program 2 - Print numbers from 10 to 1

for i in range(10, 0, -1):
    print(i)

print("----------------------------")


# ----------------------------
# Program 3 - Print even numbers from 2 to 20

for i in range(2, 21, 2):
    print(i)

print("----------------------------")


# ----------------------------
# Program 4 - Print odd numbers from 1 to 19

for i in range(1, 20, 2):
    print(i)

print("----------------------------")


# ----------------------------
# Program 5 - Print multiples of 5 from 5 to 50

for i in range(5, 51, 5):
    print(i)

print("----------------------------")


# ----------------------------
# Program 6 - Print multiples of 5 from 50 to 5

for i in range(50, 4, -5):
    print(i)