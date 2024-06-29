'''
name:Sandra Jurado Connors
email:sandra.connors@ndus.edu

Write individual while loops in each of the following parts
Part 1
Ask for an integer ending value. It will be a positive value. 
Count from 0 to the ending value (inclusive) by 1 - output one value per line.
'''
import math
inputValue = int(math.fabs(int(input("Integer ending value: "))))
# print(type(inputValue))
# for i in range(inputValue+1):
#     print(i)
i = 0
while i <= inputValue:
    print(i)
    i+=1