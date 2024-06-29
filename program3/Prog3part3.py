'''
name:Sandra Jurado Connors
email:sandra.connors@ndus.edu


Write individual while loops in each of the following parts.
Part 3 – must be named Prog3part3.py 
Count from 0 to 10 (inclusive) by ½ - 
output one value per line and right justified with exactly 2 places in front of the decimal point and 
exactly 2 places after the decimal point. 
'''
i = 0.0
while i <= 10:
    print(f'{i:>5.2f}')
    i += .5