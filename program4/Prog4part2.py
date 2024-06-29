'''
email: sandra.connors@unds.edu
name: Sandra Jurado Connors
Ask for an integer value. 
Write a program that determines the largest value, 
other than the original value, 
that divides evenly into the input value. 
You will need the modulus operator in this program.
'''

def calculateLargest(int):
    largest = 0
    for i in range(1, int):
        if int % i == 0:
            largest = i
        # print(f'i is: {i}, {int} % {i} is: {int%i}, {int} // {i} is {int//i}')
        # print(f'Largest factor: {largest}')
    return largest

def main():
    integerValue = int(input('Enter value: '))
    # calculateLargest(36)
    print(calculateLargest(integerValue))

main()
