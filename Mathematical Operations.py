"""
    Exploring mathematical operators in python

    Write a Python program to calculate the area of a rectangle:
Declare two variables, length and width, and assign values to them.
Calculate the area using the formula: area = length * width.
Print a message displaying the dimensions
and the area using concatenation or formatting.
"""
# declare variables
width = 10
width = int(width)
length = 15
length = int(length)
# calculate area
area = (length*width)
# print the variables length, width, and area
print("the area of a rectangle with a length of", int(length),
      "and a width of", int(width), "is", (area))

# just for fun down here

if (length > width):
    print("the rectangle is longer than it is wide")
else:
    print("the rectangle is wider than it is long")
