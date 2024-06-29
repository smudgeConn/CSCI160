'''

Ask for the number of credits a student has passed. 
State whether the student is a freshman (0-23), sophomore (24-59), junior (60-89), or senior (90 or greater). 
The class rank should start with a capital letter. 

'''

credits = int(input("Number of completed credits: "))

if credits < 24:
    print("Class Rank: Freshman")
elif credits < 60: 
    print("Class rank: Sophomore")
elif credits < 90:
    print("Class rank: Junior")
else:
    print("Class rank: Senior")