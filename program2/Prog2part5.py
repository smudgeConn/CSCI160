import math

'''

Ask for an integer value. 
State if the value is, or is not, within the 400’s, meaning is it a three-digit number which starts with 4. 
This can be done at least two different ways. DO NOT do this with strings, this must be a numeric process. 
Feel free to challenge yourself to find both ways. 
No bonus points, just bonus knowledge. 
The output must text similar to “Within range?” followed by “yes” if the value is within the specified range, 
and “no” if the value is not within the range. 
Note that for this output the text must end with a question mark instead of the usual colon

'''

number = (int(input("Enter an integer value: ")))

# First try
if math.floor(number / 100) == 4:
    print("Within range?", end="")
    print("yes")
else:
    print("Within range?", end="")
    print("no")

# Alternative attempt
# if number >= 400 and number <500:
#     print("Within range? yes")
# else:
#     print("Within Range? no")