"""
A guess the number game in Python

Insert the following words into the gaps (...) to make the program work:

    else
    finished
    int
    not
    number
    print
    randint

"""
from random import ...


... = randint(1, 100)
finished = False

print("""
Guess the number
================

I am thinking of a number between 1 and 100.
Try to find it with as few attempts as possible.

""")
n = 0

while ... finished:
    guess = ...(input("Enter your guess: "))
    n += 1

    if guess == number:
        print(f'\nYou found the number in {n} attempts')
        ... = True
    elif guess < number:
        print('\nThe number you entered is too small.')
    ...:
        ...('\nThe number you entered is too large.')
