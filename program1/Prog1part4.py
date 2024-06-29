'''

Part 4 - Work with output. Must be named Prog1part4.py 
Write a program that asks the user their first name, last name, current address, city, state, and zip code. 
Then write a mailing label to the screen exactly as laid out below. This MUST be done with exactly 6 print statements. 
Understanding the sep= and end= print options will be helpful. There is no output other than the mailing label.

'''

first = input("First: ")
last = input("Last: ")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zip = input("Zip: ")

print(first, end=' ')
print(last)
print(address)
print(city+", ", end='')
print(state+"  ", end='')
print(zip)
