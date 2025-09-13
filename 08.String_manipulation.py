s = "Sample"
print(s)       # Output: Sample
print(s[0:2])  # Output: Sa (Characters from index 0 to 1, 2 is excluded)
print(s[:5])   # Output: Sampl (From start up to index 4)
print(s[1:])   # Output: ample (From index 1 to the end)
print(s[-1])   # Output: e (Last character)
print(s[-2:-1]) # Output: l (Only the character at index -2)
print(s[:-1])  # Output: Sampl (All characters except the last one)
print(s[::-1]) # Output: elpmaS (Reversed string)

#String slicing is used in Python in many different contexts.
# It's a powerful feature
# that allows you to manipulate strings in a concise and efficient way.
# Here are some common use cases where string slicing is helpful:

#1. Extracting Substrings
#You can extract a portion of a string by specifying the start and end indices.
s = "Hello, World!"
substring = s[7:12]  # Extracts 'World'
print(substring)

#2. Reversing Strings
s = "Python"
reversed_s = s[::-1]  # 'nohtyP'
print(reversed_s)

#3. Skipping Characters
s = "abcdef"
every_other = s[::2]  # 'ace'
print(every_other)

#4. Trimming Leading/Trailing Characters
s = "   Hello   "
trimmed = s.strip()  # 'Hello'
trimmed_left = s.lstrip()  # 'Hello   '
trimmed_right = s.rstrip()  # '   Hello'
print(trimmed)
print(trimmed_left)
print(trimmed_right)

#5. Modifying Parts of a String
s = "Hello, World!"
modified = s[:5] + " Python"  # 'Hello Python'
print(modified)

#6. Checking Palindromes
#String slicing makes it easy to check if a string is a palindrome (i.e., it reads the same forwards and backwards).
s = "madam"
is_palindrome = s == s[::-1]  # True
print(is_palindrome)

#7. Working with Data Extraction (Parsing)
#Often in data parsing tasks (e.g., extracting specific parts of data from a formatted string), slicing is useful.
s = "2025-03-29"
year = s[:4]  # '2025'
month = s[5:7]  # '03'
day = s[8:]  # '29'
print(year)
print(month)
print(day)


my_str = "python"
result = my_str[::-2]
print(result)
"""
start → empty → means "start from end" (since step is negative).
stop → empty → means go until the beginning.
step = -2 → means move backwards through the string, skipping 1 character each time."""
# It prints nhy because [::-2] reverses the string while taking every 2nd character.

# [::2] → "pto"
# [::-1] → "nohtyp"
# [::-2] → "nhy"