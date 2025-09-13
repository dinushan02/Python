a = 25  # 25 stores in variable a
b = 25  # 25 stores in variable b
c = a + b  # Store Total in variable c

print("Total:", c)  # Output: 50
print(type(a))  # Output: <class 'int'>

print(id(a))  # Memory location of a
print(id(b))  # Same memory location as a (Python optimizes small integers)
print(id(c))  # Different memory location (new object for 50)

