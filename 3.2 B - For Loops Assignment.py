"""
3.2 B - For Loops
Write a Python program to find and print all numbers divisible by 7 between 1 and 300.
 Use a for loop and the modulus operator (%).
"""
for i in range(1, 300):
    if i % 7 == 0:
            print(i)
            continue 

