"""
Directions:
Accept a numeric grade from the user and display a letter grade. The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F

Check to see if the number given is between 0 and 100
"""

# Define a function to get a letter grade from a numeric grade
# Get the user's numeric grade
NumGrade = int(input("What is your numeric grade?  "))
# Check if grade is less than 60
if NumGrade < 60:
    LetterGrade = "F"  # Below 60 is a fail
# Check if age is between 60 and 69
elif NumGrade < 69:
    LetterGrade =  "D"
elif NumGrade < 79:
    LetterGrade = "C"
elif NumGrade < 89:
    LetterGrade = "B"
else:
    LetterGrade = "A"

print("Your Letter grade is: ", str(LetterGrade))