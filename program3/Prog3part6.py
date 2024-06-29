'''
name:Sandra Jurado Connors
email:sandra.connors@ndus.edu


Write individual while loops in each of the following parts.
Part 5 – must be named Prog3part5.py 
Ask for the starting value and ending values. Both values will be integers. 
Count from the starting value to the ending value by 1, regardless if you need to count up or count down. 
The output should include both the starting value and ending value


Part 6 – must be named Prog3part6.py 
Write a program that asks for the number of students in a class. 
Then use a while loop to ask for each students class rank (“Freshman”, “Sophomore”, “Junior”, “Senior”), 
with the case of each group as shown. 
Once all of the information has been entered tell how many students there are in each group. 
The class ranks must be in the order shown, followed by a color, with your calculated result last in the line
'''

totalStudents =  int(input('How many students in the class: '))
freshmen = 0
sophomores = 0
juniors = 0
seniors = 0

while freshmen+sophomores+juniors+seniors < totalStudents:
    rank = input('Enter the student rank: ')
    if rank == 'Freshman':
        freshmen += 1
    elif rank == 'Sophomore':
        sophomores += 1
    elif rank == 'Junior':
        juniors += 1
    elif rank == 'Senior':
        seniors += 1
    else:
        input("You must enter Freshman, Sophomore, Junior, or Senior. Try again.")

print(f'Freshman: {freshmen}\nSophomores: {sophomores}\nJuniors: {juniors}\nSeniors: {seniors}')
        