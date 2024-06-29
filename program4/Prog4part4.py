'''
email: sandra.connors@unds.edu
name: Sandra Jurado Connors
Ask for a string to be searched and a single character (also a string value). 
Tell how many times that single character occurs within the initial string. 
You CANNOT use the count method, you must use a for loop to make a decision and count the occurrences. 
To match, the letters must be the same case. In the example below, the character to count does not match the capital T.
'''

# stringToSearch = 'This is the sample text.'
# charToCount = 't'

stringToSearch = input('String to search: ')
charToCount = input('Character to count: ')
total = 0

for char in stringToSearch:
    if char == charToCount:
        total += 1
        
print(total)
