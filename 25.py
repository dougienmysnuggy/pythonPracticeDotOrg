'''
In a previous exercise, we’ve written a program that “knows” a number 
and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will
have in your head a number between 0 and 100. The program will guess a
number, and you, the user, will say whether it is too high, too low, or
your number.

At the end of this exchange, your program should print out how many guesses
it took to get your number.

As the writer of this program, you will have to choose how your program will 
strategically guess. A naive strategy can be to simply start the guessing at 1, 
and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an 
optimal guessing strategy. An alternate strategy might be to guess 50 (right in 
the middle of the range), and then increase / decrease by 1 as needed. After 
you’ve written the program, try to find the optimal strategy! (We’ll talk about 
what is the optimal one next week with the solution.)
'''

import time

def check_guess(cpu_guess):
    guess_result = input('Was the guess correct/higher/lower (C/H/L)? ')
    if guess_result.upper() not in ['C', 'H', 'L']:
        print('Invalid entry. Valid entries: C, H, or L')
        check_guess(cpu_guess)
    return guess_result.upper()

def guess_number(f, l):
    # Uses a binary search type algorith to guess the number
    guesses = 0
    found = False
    while not found:
        cpu_guess = (f + l) // 2
        print('My guess: {}'.format(cpu_guess))
        result = check_guess(cpu_guess)
        guesses += 1
        if result == 'H':
            l = cpu_guess - 1
        elif result == 'L':
            f = cpu_guess + 1
        else:
            found = True
        if not found:
            print('Coming up with a new guess...')
            time.sleep(1)
    return guesses

print('Think of a number between 1 & 100. You have 5 seconds to decide...')
time.sleep(5)
print('Now I\'m going to guess that number...')
time.sleep(1)
guesses = guess_number(1, 100)
print('It only took me {} guesses to get the number!'.format(str(guesses)))

