"""2.5 4 simple programs

Change the WORD_LIST to include 15 different words on a subject of your choice (e.g., animals, food, movies, sports, etc.).
Finish the guessed_letters logic:
    Before checking if the guessed letter is in the word, check if it is already in guessed_letters.
    If it is, print a message like You already guessed that letter! and skip the rest of the loop using continue.
    If it is not in the list, add it to guessed_letters and proceed with checking if it's in the word.
    Display how many incorrect guesses they have left.
"""

"""
Hangman Start - Week 10 Strings Demo

This program begins a simple version of Hangman. You will finish it by:
- Adding a list to keep track of guessed letters
- Checking if the letter was already guessed BEFORE checking if it is in the word ( give them feedback)
- Changing the word list to 15 words on a subject of your choice
- Display how many incorrect guesses they have left 
- validate data entry (actual letter? only 1 letter?)
- use a try and except statement around data entry
"""

import random

WORD_LIST = ("BUSTER", "MOONSHINE", "PHANTOM", "SCATTERSHOT" , "SEEP" , "SHOCKENAUGH", "ARCHITECT", "OVERDRIVE", "HURRICANE", "EAGLEEYE" , "FIREBIRD", "WARTHOG", "PINCHFIST","SPOOK","ARMOURDILLO")


def game(answer, display):
    wrong = 0
    right = 0

    print("Welcome to Code of Fortune Forts commanders edition!")
    print("You will guess letters until you have the commander")
    print("If you have 5 wrong guesses you will lose!")

    guessed_letters = []

    while True:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        guess = input("Please enter a letter: ").upper()

        # check if length is 1 charachter and a letter
        if len(guess) > 1:
            print("You can only guess one letter at a time!")
            continue
        # check if guess is in the alphabet    
        if guess.isalpha() == False:
            print("You have to guess a letter!")
            continue
            
        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        else:
            guessed_letters.append(guess)

        bad_guess = True
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess
                right += 1
                bad_guess = False

        if bad_guess:
            print("Wrong!")
            wrong += 1
            if wrong < 6:
                print("You can guess incorrectly", (5 - wrong), "more times!")
            if wrong > 5:
                print("You Lose!")
                print("The correct word was:", answer)
                break

        if right == len(answer):
            print("You Win!")
            print("The word was:", answer)
            break


def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)


main()