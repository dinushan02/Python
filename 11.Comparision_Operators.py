"""a = 20
b = 20

print(a == b)  # True  (Checks if a is equal to b)
print(a != b)  # False (Checks if a is not equal to b)
print(a > b)   # False (Checks if a is greater than b)
print(a < b)   # False (Checks if a is less than b)
print(a >= b)  # True  (Checks if a is greater than or equal to b)
print(a <= b)  # True  (Checks if a is less than or equal to b)"""

#Project Idea: Student Grade Evaluator 🎓
#This project will take a student's marks, compare them to grade thresholds,
#and determine the final grade using comparison operators (==, !=, >, <, >=, <=).

#📜 Project: Student Grade Evaluator
#This program will:
#✅ Ask the user to input a student's score.
#✅ Compare the score against a grading system.
#✅ Display the final grade (A, B, C, D, or F).

# Student Grade Evaluator
# This program determines the grade of a student based on their marks.

def evaluate_grade(marks):
    """
    Determines the student's grade based on marks.

    Parameters:
    marks (int or float): The score obtained by the student.

    Returns:
    str: The grade corresponding to the marks.
    """
    if marks >= 90:
        return "A"  # 90 and above = Grade A
    elif marks >= 80:
        return "B"  # 80-89 = Grade B
    elif marks >= 70:
        return "C"  # 70-79 = Grade C
    elif marks >= 60:
        return "D"  # 60-69 = Grade D
    else:
        return "F"  # Below 60 = Fail


# Taking input from the user
marks = float(input("Enter student's marks: "))

# Evaluating and displaying the grade
grade = evaluate_grade(marks)
print(f"Student's Grade: {grade}")

# Checking if the student passed or failed
if grade == "F":
    print("The student has failed. Needs improvement!")
else:
    print("The student has passed. Well done!")


#📌 Explanation:
#The function evaluate_grade(marks) determines the grade based on the comparison operators (>=).
#The program then checks if the student passed or failed using ==.
#It takes user input and converts it into float to allow decimal scores.
#The final grade is printed, along with a message of encouragement.

#✅ Uses comparison operators effectively
#✅ User-friendly and interactive
#✅ Perfect for an HND-level project