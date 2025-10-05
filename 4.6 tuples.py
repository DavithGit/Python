"""
    Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
    Write a program that uses a for loop to print each class in the tuple.
    Use the len function to print how many courses are in the tuple.
    Make sure to use a main function for this program.
"""

def main():
    programming_classes = (
        'Intro to Python',
        'Advanced Python',
        'Database Essentials',
        'Web Development Basics',
        'Data Structures in Python',
        'Web Design Fundamentals'
    )

    # Print each class using a for loop
    print("Programming Classes:")
    for course in programming_classes:
        print(course)

    # Print how many courses are in the tuple
    print(f"\nTotal number of courses: {len(programming_classes)}")
main()