'''

Part 3 - Convert to dollars. Must be named Prog1part3.py 
1. Prompt the user to enter four integers: quarters, dimes, nickels and pennies. 
2. Calculate the total number of cents 
3. Convert from cents to dollars by dividing by 100.0 
4. Display the equivalent in dollars and cents, with a leading dollar sign and no space between the dollar sign and the value 
5. Output with no cents may display a single 0 after the decimal point, such as “$1.0”. 
Ensuring there are two places after the decimal point will be addressed later in the semester. 

'''
userInputQuarters = int(input("Quarters: "))
userInputDimes = int(input("Dimes: "))
userInputNickels = int(input("Nickels: "))
userInputPennies = int(input("Pennies: "))

def totalCents(Q, D, N, P):

    return (Q*.25)+(D*.1)+(N*.05)+(P*.01)

def convertCentsToDollars(totalCents):
    if totalCents > 100:
        dollars = totalCents/100
        leftoverCents = totalCents - dollars
        return "$"+dollars+leftoverCents
    else:
        return "$"+str(totalCents)

print(convertCentsToDollars(totalCents(userInputQuarters, userInputDimes, userInputNickels, userInputPennies)))