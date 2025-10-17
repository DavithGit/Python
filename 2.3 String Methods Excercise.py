"""
2.3
String Methods Exercise

Step 1: Download the Exercise File
There is a Python file string_methods2.py Download string_methods2.pythat you need to download. 
This file contains several TODO comments, each indicating a small task for you to complete.

Step 2: Complete the Exercises
Open string_methods2.py in your favorite Python editor. 
For each TODO comment in the file, write the necessary Python code to complete the task. 
These tasks are designed to give you hands-on experience with different string methods.

Step 3: Test Your Code
After writing your code for each task, run the file to test your solutions. 
Make sure each part of the exercise works as expected. 
If you encounter errors, try to debug and fix them.

Step 4: Upload to GitHub
Once you are confident that your code works correctly, upload the string_methods2.py file to your existing GitHub repository. 
If you're new to GitHub, remember to 'commit' your changes and 'push' them to the repository.

Step 5: Submit Your Work
After uploading the file to GitHub, copy the URL of the file in your GitHub repository. 
Submit this link as your assignment. 
Make sure the link you submit goes directly to the string_methods2.py file in your GitHub repository.
"""
# just one line of code each :)

# TODO: Use the capitalize() method to capitalize the first letter of the string
string1 = "python"
print(string1.capitalize())

# TODO: Use the center() method to center the string in a string of specified width
string2 = "python"
print(string2.center(10, " "))  # width of 10, fills with spaces

# TODO: Use the endswith() method to check if the string ends with a specified substring
string3 = "python"
print(string3.endswith("on"))

# TODO: Use the find() method to find the first occurrence of a substring in the string
string4 = "python"
print(string4.find("th"))

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
string5 = "python3"
print(string5.isalnum())

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
string6 = "python"
print(string6.isalpha())

# TODO: Use the islower() method to check if all characters in the string are lowercase
string7 = "python"
print(string7.islower())

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
string8 = " "
print(string8.isspace())

# TODO: Use the isupper() method to check if all characters in the string are uppercase
string9 = "PYTHON"
print(string9.isupper())

# TODO: Use the join() method to join elements of an iterable with the string as the separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
print(separator.join(iterable1))

# TODO: Use the lower() method to convert all characters in the string to lowercase
string10 = "PYTHON"
print(string10.lower())

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
string11 = " python"
print(string11.lstrip())

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
string12 = "python "
print(string12.rstrip())

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
string13 = "I love python"
print(string13.replace("python", "snake"))

# TODO: Use the rfind() method to find the highest index of a substring
string14 = "python"
print(string14.rfind("n"))

# TODO: Use the split() method to split the string at a specified separator
string15 = "python-is-fun"
print(string15.split("-"))

# TODO: Use the startswith() method to check if the string starts with a specified substring
string16 = "python"
print(string16.startswith("py"))

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
string17 = " python "
print(string17.strip())

# TODO: Use the swapcase() method to swap the case of all characters in the string
string18 = "Python"
print(string18.swapcase())

# TODO: Use the title() method to convert the first character of each word to uppercase
string19 = "python is fun"
print(string19.title())

# TODO: Use the upper() method to convert all characters in the string to uppercase
string20 = "python"
print(string20.upper())


