"""
4.7 - Exceptions
Demonstrate the basics of exception handling in Python. Use try, except, else, and finally blocks to manage errors.
Assignment: Adding Exception Handling

Instructions
Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError.
 Handle incorrect data types with an error message.
Test Your Code: Ensure the exception handling works correctly with various inputs.
GitHub Upload: Upload your py file to GitHub and hand in the link

Objective: Enhance a basic Python program by implementing try and except statements to handle 
errors in user input, focusing on data type errors.


"""
# Simple Python program to calculate the square of a number

#use try and except

#at least a value error
def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
    except ValueError:
        print("Error: That is not a valid number. Please enter a number.")
    else:
        print(f"The square of {number} is {squared_number}.")
    finally:
        print("Program finished.")

square_number()