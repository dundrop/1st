# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
myAge = input('What is your age?\n')
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
if int(myAge) > 50:
    print('You will dye soon')
else:
    print('Chipper lad arn\'t ya?')
"""
Fizzbuzz

Given a number n from the console:

If n is divisible by 2, print "Fizz"
If n is divisible by 3, print "Buzz"
Or, if n is divisible by 2 and 3, print "Fizzbuzz"
Don't print anything otherwise
"""
