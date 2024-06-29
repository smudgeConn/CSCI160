'''
Sandra Jurado Connors

Write each of the following functions using Python. 
All functions can be in the same program. 
The function header MUST be written as specified. 
In your main code test all of the specified functions. 
Each function must have a comment block explaining what it does, what the parameters are and what the return value is. 
Please remember the following two guidelines: 
• unless the purpose of the function is to generate output DO NOT write to the screen within the function (output for debugging purposes does not apply) 
• unless the purpose of the function is to ask the user for a value DO NOT ask the user for a value within the function 
• If there are built-in functions in Python that can accomplish the require task DO NOT USE THEM. Write code that uses loops and/or decisions to meet the requirements of the functions. 
'''

from math import fabs
import random

def square(intValue):
    # returns the square of intValue
    return intValue**2

def sumOfSquares(intValue):
    # returns the sum of the squares from 1 to intValue
    # you MUST use a loop and the square function to determine the retuned value
    sum = 1
    for number in range(2, intValue + 1):
        sum += number**2
    return sum

def isOdd(intValue):
    # returns True if intValue is odd, otherwise returns False
    if (intValue % 2):
        return True

def isEven(intValue):
    # returns True if intValue is even, otherwise returns False
    # this function MUST use isOdd to determine the retuned value
    return not isOdd(intValue)

def compareTo(intValue1, intValue2):
    # returns -1 if intValue1 is less than intValue2
    # returns 1 if intValue1 is greater than intValue2
    # returns 0 if intValue 1 is equal to intValue2
    if intValue1 < intValue2:
        return -1
    if intValue1 > intValue2:
        return 1
    return 0

def maxMagnitude(*args):
    # refers to the distance of a value from zero
    # does not necessarily return the largest value
    # returns the value furthest from 0
    largest = 0
    for arg in args:
        if fabs(arg) > largest:
            largest = arg
    return largest

def daysInFebruary(year):
    # determines the number of days in February given a year
    # Feb has 28 days except for leap years, which have 29 days
    # the rules to determine a leap year: 
        # the year must be divisible by 4
        # every 100th year is not a leap year unless it is also divisible by 400
    hundrethYear = not(bool(year % 100))
    divisibleBy400 = not(bool(year % 400))
    divisibleByFour = not(bool(year % 4))
    if (hundrethYear and divisibleBy400) or (divisibleByFour and not hundrethYear):
        return 29
    return 28

def militaryToRegularTime(militaryTime):
    # accepts a single int that contains a ime in military time, 0000-2359
    # return a str that contains the equivalent 'regular' time with AM or PM as part of the returned values
    # put a blank space between the minutes and the AM/PM text (e.g. "5:00 AM")
    hours = '00'
    minutes = str(militaryTime)[-2:]
    amPM = 'AM'

    threeDigits = len(str(militaryTime)) == 3
    fourDigits = len(str(militaryTime)) == 4
    
    if threeDigits:
        hours = '0'+str(militaryTime)[0]
    if fourDigits and militaryTime < 1200:
        hours = str(militaryTime)[0] + str(militaryTime)[1]
    if fourDigits and militaryTime >= 1200:
        hours = int(str(militaryTime)[0] + str(militaryTime)[1]) - 12
        amPM = 'PM'
    return f'{hours}:{minutes} {amPM}'

def main():
    # intValue = random.randint(0, 2359)
    # print(f'Square Function: {square(intValue)}')
    # print(f'Sum of Squares Function: {sumOfSquares(intValue)}')
    # print(f'Is Odd Function: {isOdd(intValue)}')
    # print(f'Is Even Function: {isEven(intValue)}')
    # print(f'Compare To Function: {compareTo(intValue, intValue2=600)}')
    # print(f'Max Magnitude Function: {maxMagnitude(intValue, randint, randint)}')
    # print(f'Days in February Function: {daysInFebruary(intValue)}')
    # print(f'Military to Regular Time Function: {militaryToRegularTime(intValue)}')


if __name__ == "__main__":
    main()