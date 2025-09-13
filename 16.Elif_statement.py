#You can use this type of condition-based logic in real projects.
#However, in larger applications, you should follow best practices
#to make your code more efficient, readable, and maintainable.
#Here are some important considerations:

#✅ Best Practices for Real Projects
#1️⃣ Use Functions for Reusability
#Instead of writing the logic in one block, wrap it in a function:
def calculate_fine(days):
    if days == 0:
        return "😊 Good job! No fine. 👍"
    elif 1 <= days <= 5:
        return f"📅 Fine Amount: ${days * 0.5} 💰 (Small fine)"
    elif 6 <= days <= 10:
        return f"📅 Fine Amount: ${days * 1} 💰 (Moderate fine)"
    elif 11 <= days <= 30:
        return f"📅 Fine Amount: ${days * 5} 💸 (High fine)"
    else:
        return "⚠️ Membership canceled! ❌ Please contact the library."

days = int(input("Enter the number of overdue days: "))
print(calculate_fine(days))
#✔ Why? Functions make it modular and reusable for different parts of your project.


#2️⃣ Use Dictionaries for Cleaner Code
#Instead of multiple elif conditions, you can use a dictionary:
def calculate_fine(days):
    fine_rates = {5: 0.5, 10: 1, 30: 5}
    for limit, rate in fine_rates.items():
        if days <= limit:
            return f"📅 Fine Amount: ${days * rate} 💰"
    return "⚠️ Membership canceled! ❌"

days = int(input("Enter the number of overdue days: "))
print(calculate_fine(days))

#✔ Why? This avoids too many elif conditions and makes it easier to update.


⃣#3.Use a Database for Real-World Systems
#If you’re building a library management system, storing fines in a database would be better:
#Use SQL (PostgreSQL, MySQL, SQLite) or NoSQL (MongoDB)
#Instead of checking conditions in Python, fetch fine rules from the database.
#Example:
#Store fine rates in a database table.
#When a user enters days, fetch the fine rule and calculate accordingly.

#🔥 Conclusion
#Your method works fine for small scripts, but in real projects, you should: ✅ Use functions for reusability
#✅ Use dictionaries for better condition handling
#✅ Store data in a database for scalability


