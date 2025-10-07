""""
demonstrate using the calculator module
"""
from math_operations import calculator
from math_operations import geometry

def main():
    result = calculator.add(5, 3)
    print("Addition result:", result)

    result = calculator.subtract(10, 4)
    print("Subtraction result:", result)

    result = geometry.area_circle(10)
    print("Circle area result:", result)

    result = geometry.area_rectangle(10,10)
    print("Rectangle area result:", result)

    result = geometry.area_triangle(10,5)
    print("Triangle area result:", result)
main()