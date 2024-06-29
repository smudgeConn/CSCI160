'''
Part 2 - Convert from seconds. Must be named Prog1part2.py 
1. Add a comment section to your program. 
2. Prompt the user to enter one integer value, which will be the number of seconds 
3. Calculate and display the number of equivalent hours, minutes and seconds 
(refer to documentation and/or notes about integer division and the modulus or remainder operator). 
The output should be on a single line. Remember that there are 3600 seconds in an hour. 
'''

inputSeconds = int(input("Seconds: "))
hours = inputSeconds//60**2
minutes = inputSeconds//60 - hours * 60
if inputSeconds >= 3600:
    seconds = abs(hours*3600 + minutes*60 - inputSeconds)
elif inputSeconds >= 60:
    seconds = abs(minutes*60 - inputSeconds - hours*60)
else:
    seconds = inputSeconds
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)