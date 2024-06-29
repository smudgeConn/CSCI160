'''
Name: Sandra Jurado Connors
Student ID Number: 1551539
Program Number: 6

Part 2:
Use input() to ask for a file name. 
Use the data file(s) created in part 1. 
Do not let the program crash if you enter the name of a file that does not exist. 
Detecting the existence of a file was discussed in class. 
If the file does not exist, gracefully display an error message stating the file does not exist 
and quit the program.  
If the file does exist, ask for a low limit and a high limit, in that order. 
Then read all the values in the file. 
You will only need to read the file once, or more to the point, only read the file once. 
After the program has finished reading all the data, display the following information to the screen. 
The MUST be in the order specified, with any preceding text on the line ending with a colon.  
The total number of values that fell within the range
The minimum value. This will be equal to, or greater, than the input low limit.
The maximum value. This will be equal to, or less than the input high limit.
If any values were equal to the high limit. 
NO output if none of the values were equal to the high limit. 
The text “Found value of high limit” must be in the text, if displayed. 
Do not use a colon in this text. 
If any values were equal to the low limit. 
NO output if none of the values were equal to the low limit. 
The text “Found value of low limit” must be in the text, if displayed. 
Do not use a colon in this text.
The average of the scores within the range - display with 2 places after the decimal point.
If no data exists in the file, write out a simple message indicating that there was 
no data in the file and nothing else.
'''

# fileName = input('What is the name of the file? ')
import os
fileName = 'part1file.txt'
if fileName not in os.listdir():
      print("The file does not exist.")
else:
    with open (fileName, 'r') as file:
        lowLimit = float(input("Enter the low limit: "))
        highLimit = float(input("Enter the high limit: "))
        totalNumOfValues = 0
        lowValue = -6
        maxValue = -6
        equalToHighLimit = False
        equalToLowLimit = False
        sum = 0
        for line in file:
            if line == '':
                 print('No data in the file.')
            if lowLimit <= float(line) <= highLimit:
                 sum = sum + float(line)
            if lowLimit <= float(line) < lowValue:
                 lowValue = float(line)
                 totalNumOfValues= totalNumOfValues + 1
            if maxValue < float(line) <= highLimit:
                 maxValue = float(line)
                 totalNumOfValues= totalNumOfValues + 1
            if float(line) == highLimit:
                 equalToHighLimit = True
            if float(line) == lowLimit:
                 equalToLowLimit = True
            average = sum / totalNumOfValues
            
        print(f'Total number of values: {totalNumOfValues}') 
        if lowValue > -6:
              print(f'Low value: {lowValue}')
        if maxValue > -6:
              print(f'High value: {maxValue}')
        if equalToHighLimit:
            print(f'Found value of high limit.')
        if equalToLowLimit:
            print(f'Found value of low limit.')
        print(f'Average: {average:0.2f}')