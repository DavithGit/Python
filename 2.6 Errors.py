"""2.6 Errors
Write a short interactive Python program of your choice that uses try and except to catch and respond to at least two specific exceptions. Your program should:

Include a main() function.
Use try and except to catch specific errors like ValueError or ZeroDivisionError.
Provide helpful messages when errors occur.
Do something meaningful or fun—be creative! You could build a number guessing game, a basic calculator,
 or even a simple quiz with input validation.
Make sure to comment your code and upload it to GitHub when complete. Submit your link on Canvas.
"""
def main():
    try:
        numerator = int(input("enter a number to be the numerator: "))
        denominator = int(input("enter a number to be the denominator: "))
        division = numerator/denominator
        print((division), "is the output after division." )
    except ValueError:
        print("Enter a valid value, Try again.")
        main()
    except ZeroDivisionError:
        print("Cannot divide by zero! Try again.")
        main()
    except SyntaxError:
        print("SyntaxError should not happen if I coded this right")
        main()
    except: 
        print("An error occured, try again.")
    #recursion is a cool thing to do here I think
main()
