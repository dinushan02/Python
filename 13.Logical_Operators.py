"""a = 25
print(a >= 10 and a <= 20)  # False, because 25 is not in the range [10, 20]
print(a >= 10 or a <= 20)   # True, because 25 >= 10 (one condition is True)
print(not(a >= 10 and a <= 20)) """ # True, because `a >= 10 and a <= 20` is False, and `not False` is True


#Project: Grade Evaluator
#Features
#Accepts a numerical score (0-100).
#Uses comparison and logical operators to determine the grade.
#Displays appropriate messages based on the score.

# Grade Evaluator Program

# Function to evaluate the grade based on the given score
def evaluate_grade(score):
    """
    Evaluates and returns the grade based on the given score.

    Parameters:
    score (int): The student's score (0-100)

    Returns:
    str: The grade category
    """

    # Checking if the score is within a valid range
    if score < 0 or score > 100:
        return "Invalid Score! Please enter a value between 0 and 100."

    # Using logical and comparison operators to assign grades
    if score >= 90 and score <= 100:
        return "Grade: A (Excellent)"
    elif score >= 75 and score < 90:
        return "Grade: B (Good)"
    elif score >= 50 and score < 75:
        return "Grade: C (Average)"
    elif score >= 35 and score < 50:
        return "Grade: D (Needs Improvement)"
    else:
        return "Grade: F (Failed)"


# Taking input from the user
try:
    student_score = int(input("Enter your score (0-100): "))
    result = evaluate_grade(student_score)
    print(result)  # Display the grade
except ValueError:
    print("Invalid input! Please enter a numeric value.")

#How It Works
#The user enters a score between 0 and 100.
#The program checks if the score is valid.
#It evaluates the grade using comparison (>=, <=, <, >) and logical (and, or) operators.
#The result is displayed as:
#A (Excellent)
#B (Good)
#C (Average)
#D (Needs Improvement)
#F (Failed)
#If an invalid score is entered, an error message is displayed.