"""
Welcome to your Python assignment! 3.4 Lists
This task will help you practice working with lists, user input, and basic calculations. 
Follow the steps below:

Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps.
"""

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
total = 0

for day in days:
    step = input(f"Please enter your steps taken on {day} :")
    steps.append(step)
    print(f"{step} steps were taken on {day}")   
    
#trying to print the steps taken on each day 

#for mysteps in steps:
#    print(f"{mysteps} steps were taken on {day}")
    #when the second var is day it just prints saturday
    #when the second var is days it just prints every item in the list

#for day in days:
#    print(f"{step} steps were taken on {day}")    
#^ this does the same thing but with steps broken instead of days

for  mysteps in steps:
#     print(mysteps)
     total = total + int(mysteps)

print(f"total: {total}")
print(f"the average steps was: {total / len(steps): .2f}")
