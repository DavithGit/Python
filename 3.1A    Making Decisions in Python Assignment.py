"""
Write a Python program that uses if-else statements and:

Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.
Remember:

Comment your code to explain the functionality of each section.
Handle edge cases, such as ages, precisely at the thresholds.

"""
#get user age
age = int(input("What is your age?  "))

#can they drive
if age > 15:
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")

 #can they vote
if age > 17:
    print("You are old enough to vote ")
else:
    print("You are not old enough to vote ")

#can they drink
if age > 20:
    print("You are old enough to drink")
else:
    print("You are not old enough to drink")

#can they get a discount
if age > 64:
    print("You are old enough to get a senior discount")
else:
    print("You are not old enough get a senior discount")
