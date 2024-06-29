'''

Part 1 - must be named Prog2part1.py 
A bank charges a base fee of $10 per month, plus the following check fees for a commercial checking account: 
• $.12 each for less than 20 checks 
• $.10 each for 20–39 checks 
• $.08 each for 40–59 checks 
• $.06 each for 60 or more checks 
Write a program that asks for the number of checks written for the month. 
The program should then calculate and display the bank’s service fees for the month. Make sure to round the cost to two decimal places.  

'''



numOfChecks = int(input("Number of checks: "))

def monthlyFees(n): ### Question: What's the best way to pass input() as an argument to the function?
    baseFee = 10.00
    under20 = .12
    twentyTo39 = .1
    fortyTo59 = .08
    sixtyPlus = .06

    if n < 20:
        return n*under20+baseFee
    elif n < 40:
        return n*twentyTo39+baseFee
    elif n < 60:
        return n*fortyTo59+baseFee
    else:
        return n*sixtyPlus+baseFee
    
print(f'${monthlyFees(numOfChecks):.2f}')
# print('$', monthlyFees(numOfChecks), sep='')