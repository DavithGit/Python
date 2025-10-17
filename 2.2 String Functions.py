"""
2.2
Exploring String Functions in Python

Setting Up Your Environment:
Open Visual Studio Code (VS Code) on your computer.
Create a new Python file named strings.py.
Download the Starting Code:
string_practice-2.pyDownload string_practice-2.py

Complete the Code:
Follow the directions in each TODO section.
Write the necessary Python code to accomplish the tasks in the comments.
Ensure your code runs without errors.
Upload to GitHub:
Upload the completed strings.py file to a new repository in your GitHub account.
If new to GitHub, create a repository and upload your file.
Submit Your Assignment:
Copy the URL to your strings.py file on GitHub.
Submit this link to your instructor or through your course submission portal.
"""
def main():
# Example string
    example_string = "Hello, Python programmers!"
    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char)
        
    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    print(min(example_string))

    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    print(max(example_string))

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    print(example_string.find('o'))
 

    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    char_list = list(example_string)
    print(char_list)
    
    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    print(example_string.count('o'))
main()
