# If-Else statement with emojis
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    msg = f"🎉 Hi {name}, you are {age} years old. Congratulations! You are eligible to vote. 🗳️✅"
else:
    msg = f"😞 Hi {name}, you are {age} years old. Sorry! You are not eligible to vote yet. ⏳❌"

print(msg)
