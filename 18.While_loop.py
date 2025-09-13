i = 1  # Start from 1

while i <= 10:  # Continue until 10
    print(i)
    i += 1  # Increment by 1


print("-----------------------------")

print("Even No: ")
i = 2  # Start from 2
while i <= 20:  # Continue to 20
    print(i)
    i += 2  # Increment by 2

"""
Since you know Python basics and loops, here are some beginner-friendly 
real-world projects you can build using while loops:

1. Number Guessing Game 🎯
#The program picks a random number, and the user has to guess it.
#Use a while loop to keep asking until the user gets it right.
#Use random.randint() to generate a number.

2. Simple ATM Simulator 💳
#Let the user check balance, deposit, or withdraw money.
#Use a while loop to keep showing the menu until they exit.

3. Even & Odd Number Sorter 🔢
#Ask the user for a range of numbers.
#Use a while loop to separate even and odd numbers.

4. Basic Password System 🔐
#Set a correct password.
#Keep asking for the password in a while loop until the user enters it correctly.

5. Multiplication Table Generator 🏫
#Let the user enter a number.
#Use a while loop to print its multiplication table.
"""
print("-----------------------------")

#To print the words "one", "two", "three" using a while loop in Python,
#you can use a list and iterate through it with an index. Here's a simple example:
# Define a list of words to be printed
print("🧑🏿‍💻Choose one that you wish:")
words = ["Python", "C", "C#"]

# Initialize a counter variable
i = 0

# Start a while loop that runs until the counter reaches the length of the list
while i < len(words):
    # Print the current word from the list
    print(words[i])

    # Increment the counter to move to the next word
    i += 1



