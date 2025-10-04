'''
4.6.B - Dictionaries
Assignment: NATO Phonetic Alphabet Dictionary
Your mission is to create a Python program that uses a dictionary to translate letters into
 the NATO Phonetic Alphabet. This program will ask users for a word and then spell it out using the NATO codes.

Steps to Follow:
Create the NATO Phonetic Alphabet Dictionary:
Construct a dictionary in Python named nato_alphabet, where each key is a letter, 
and its value is the corresponding NATO phonetic term.
Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter
 to find and print the NATO phonetic term.
Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.
Test Your Program:
Test the program with various inputs, ensuring it works as expected.
'''

"""
LOGIC OUTLINE
(#)Declare Global dictionary

(#)function to get word from user
(#)convert to all caps

(#)Loop
    use one of the dictionary methods to look up the nato value for each letter
    print nato value and a space

main
provide directions,
call function

call main
"""
nato_alphabet = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
    " ": " "
}
#get user word, explain
def main():
    print("You're going to be entering a word, and this code will translate it to NATO Phonetic English")
    user_word = input("\nPlease enter your word to be translated to NATO Phonetic Alphabet. ")
    spell_word(user_word)

#iterate through each letter, find and print the NATO alph version
def spell_word(word):
    caps_user_word = word.upper()
    print("\nYour translated word is: ")
    for letter in caps_user_word:
        translation = nato_alphabet.get(letter, " ")
        print(translation)

#call main
main()






#different methods of doing this

#using keys, key first value second
#"" for strings, no "" for non string
# whatever text it is .upper
# uppercase_text = text.upper
# letter = nato_alphabet["A"]
# print str(letter)

# for i  in range(0,20):
#     letter = nato_alphabet[i]
#     print(letter)

# value = nato_alphabet.get(0, "invalid")
# print(value)

# for key in nato_alphabet:
#     print(key, nato_alphabet[key])

# for key, value in nato_alphabet():
#     if key > 26:
#         print(key, value) 
     