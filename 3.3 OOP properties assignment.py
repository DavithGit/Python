"""
3.3
This assignment is designed to reinforce your understanding of Python classes, properties, and the use of getter and setter methods, as well as class versus instance variables.
Assignment Details

        Define a Pet Class:
            #Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
            #Set a default value for pet_type as "Dog".
            #Implement getter and setter methods for all properties.
            #Include a class variable vet_name set to the name of your veterinary office.
            #Add a method display_pet_info to print all details of the pet and owner.

        Create Pet Objects:
            Instantiate at least three pet objects with different details.
            Show the use of setter methods for at least one pet object.
        Implement Property Existence Check:
            Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
        Display Information:
            Use display_pet_info to print details for each pet.
            Show three examples of check_property being used on various properties and pets.
            show two examples of display_pet_info on different instances of pet that you create

Deliverables

    Source code for the Pet class and a script demonstrating its functionality uploaded to GitHub.
    Hand in the link to your code on Canvas. 

About this Assignment:

    This assignment should take approximately 1-2 hours of study and 45 minutes of coding.
    Late submissions will result in a 10% deduction per day, up to a maximum of 50%.
    Submit your program on GitHub and provide the link for assessment.
    See grading details in the rubric below. 
    You may fix and resubmit your program within a week after the assignment is graded.

"""


class Pet:
        vet_name = "Pawfect Clinic"
        # Initializer with private variables
        def __init__(self, owner_first_name: str, owner_last_name: str, pet_id: int, pet_name: str, pet_type:str="Dog"):
            #owner_first_name, owner_last_name, pet_id, pet_name, and pet_type
            self.__owner_first_name = owner_first_name          # Private variable for first name
            self.__owner_last_name = owner_last_name            # Private variable for last name
            self.__pet_id = pet_id                              # Private variable for pet id
            self.__pet_name = pet_name                          # Private variable for pet name
            self.__pet_type = pet_type                          # Private variable for pet type

        # Method to display pet info
        def display_pet_info(self):
            return f"First: {self.__owner_first_name}, Last: {self.__owner_last_name}, Pet ID: {self.__pet_id}, Pet Name: {self.__pet_name}, Pet type: {self.__pet_type}"
        
        # Getters

        # Getter for first
        def get_first(self):
            return self.__owner_first_name

        # Getter for last
        def get_last(self):
            return self.__owner_last_name

        # Getter for id
        def get_ID(self):
            return self.__pet_id
        
        # Getter for pet name
        def get_pet_name(self):
            return self.__pet_name

        # Getter for type
        def get_type(self):
            return self.__pet_type

        # Setters

        # Setter for first
        def set_first(self, owner_first_name):
            self.__owner_first_name = owner_first_name

        # Setter for last
        def set_last(self, owner_last_name):
            self.__owner_last_name = owner_last_name

        # Setter for id
        def set_id(self, pet_id):
            self.__pet_id = pet_id

        # Setter for pet name
        def set_pet_name(self, pet_name):
            self.__pet_name = pet_name  

        # Setter for type
        def set_type(self, pet_type):
            self.__pet_type = pet_type

#check if a property exists
def check_property(obj, property_name):
    exists = hasattr(obj, property_name)
    print(f"Does '{property_name}' exist in {obj.__class__.__name__}? {exists}")
    return exists

def main():
    #create 3 pet objects
    user1 = Pet("John", "Doe", 1, "Charlie", "Cat")
    user2 = Pet("Kevin", "Neil", 2, "Bernard", "Dog")
    user3 = Pet("Zach", "Armstrong", 3, "Sparky", "Dog")

    #print the 3 pet objects
    print(user1.display_pet_info())
    print(user2.display_pet_info())
    print(user3.display_pet_info())
    
    #check that setters work
    user1.set_pet_name("Thor God of Thunder")
    user1.set_first("Odin")
    print(user1.display_pet_info())

        # Check property existence (3 examples)
    check_property(user1, "_Pet__pet_name")  
    check_property(user2, "vet_name")        
    check_property(user3, "set_pet_name")           


main()