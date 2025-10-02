"""
4.7 - Exceptions
Demonstrate the basics of exception handling in Python. Use try, except, else, and finally blocks to manage errors.
Assignment: Adding Exception Handling

Instructions
Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError.
 Handle incorrect data types with an error message.
Test Your Code: Ensure the exception handling works correctly with various inputs.
GitHub Upload: Upload your py file to GitHub and hand in the link

Objective: Enhance a basic Python program by implementing try and except statements to handle 
errors in user input, focusing on data type errors.


"""

#Starting Code

# Simple Python program to calculate the square of a number

def square_number():
     number = input("Enter a number to square: ")
     squared_number = int(number) ** 2
     print(f"The square of {number} is {squared_number}.")
    #except UnboundLocalError:
#print("I'm sorry, you need to enter a number between 1 and 3")
        
   # except ValueError:
       # print("I'm sorry, that is not a number")

square_number()


#use try and except

#at least a value error
"""

    dictionary and error checking with exceptions


"""

SECRET_CODE = {
    "a": "🍎",
    "b": "🐝",
    "c": "🌊",
    "d": "🐬",
    "e": "🥚",
    "f": "🐸",
    "g": "🦒",
    "h": "🏠",
    "i": "🍦",
    "j": "🕹️",
    "k": "🔑",
    "l": "🦁",
    "m": "🌙",
    "n": "🎶",
    "o": "🐙",
    "p": "🥞",
    "q": "👑",
    "r": "🌈",
    "s": "⭐",
    "t": "🌴",
    "u": "☂️",
    "v": "🎻",
    "w": "🌍",
    "x": "❌",
    "y": "🧶",
    "z": "🦓",
    " ": "⬜",   # space
    ",": "⚓",
    "!": "💥",
    ".": "🔵"
}

def create_code(word):
    # using get in case does not exist
    code = ""
    word = word.lower()
    for letter in word:
        symbol = SECRET_CODE.get(letter, "⁉️")
       # print(symbol)
        code = code + symbol
    return code

def decode(code):
    result = ""
    for symbol in code:
        for k, v in SECRET_CODE.items():
            if v == symbol: 
                result += k

    return result

def main():
    try:
        value = 0
        print(" 1. Create Secret Code \n 2. Decode \n 3. Quit")
        while value > 3 or value < 1:
            value = int(input("Please enter a number for your selection (1, 2 or 3 to quit):") )
            if value == 1:
                my_word = input("Please enter a word or phrase:   ")
                result = create_code(my_word)
            elif value == 2:
                my_code = input("Paste the code!:  ")
                result = decode(my_code)
            elif value == 3: 
                break

            print(result)
            value = 0
    except UnboundLocalError:
        print("I'm sorry, you need to enter a number between 1 and 3")
        
    except ValueError:
        print("I'm sorry, that is not a number")
      

#main()