a = "Ram kumar"
print(type(a))  # Output: <class 'str'>

# To input a multiline string, we should use triple quotes """ """
a = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
"""
print(a)
print(type(a))  # Output: <class 'str'>

# List example
para = []
print(type(para))  # Output: <class 'list'>

# Accessing list elements
para = [25, 35, 46]
print(para[2])  # Output: 46 (indexing starts from 0)

# Printing the list
print(para)  # Output: [25, 35, 46]

# Joining list elements into a string
para = ["25", "35", "46"]
print(','.join(para))  # Output: 25,35,46
print('|'.join(para))  # Output: 25|35|46 (Corrected)

print("😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁")

#TO GET MULTILINE STRING INPUT=> WE SHOULD USE while loop
para = []
print("Enter your favourite Hollywood movies (press Enter to stop): ")

while True:
    line = input()  # Store inputs from user
    if line:  # Check if input is not empty
        para.append(line)
    else:
        break  # Stop if the user enters an empty line

    print(para)  # Show the current list of movies

output = "\n".join(para)  # Join the list into a string with new lines
print(output)  # Print the final formatted output


