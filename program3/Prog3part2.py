'''
name:Sandra Jurado Connors
email:sandra.connors@ndus.edu


Write individual while loops in each of the following parts.
Part 2 – must be named Prog3part2.py Ask for an integer starting value. 
It will be a positive value. 
Count from the starting value down to 0 (inclusive, counting down by 1 – 
all output must be on a single line with a single place between all values.  
'''
import math

startingValue = int(input("Integer starting value: "))

while startingValue >= 0:
    print(startingValue, end=' ')
    startingValue -= 1