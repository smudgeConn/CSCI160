'''
email: sandra.connors@unds.edu
name: Sandra Jurado Connors
Ask for an integer value. 
Write a program that calculates the factorial of the input number. 
The factorial of a number is determined by multiplying all number 
from 1 to the input number. 
For example, the factorial of 6 is 1 * 2 * 3 * 4 * 5 * 6, or 720.
'''


def calculateFactorial(integer):
    factorial = 1
    for i in range(1, integer+1):
        factorial = factorial * i
    print(f'Factorial: {factorial}')

def main():
    integerValue = int(input('Enter value: '))
    calculateFactorial(integerValue)

main()
