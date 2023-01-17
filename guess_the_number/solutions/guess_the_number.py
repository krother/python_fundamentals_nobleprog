"""
a guess the number game in Python
"""
from random import randint

number = randint(1, 100)
finished = False

print("""
Guess the number
================

I am thinking of a number between 1 and 100.
Try to find it with as few attempts as possible.

""")
n = 0

while not finished:
    guess = int(input("Enter your guess: "))
    n += 1

    if guess == number:
        print(f'\nYou found the number in {n} attempts')
        finished = True
    elif guess < number:
        print('\nThe number you entered is too small.')
    else:
        print('\nThe number you entered is too large.')
