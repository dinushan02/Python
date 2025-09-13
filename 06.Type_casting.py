a = 10
print(a)          # Prints the value of 'a' (10)
print(type(a))    # Prints the type of 'a' (<class 'int'>)

b = int(a)        # Converts 'a' to an integer (which is already an int)
print(b)
print(type(b))    # Still an integer

a = 16.0          # Assigning a float value to 'a'
print(a)
print(type(a))    # Prints <class 'float'>

a = int(input("Enter The value of A : "))  # Takes integer input from the user
b = int(input("Enter The value of B : "))  # Takes another integer input
c = a + b  # Adds two integers

# print("Total : " + str(c))
# Using '+' for concatenation requires 'c' to be converted to a string

print("Total : ", c)
# The comma (,) automatically separates values with a space and handles integers directly.

#Using + for concatenation requires converting the integer c into a string:
#print("Total : " + str(c))

#Using a comma (,) in print() is easier:
#print("Total : ", c)

#It automatically adds a space between "Total : " and c.
#You don't need to convert c into a string.
#It works with different data types (string, integer, float, etc.).