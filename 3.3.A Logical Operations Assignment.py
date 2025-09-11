"""
3.3.A: Logical Operations
In this exercise, you will practice using logical operators (and, or, not) in Python.
Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.

User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers.
Include two examples for each of the following operators:
and
or
not
Display Results: Print the logical statement and its result for each comparison.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input.
Sample Output: Here's an example of what your program's output might look like:
"""
# Get the user's numbers
a = int(input("Pick the first number  "))
b = int(input("Pick the second number  "))
c = int(input("Pick the third number  "))
# use all of (> < and or not)
if a > b and a > c:
    print(f"{a} is the largest number")
elif b > a and b > c:
    print(f"{b} is the largest number")
elif a == b == c:
    print("All of your numbers are the same")
else: print(f"{c} is the largest number")

if a == b:
    print("The first number is the same number as the second number")
elif a == c:
    print("The first number is the same number as the third number")
else:
     print("all of your numbers are unique from each other")
#or 
if b or c > 100:
    print("The second or third number is greater than 100")
elif b or c == 100:
    print("The second or third number is equal to 100")
else:
    print("The second or third number is less than 100")
#not
if not a > 100:
    print("The first number is not greater than 100")
elif a == 100:
    print("The first number is equal to 100")
else:
    print("The first number is not less than 100")