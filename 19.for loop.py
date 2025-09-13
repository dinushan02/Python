"""print("This program lets you add two numbers, 5 times.\n")

for i in range(1, 6):  # start loop at 1 for better user readability
    print(f"--- Attempt {i} ---")

    # Using try-except to handle wrong inputs
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = a + b
        print(f"Result: {a} + {b} = {c}\n")
    except ValueError:
        print("❌ Invalid input! Please enter integers only.\n")
"""

# If you want to make it even more flexible, instead of running only 5 times,
# you can ask the user how many times they want:

times = int(input("How many times do you want to add numbers?: "))

for i in range(1, times + 1):
    print(f"--- Attempt {i} ---")
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"Result: {a} + {b} = {a + b}\n")
    except ValueError:
        print("❌ Invalid input! Please enter integers only.\n")
