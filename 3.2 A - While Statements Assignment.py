"""
3.2 A - While Statements
Write the program "99 Bottles of Beer on the Wall" using a while loop. 
Be mindful to change the word 'bottles' to 'bottle' when down to the last one. 
You must do the full 99 bottles; the sample shows the last 3 verses.
"""
bottles = 99
while bottles >1:
    print(f"{bottles} bottles of beer on the wall")
    print(f"{bottles} bottles of beer")
    print("Take one down, pass it around")
    #subtract 1 from bottles
    bottles = bottles - 1
print(f"{bottles} bottle of beer on the wall")
print(f"{bottles} bottle of beer")