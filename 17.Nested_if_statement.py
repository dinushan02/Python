def get_valid_mark(subject):
    """Function to ensure valid input between 0 and 100"""
    while True:
        try:
            mark = int(input(f"📚 Enter {subject} Marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("⚠️ Marks must be between 0 and 100. Try again!")
        except ValueError:
            print("❌ Invalid input! Please enter a number between 0 and 100.")

# Get marks with validation
m1 = get_valid_mark("Mark-1")
m2 = get_valid_mark("Mark-2")
m3 = get_valid_mark("Mark-3")

# Calculate total and average
total = m1 + m2 + m3
average = round(total / 3, 2)

# Display results
print("\n📊 Results:")
print(f"📌 Total Marks: {total}")
print(f"📌 Average Marks: {average}")

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("✅ Result: Pass")

    # Determine Grade
    if average >= 90:
        grade = "A 🏆"
    elif average >= 80:
        grade = "B 🎖️"
    elif average >= 70:
        grade = "C 🏅"
    else:
        grade = "D"

    print(f"🎓 Grade: {grade}")

else:
    print("❌ Result: Fail")
    print("🚫 Grade: No Grade")
