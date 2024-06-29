'''
name:Sandra Jurado Connors
email:sandra.connors@ndus.edu


Write individual while loops in each of the following parts.
Part 5 – must be named Prog3part5.py 
Ask for the starting value and ending values. Both values will be integers. 
Count from the starting value to the ending value by 1, regardless if you need to count up or count down. 
The output should include both the starting value and ending value
'''

start = int(input('Enter starting value: '))
end = int(input('Enter ending value: '))

if start > end:
    while start >= end:
        print(start)
        start -= 1
else:
    while start <= end:
        print(start)
        start += 1