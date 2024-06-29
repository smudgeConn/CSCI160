'''

Part 3 – must be named Prog2part3.py 

In this order, ask for a number (float), a math operator (string), and another number (float). 
Then perform the requested mathematical operation. 
The only valid operations are "+", "-", "*", "/", and "//". 
This program will not address the modulus operator. 
• Do not worry about the denominator being 0 for division. That WILL NOT be part of the test data. 
0 is a valid value for addition, subtract, multiplication or as the numerator when performing division. 
• No error checking is required. You can assume all values enter for numbers will “look like “valid numbers, 
and not cause an error when cast to a float

'''

num1 = float(input("Enter the first number: "))
operator = str(input("Enter the operation: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print(num1//num2)