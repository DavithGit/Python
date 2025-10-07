"""
In this assignment, you will create a Python program that generates a random number 
between 1 and 100. Your program should allow the user to guess the number,
 and provide feedback on how close their guess is to the actual number.

Assignment Objectives:
Use the random module to generate a random number.
Implement a while loop to allow continuous guessing until the correct number is guessed.
Use the abs() function to determine the difference between the guess and the actual number.
Provide feedback based on the proximity of the guess to the actual number:
If the difference is within 5, print "Very Hot".
If the difference is within 15, print "Hot".
If the difference is within 25, print "Cool".
If the difference is more than 25, print "Cold".
Make sure to call the main function!
After completing the program, upload it to your GitHub repository.
Submit the link to your GitHub repository in Canvas.

Task Details:
Import the random module and use it to generate a random number between 1 and 100.
Write a while loop that allows the user to enter a guess for the number.
Inside the loop, use the abs() function to calculate the absolute difference between the guess 
and the actual number.
Provide feedback based on the computed difference (e.g., "Very Hot" for close guesses).
The loop should continue until the user guesses the correct number.
Additional Notes:
The abs() function is a built-in Python function used to calculate the absolute value of a number. 
The absolute value of a number is its distance from zero on the number line, regardless of direction. 
For example, abs(-5) and abs(5) both return 5.
"""
def main(): 
    import random
    #generate a random number between 1-100
    #call that number actual_number
    actual_number=random.randint(1,100)
    #while loop while the problem is unsolved
    solved = False
    while solved==False:
    #get guess with input
        guess = int(input("Please guess a number between 1 and 100!\n"))
        #use abs() to calculate distance from guess and actual number   
        difference = abs(guess - actual_number)
        if difference == 0:
            print(f"You got the number right! it was {actual_number}")
            solved = True
        elif difference > 25:
            print("Cold!")
        elif 25 > difference > 15:
            print("Cool!")
        elif 15 > difference > 5:
            print("Hot!")
        elif 5 > difference > 0:
            print("Very Hot!")

main()