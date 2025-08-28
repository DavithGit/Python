"""
Create a Python program that converts kilograms to pounds.
Use at least four different samples to convert.
 A sample of the math is provided below;
do not use the same example in your program.
"""

# define variables for kg values
kg_value_1 = 100.100
kg_value_2 = 111.111
kg_value_3 = 999.99
kg_value_4 = 50.56

# 1 lb = 2.20462 kg
conversion_factor = 2.20462

# calculate pounds for each kg value
lbs_1 = kg_value_1/conversion_factor
lbs_2 = kg_value_2/conversion_factor
lbs_3 = kg_value_3/conversion_factor
lbs_4 = kg_value_4/conversion_factor

# output the results
print(f"{kg_value_1} kilograms is equal to {lbs_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {lbs_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {lbs_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {lbs_4:.2f} pounds.")

# seems like a lot of work but really not bad
