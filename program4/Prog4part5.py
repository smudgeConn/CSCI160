'''
email: sandra.connors@unds.edu
name: Sandra Jurado Connors
Ask for two integer values, a width and a height. 
Then ask for a single character. 
Draw a filled rectangle using the user input. 
You CANNOT use the string multiplier operator; you must print a single character in the print statement, 
and loops to create the sequence of characters.
'''

width = int(input('Enter width: '))
height = int(input('Enter height: '))
char = input('Enter character: ')
# width = 5
# height = 4
# char = '@'

wCount = 0
hCount = 0

for i in range(width * height):
    if hCount < height:
        if wCount < width-1:
            print(char, end='')
            wCount += 1
        if wCount == width-1:
            print(char, end='\n')
            wCount = 0
            hCount += 1
            
