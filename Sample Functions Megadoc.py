"""
example try and except input loop to be copy pasted 
"""
def main():
    #fahrenheit_to_celsius(100)
    #i_range()
    #input()
    #daylist()
    #bottles()
    
    print("This is a program designed to be an example of copy-paste-able simple inputs so I don't have to retype them all the time")


#parameter exampl
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

    #print(fahrenheit_to_celsius(77))
    #print(fahrenheit_to_celsius(95))
    #print(fahrenheit_to_celsius(50))

#i range not 100% sure what for
def i_range():

    for i in range(1, 10):
        if i % 7 == 0:
            print(i)
            continue

#Input try and except ****** use this every time
def input():

    try:
        number = int(input("Enter a number: "))
        result = 10 / number
    except ZeroDivisionError:
        print("Oops! Can't divide by zero. Try a different number.")
    except ValueError:
        print("That's not a number! Please enter a valid number.") 

#list append and print
def daylist():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    steps = []
    total = 0

    for day in days:
        step = input(f"Please enter your steps taken on {day} :")
        steps.append(step)
        print(f"{step} steps were taken on {day}")   

#while loop
def bottles():
    bottles = 99
    while bottles >1:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
        print("Take one down, pass it around")
        #subtract 1 from bottles
        bottles = bottles - 1
        print(f"{bottles} bottle of beer on the wall")
        print(f"{bottles} bottle of beer")

#string methods  
def string_methods():
    #honestly just see 2.3 string methods for full list, heres copy paste of that
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

main()       