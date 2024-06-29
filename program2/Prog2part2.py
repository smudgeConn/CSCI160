'''

Create a program that asks the user for an x and y value, both integer values. 
Ask for the values one at a time. Then, using the standard notation for identifying a point (x and y inside parenthesis, 
separated by a comma), repeat the location and the Cartesian coordinate quadrant in which the x,y position is located. 
You can assume that neither x or y will be 0. Use the image below for quadrant information. 
Your output must contain the word “quadrant”, the blank space and your calculated result in Roman numerals.

'''

xValue = int(input("x: "))
yValue = int(input("y: "))

def findQuadrant(x, y):
    if x > 0 and y > 0:
        return 'quadrant I'
    elif x < 0 and y > 0:
        return 'quadrant II'
    elif x < 0 and y < 0:
        return 'quadrant III'
    elif x > 0 and y < 0:
        return 'quadrant IV'


print(f'({xValue}, {yValue}) is in: {findQuadrant(xValue, yValue)}')