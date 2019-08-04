# This is a guess the number game.
import random

print('Hello, choose a number greater than one.')
maxGuess = input()

# Ask the player to guess six times
def getSecretNumber(g):
    print('I am thinking of a number between 1 and ' + g)
    return random.randint(1, int(g))

def run(s):
    print()
    guessesTaken = 0
    g = 0
    for guessesTaken in range(1, 7):
        print('Take a guess.')
        g = int(input())
        if g < s:
            print('Your guess is too low')
        elif g > s:
            print('Your guess is too high')
        else:
            break  # This condition is the correct guess!
    if g == s:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(s))

run(getSecretNumber(maxGuess))




