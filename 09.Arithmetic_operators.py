"""a = 123
b = 10
print(a + b)  # Adds a and b (123 + 10 = 133)
print(a - b)  # Subtracts b from a (123 - 10 = 113)
print(a * b)  # Multiplies a and b (123 * 10 = 1230)
print(a / b)  # Divides a by b (123 / 10 = 12.3)
print(a // b) # Integer division (divides a by b and drops the decimal part) (123 // 10 = 12)
print(a % b)  # Modulus (remainder of the division) (123 % 10 = 3)
print(2 ** 3)  # Exponentiation (2 raised to the power of 3 = 8)
"""

def add(a, b):
    result = a + b
    print(f"\n{a} + {b} = {result}\n")


def subtract(a, b):
    result = a - b
    print(f"\n{a} - {b} = {result}\n")


def multiply(a, b):
    result = a * b
    print(f"\n{a} × {b} = {result}\n")


def divide(a, b):
    if b == 0:
        print("\n❌ Error: Division by zero is not allowed!\n")
    else:
        result = a / b
        print(f"\n{a} ÷ {b} = {result}\n")


def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")


def main():
    while True:
        print("\n🔢 Simple Calculator 🔢")
        print("A. Addition (➕)")
        print("B. Subtraction (➖)")
        print("C. Multiplication (✖️)")
        print("D. Division (➗)")
        print("E. Exit (🔚)")

        choice = input("📌 Input your choice: ").strip().upper()

        if choice == "E":
            print("\nProgram ended (🔚)")
            break  # Exit the loop

        if choice in ["A", "B", "C", "D"]:
            a = get_number_input("💡 Input first number: ")
            b = get_number_input("💡 Input second number: ")

            if choice == "A":
                add(a, b)
            elif choice == "B":
                subtract(a, b)
            elif choice == "C":
                multiply(a, b)
            elif choice == "D":
                divide(a, b)
        else:
            print("\n❌ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()

