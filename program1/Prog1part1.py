'''
Assignment Make sure to create a file for program(s). 
Do not do the work in the Python Shell, you will need a file that you can upload into Gradescope for testing.  
Each part needs to be a separate file. Each file will have to have a specific file name. 
Input text for each part will be in red. Output text for each part will be in green. 
The prompts used when asking questions must end with a colon. 
The labels before each output value must also end with a colon for Gradescope to work. 
Questions MUST be asked in the requested order. 

Part 1 - Convert to seconds. Must be named Prog1part1.py 

1. Add a comment section to your program 

2. Prompt the user to enter three integers for hours, minutes and seconds. 
The prompts for input MUST be as demonstrated in the sample output (in red). 

3. Use variables with meaningful names 

4. Calculate and display the number of equivalent seconds. 
The output must be in the form of the number, followed by the word “seconds”. 
Sample Output Hours: 1 Minutes: 6 Seconds: 6 Total seconds: 3966
'''

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

def findSeconds(hours, minutes, seconds): 
    return hours*60**2+minutes*60+seconds

print("Total seconds: ", findSeconds(hours, minutes, seconds))