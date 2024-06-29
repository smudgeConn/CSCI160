'''
email: sandra.connors@unds.edu
name: Sandra Jurado Connors
Write a program that asks for integer values until the user enters 0. 
Once the user has finished entering values, display the average of the positive values that were entered 
and the average of the negative values that were entered. 
DO NOT make any assumptions regarding the data that will be entered. 
If you are not able to calculate an average, print “N/A” for the average. 
Each calculated average should be displayed with 2 places after the decimal point.
'''
import math
posValues = []
negValues = []
exit = False #if False then 0 has not been entered yet
turns = 0
while exit == False:
    value = int(input('Enter a value: '))
    if value == 0:
        exit = True
    if value < 0:
        negValues.append(value)
        turns += 1
    if value > 0: 
        posValues.append(value)
        turns += 1

if len(posValues) == 0:
    print(f'Average of positive values:\tN/A')
elif len(posValues) > 0:
    print(f'Average of positive vlaues:\t{math.fsum(posValues) / len(posValues):1.2f}')

if len(negValues) == 0:
    print(f'Average of negitive values:\tN/A')
elif len(negValues) > 0:
    print(f'Average of negative vlaues:\t{math.fsum(negValues) / len(negValues):1.2f}')
