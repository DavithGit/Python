"""
Use a main() function to organize your code.
Prompt for User Input:
Ask the user to enter a single character using input().
Validate the Input:
Ensure the user enters precisely one character.
Use len() to check input length.
Convert to ASCII Value:
Use the built-in function ord() to get the ASCII value.
Example:
ascii_value = ord(user_input)
Display the Result:
Print the ASCII value to the user.

Reverse Lookup:
Prompt the user to enter an ASCII value.
Ensure that the value is between 32 and 127.
Use a try-except block to handle invalid inputs.
Use the built-in function chr() to get the corresponding character.
Example:
character = chr(ascii_input)
Test Your Program:
Run your script and try various characters and ASCII values.
Submit Your Work:
Upload your script to GitHub.
Submit a link to your repository.
"""
def main():
    user_input= input("enter a single character without spaces ")
    if len(user_input) != 1:
        print ("invalid length")
    ascii_value = ord(user_input)
    print(f"Your ASCII value is {ascii_value}")
    try:
        ascii_input = int(input("enter a value between 32 and 127: "))
        if ascii_input>31 and ascii_input<128:
            character = chr(ascii_input)
            print(f"The character for ASCII value {ascii_input} is '{character}'.")
        else:
            print("invalid ASCII value")
    except TypeError:
        print("invalid input")
main()