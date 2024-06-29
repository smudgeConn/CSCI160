'''
email: sandra.connors@unds.edu
name: Sandra Jurado Connors
Ask for an integer value. 
Write a program that determines the smallest value, other than 1, that divides evenly into the input value. 
You will need the modulus operator in this program.
'''

def calculateSmallest(int):
    smallest = 0
    list = []

    for i in range(2, int):
        if int % i == 0:
            list.append(i)
    list.sort()
    print(list[0])
    

def main():
    # calculateSmallest(44)
    integerValue = int(input('Enter value: '))
    calculateSmallest(integerValue)

main()
