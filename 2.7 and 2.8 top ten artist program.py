"""2.7 and 2.8 exceptions
Objective: Write a Python program that handles exceptions related to list operations.
 Your program will start with a predefined list of the top ten performing
   artists of all time and will include functionality to modify this list based on user input.

Tasks:
Modify Artist List: Write a function to replace an artist in the top_artists list.
 The function should ask the user for an index and a new artist name.
   Ensure your function catches and handles ValueError for invalid number conversion and IndexError for out-of-range indices.
General Error Handling: Modify your function to catch both ValueError
 and IndexError using a single except block. Provide a general error message like "An input error occurred."
Hints:
Use input() to get user input for the index and new artist name.
Convert the index input to an integer using int(). This might raise a ValueError if the input is not a valid integer.
When replacing an artist in the list, accessing an invalid index will raise an IndexError.
Use a try...except block to catch and handle these exceptions.
Remember that you can catch multiple exceptions in a single block by using a tuple for general error handling.
Example User Interaction:
Enter the index of the artist to replace: 2
Enter the new artist name: Taylor Swift
Updated list: ['The Beatles', 'Madonna', 'Taylor Swift', 'Elvis Presley', ...]

Note to Students: This assignment is designed to test your understanding of exception handling in Python.
Focus on how you can make your program robust against invalid user inputs and how to provide informative error messages.
Good luck!
"""
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

    #print instructions to user
    print("This is a program to view and replace a top 10 list of popular music artists. ")
    print("The current top 10 list is: ")
    print(top_artists)
    #replace an artist in the top 10
    #get replacement name new artist
    new_art = input("Please enter the name of the artist you would like to add to the list: ")
    #get wanted replacement positoion
    try: 
        old_index = int(input("Please enter the index of the artist you would like to replace in list: "))
    except ValueError:
        print("Please enter a valid index.")
        main()
    except IndexError:
        print("Invalid Index, please try again")
        main()
    #remove the artist the user wants removed, and add the artist they want added
    try:
        top_artists.pop(old_index)
        top_artists.append(new_art)
    except:
        print("Error removing old artist or adding new one. Please try again.")
        main()
    #print updated list
    print(top_artists)
main()
