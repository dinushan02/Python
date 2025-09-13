# Nested for loop to print a square pattern
"""size = 5

for i in range(size): # Outer loop for rows
    for j in range(size): # Inner loop for columns
        print("*", end = " ") # Print star without moving to the next line
    print() # Move to the next line after each row"""

#Hollow square pattern
"""size = 5 # size of the square

for i in range(size):
    for j in range(size): # 0 1 2 3 4(size - 1)
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")

    print()"""

# Pyramid Pattern
"""rows = 5  # Number of rows

for i in range(1, rows + 1):
    # print leading spaces
    print(" " * (rows - i), end="")

    # print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()  # move to next line"""

# Inverted Pyramid pattern
"""rows = 5

for i in range(rows, 0, -1):
    # spaces increase as rows decrease
    print(" " * (rows - i), end=" ")

    # stars decrease with each row
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()"""

# Diamond Pattern
rows = 5

# Upper half
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # no extra space
    for j in range(2 * i - 1):
        print("*", end="")
    print()  # new line

# Lower half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


















