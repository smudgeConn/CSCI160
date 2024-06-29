'''
Name: Sandra Jurado Connors
Student ID Number: 1551539
Program Number: 6

Part 1:
Use input() to ask for a file name. 
The file must exist in the same folder as the program. 
Then ask for a series of floating point values. 
For this assignment we will keep the values in the range of -5 to 105. 
DO NOT accept a value that is outside of this range. 
Continue to accept, and write values to the file until the user enters a value NOT 
within the inclusive range of -5 to 105. 
Write each value to the file as it is entered. 
Make sure to close the file once the user has finished entering in the data.  
'''

fileName = input('What is the name of the file? ')
# fileName = 'part1file.txt'
with open (fileName, 'w') as file:
    while True:
        floatingPointValue = input('Enter a floating point value between -5 and 105: ')
        try:
            if -5 <= float(floatingPointValue) <= 105:
                file.write(f'{floatingPointValue}\n')
            else: 
                break
        except:
            print('You must enter a number.')