"""
3.4 Methods assignment


Objective: Understand and implement a class with specific attributes and methods and explore Python's special methods and functions.
Task Description:

        Create the Pet Class:
            Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
            Implement get and set methods for each of these attributes.
            Add a method called print_details that prints the details of the pet.
        Create Instances:

        Create three objects of the Pet class with different kinds, breeds, and names.

        Call the print_details method for each object that you created
        Demonstrate a Special Method or Function:

        Choose three of the following and demonstrate its use with the Pet class instances:
            __name__: Display the name of the class.
            type(): Show the class used to instantiate a pet object.
            __module__: Return the module name in which the Pet class is defined.
            __bases__: Display the base classes of the Pet class (if any).
            isinstance(): Check if an instance is of the Pet class.

Submission Requirements:

        Submit the Python script containing the Pet class definition and instances by uploading it to your GitHub repository and submitting the link
        Include comments to demonstrate the usage of the chosen special method or function.
        Ensure code follows Python best practices for readability and efficiency.

 
About this Assignment:

    This assignment should take approximately 1-2 hours of study and 45 minutes of coding.
    Late submissions will result in a 10% deduction per day, up to a maximum of 50%.
    Submit your program on GitHub and provide the link for assessment.
    See grading details in the rubric below. 
    You may fix and resubmit your program within a week after the assignment is graded.

"""
class Pet:
        # Initializer with private variables
        def __init__(self, kind: str, breed: str, name: str):
            #owner_first_name, owner_last_name, pet_id, pet_name, and pet_type
            self.__kind = kind              # Private variable for first name
            self.__breed = breed            # Private variable for last name
            self.__name = name              # Private variable for pet id


        # Method to display pet info
        def print_details(self):
            return f"Kind: {self.__kind}, Breed: {self.__breed}, Name: {self.__name}"
        
        # Getters

        # Getter for kind
        def get_kind(self):
            return self.__kind

        # Getter for breed
        def get_breed(self):
            return self.__breed

        # Getter for name
        def get_name(self):
            return self.__name

        # Setters

        # Setter for kind
        def set_kind(self, kind):
            self.__kind = kind

        # Setter for breed
        def set_breed(self, breed):
            self.__breed = breed

        # Setter for name
        def set_name(self, name):
            self.__name = name

def main():
    #create 3 pet objects
    user1 = Pet("Lizard", "Bearded Dragon", "Gandalf")
    user2 = Pet("Bird", "Parrot", "Jeff")
    user3 = Pet("Cat", "Persian", "Shelly")

    #print the 3 pet objects
    print(user1.print_details())
    print(user2.print_details())
    print(user3.print_details())
    
    #special method or function stuff
    
    # 1. Show the class used to instantiate a pet object
    print(f"type(user1): {type(user1)}")  # Shows the Pet class

    # 2. Display the base classes of Pet
    print(f"Pet.__bases__: {Pet.__bases__}")  # Shows (object,)

    # 3. Check if an object is an instance of Pet
    print(f"isinstance(user3, Pet): {isinstance(user3, Pet)}")  # True

main()