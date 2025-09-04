"""
Create a Python application that allows users to input their total budget and the amount spent in various categories. The program will then calculate and display the percentage of the total budget each category represents.

Requirements:
Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
Housing (rent or mortgage)
Utilities
Groceries
Transportation
Health Care
Personal Care
Clothing
Debt
Calculate the percentage of the total budget spent in each category.
Tell the user how much the spent total, and how much money they have left. 
Display the results in a user-friendly format using f-strings.
Ensure your code is well-commented to explain the functionality of different sections.
"""

#get totatl budget and amounts spent for categories

MonthlyIncome = float(input("Enter your net monthly income: "))
Housing = float(input("Enter the amount spent on Housing: "))
Utilities = float(input("Enter the amount spent on Utilities: "))
Groceries = float(input("Enter the amount spent on Groceries: "))
Transportation = float(input("Enter the amount spent on Transportation: "))
HealthCare = float(input("Enter the amount spent on Health Care: "))
PersonalCare = float(input("Enter the amount spent on Personal Care: "))
Clothing = float(input("Enter the amount spent on Clothing: "))
Debt = float(input("Enter the amount spent on Debt: "))

#calculate total and remainder money

Total = (Utilities + Housing + Groceries + Transportation + HealthCare + PersonalCare + Clothing + Debt)
Remainder = (MonthlyIncome-Total)

#print total and leftover money

print("Your total amount spent a month is "  +str(Total))
print("Your leftover money a month is "  +str(Remainder))

#calculate % of total budget and print

HousingPercent = (Housing/MonthlyIncome)
UtilitiesPercent = (Utilities/MonthlyIncome)
GroceriesPercent = (Groceries/MonthlyIncome)
TransportationPercent = (Transportation/MonthlyIncome)
HealthCarePercent = (HealthCare/MonthlyIncome)
PersonalCarePercent =(PersonalCare/MonthlyIncome)
ClothingPercent =(Clothing/MonthlyIncome)
DebtPercent =(Debt/MonthlyIncome)

#print the percentages of monthly income to user 
print("The percent of the budget you spend on Housing is "+(f"{HousingPercent:.2%}"))
print("The percent of the budget you spend on Utilities is "+(f"{UtilitiesPercent:.2%}"))
print("The percent of the budget you spend on Groceries is " +(f"{GroceriesPercent:.2%}"))
print("The percent of the budget you spend on Transportation is "+(f"{TransportationPercent:.2%}"))
print("The percent of the budget you spend on Health Care is "+(f"{HealthCarePercent:.2%}"))
print("The percent of the budget you spend on Clothing is "+(f"{ClothingPercent:.2%}"))
print("The percent of the budget you spend on Debt is "+(f"{DebtPercent:.2%}"))