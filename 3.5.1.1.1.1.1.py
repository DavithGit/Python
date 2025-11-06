# 3.5.1.1 OOP Funds: Inheritance
"""
Assignment Part 1: Defining Classes

File 1: Write an Employee class with the following attributes:

        Employee name
        Employee number

Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

        Shift number (integer: 1 for day, 2 for night)
        Hourly pay rate

Implement accessor and mutator methods (getters and setters) for each class.
Assignment Part 2: Implementing and Testing

 

Part 2: Write a script to:

        Create an instance of ProductionWorker.
        Prompt the user for each attribute's data.
        Store and then display the data using the object's methods.

"""
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Getters
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def __str__(self):
        return f"Employee Name: {self.__name}, Employee Number: {self.__number}"


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_num, pay_rate):
        super().__init__(name, number)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

    # Getters
    def get_shift_num(self):
        return self.__shift_num

    def get_pay_rate(self):
        return self.__pay_rate

    # Setters
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def __str__(self):
        return (f"{super().__str__()}, "
                f"Shift Number: {self.__shift_num}, "
                f"Hourly Pay Rate: ${self.__pay_rate:.2f}")


def main():
    print("Enter Production Worker details:")

    name = input("Employee name: ")
    number = input("Employee number: ")
    shift_num = int(input("Shift number (1 for day, 2 for night): "))
    pay_rate = float(input("Hourly pay rate: "))

    worker = ProductionWorker(name, number, shift_num, pay_rate)

    print("\nEmployee Information:")
    print(worker)

main()