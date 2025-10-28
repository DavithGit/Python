"""
3.2
Programming Assignment: coding your first class
Your task is to design and implement a class in a programming language. 
This class will represent a person and hold personal data.

 

Assignment Steps:

Class Creation: Design a class selfd Person with the following data: self, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. 
These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. 
Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. 
Ensure the output is formatted and easy to read.
Additional Resources:

For this assignment, a class diagram is provided to help you understand the structure of the Person class. 
In future assignments, you will create your class diagrams using Microsoft Word and a simple table.
Also, check out the accompanying video to learn more about accessors and mutators.

UML Class diagram
Person
- self: String
- address: String
- age: Integer
- phone: String
+ set_self(self)
+ set_address(address)
+ set_age(age)
+ set_phone(phone)
+ get_self()
+ get_address()
+ get_age()
+ get_phone()
"""

# Explanation of the Student Class
# __init__ method: This is the constructor. It initializes the object's attributes.
# self: Represents the instance of the class and allows access to its attributes and methods.
# set_ methods: Public methods to set the attributes of the student.


# Class definition for a Person

    #print("This program ")
class Person:
        """
        This class represents a Person
        """
        # Initializer with private variables
        def __init__(self: str, name: str, address: str, age: int, phone_number: str):
            self.__name = name # Private variable for name
            self.__address = address  # Private variable for address
            self.__age = age    # Private variable for age
            self.__phone_number = phone_number    # Private variable for phone number

        # Method to get person's info as a formatted string
        def get_info(self):
            return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, Phone Number: {self.__phone_number}"

        # Getters

        # Getter for name
        def get_name(self):
            return self.__name

        # Getter for address
        def get_address(self):
            return self.__address

        # Getter for age
        def get_age(self):
            return self.__age

        # Getter for phone_number
        def get_phone_number(self):
            return self.__phone_number

        # Setters

        # Setter for name
        def set_name(self, name):
            self.__name = name

        # Setter for address
        def set_address(self, address):
            self.__address = address

        # Setter for age
        def set_age(self, age):
            self.__age = age

        # Setter for phone number
        def set_phone_number(self, phone_number):
            self.__phone_number = phone_number

def main():
    fake_person = Person("John", "123 Street Lane", 25, "877CASHNOW")
    Ruth = Person("Ruth", "456 Street Bvd", "20", "1234567890")
    print(Ruth.get_info())
    print(fake_person.get_info())
    
    fake_person.set_name("Jane")
    print(fake_person.get_name())
    print(fake_person.get_address())
    print(fake_person.get_age())
    print(fake_person.get_phone_number())

main()