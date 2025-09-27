"""
Objective:

Develop a Python-based Madlib based on a song of your choice. The program should collect at least 8 different pieces of information from the user and incorporate them into the song using named arguments. The goal is to practice using functions, user input, and string manipulation in Python.
Important Note:

Choose any song you like for your madlib, but remember, no Rickrolling! Be creative and respectful in your song choice.
Task:

    #Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.
   # Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.
    Write the Function:
        Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
        Use f-strings to incorporate these parameters into the song's lyrics.
        Ensure the function prints the customized song lyrics.
    Collect User Input:
        Write code to collect user input for each of the 8 variables.
        Use clear and descriptive prompts to guide the user.
    Call the Function:
        Call the custom_song function with the user inputs as named arguments.
        Ensure the order of arguments matches the parameters in your function definition.
"""
# went with feel good inc by gorillaz
print ("we're going to make a madlib of Feel Good Inc. by Gorillaz.")
camels = input(f"Please enter an animal: ")
back = input(f"Please enter a body part: ")
horizon = input(f"Please enter a noun: ")
melancholy= input(f"Please enter an adjective: ")
smile= input(f"Please enter a verb: ")
windmill= input(f"Please enter a kind of building: ")
love= input(f"Please enter a noun: ")
free= input(f"Please enter an adjective: ")

def custom_song(camels,back,horizon,melancholy,smile,windmill,love,free):
    print("City's breaking down on a " + str(camels) +" "+ str(back))
    print("They just have to go, 'cause they don't know wack")
    print("So while you fill the streets, it's appealing to see")
    print("You won't get undercounted 'cause you're damned and free")
    print("You got a new " + str(horizon) + ", it's ephemeral style")
    print("A " + str(melancholy) + " town where we never " + str(smile))
    print("And all I wanna hear is the message beep")
    print("My dreams, they got her kissing 'cause I don't get sleep, no")
    print(str(windmill) + ", "+str(windmill) + " for the land")
    print("Turn forever, hand in hand")
    print("Take it all in on your stride")
    print("It is ticking, falling down")
    print(str(love) + " forever," + str(love) + " is " + str(free))
    print("Let's turn forever, you and me")
    print(str(windmill) + ", "+str(windmill) + " for the land")
    print("Is everybody in?")
    print("Laughin' gas, these hazmats, fast cats, linin' 'em up like ass cracks")
    print("Play these ponies at the track, it's my chocolate attack")
    print("Shit, I'm steppin' in the heart of this here")
    print("Care Bear reppin' in harder this year, watch me as I gravitate")
    print("Yo, we gon' ghost town this Motown, with yo' sound, you in the blink")
    print("Gon' bite the dust, can't fight with us, with yo' sound, you kill the Inc.")
    print("So don't stop, get it, get it until you're cheddar-headed")
    print("And watch the way I navigate, haha-haha")
    print(str(windmill) + ", "+str(windmill) + " for the land")
    print("Turn forever hand in hand")
    print("Take it all in on your stride")
    print("It is ticking, fallin' down")
    print(str(love) + " forever," + str(love) + " is " + str(free))
    print("Let's turn forever, you and me")
    print(str(windmill) + ", "+str(windmill) + " for the land")
    print("Is everybody in?")
    print("Don't stop, get it, get it") 
    print("Peep how your captain's in it")
    print("Steady, watch me navigate")
    print("Don't stop, get it, get it")
    print("Peep how your captain's in it")
    print("Steady, watch me navigate")

custom_song(camels,back,horizon,melancholy,smile,windmill,love,free)