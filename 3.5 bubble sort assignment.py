"""
Task:
Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.
Submission:
Save your program in a .py file and upload it to GitHub.
 Submit the GitHub link on Canvas.
Include comments in your code explaining your logic.
"""
#get 5 names
names = []
count=5
while count>0:
    count=count-1
    name = input(f"Please a name:")
    names.append(name)
#^this works

#convert to lwr
names = [name.lower() for name in names]
#^this works

#bubble sort the 5 names
#algorithm taken from canvas
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True # Mark that a swap occurred
print(names)

# reverse the sorted list
names.reverse()
print(names)

#the flowchart and activity were both helpful for this