#Code & Explanation
s = "Tutor Joes"  # Strings can be enclosed in "" or ''
print(s)          # Prints the string
print(type(s))    # Prints the type, which is <class 'str'>

# String methods
print(s.upper())        # Converts to uppercase: "TUTOR JOES"
print(s.lower())        # Converts to lowercase: "tutor joes"
print(s.capitalize())   # Capitalizes first letter: "Tutor joes"
print(s.title())        # Capitalizes each word: "Tutor Joes"
print(s.count("o"))     # Counts occurrences of 'o': 2
print(s.endswith("es")) # Checks if string ends with "es": True
print(s.find("o"))      # Finds index of first 'o': 2
print(s.find("o", 5))   # Finds 'o' starting from index 5: 6
print(s.replace("o", "W"))  # Replaces 'o' with 'W': "TutWr JWes"

#String Validation Methods
a = "joes1233"
print("Is upper : ", a.isupper())   # False (not all uppercase)
print("Is lower : ", a.islower())   # True (all lowercase)
print("Is Alpha Numeric : ", a.isalnum())  # True (only letters and numbers)
print("Is Alpha : ", a.isalpha())   # False (contains numbers)

#Working with Multi-line Strings
print("😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁")
s = "He\nis\ngood"
print(s)
# Output:
# He
# is
# good

print(s.splitlines())      # Splits string at newline: ['He', 'is', 'good']
print(s.splitlines(True))  # Keeps newlines: ['He\n', 'is\n', 'good']

#Splitting Strings
print("😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁")
a = "Tutor Joes Computer Education"
print(a.split())  # Splits at spaces: ['Tutor', 'Joes', 'Computer', 'Education']

a = "Tutor,Joes,Computer,Education"
print(a.split(","))  # Splits at commas: ['Tutor', 'Joes', 'Computer', 'Education']


#Whitespace Removal
print("😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁")

s = "   Dinujothi      "
print(len(s))          # 18 (includes spaces)
print(len(s.strip()))  # 9 (removes all leading & trailing spaces)
print(len(s.lstrip())) # 15 (removes only leading spaces)
print(len(s.rstrip())) # 12 (removes only trailing spaces)


#Partitioning a String
s = '12-03-2020'
print(s.partition('-'))
# Splits at first occurrence of '-' into 3 parts: ('12', '-', '03-2020')

