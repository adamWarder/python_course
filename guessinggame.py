#!/usr/bin/env python3
# -*- coding utf-8 -*-
# vim: set fenc=utf-8 et ts=4 sw=4 sts=4 :
"""
Guessing game
User must guess the generated value
"""

import sys
import random

SECRET = random.randint(1, 99)
MAX_TRIES = 10


def to_int(s, fail=None):
    """
    An exception-free “conversion” from a string to an `int`. Optionally,
    caller can specify what to return for invalid input (a default).
    """
    try:
        return int(s)
    except:
        return fail


def main():
    """
    Take SECRET, let user guess value
    compare valuse responder if lower or higher
    """
    # loop until number of guesses have been exceeded,
    # or the user guessed the `SECRET` number
    loopvalue = 0

    while loopvalue < 11:
        usergues = to_int(input("Guess a the secret number between 1 and 99: "))
        print("DEV_MODE, secret:", SECRET)
        # compare usr guess to SECRET
        # check if usergues is true and if its between 0 and 100
        if usergues and 0 < usergues < 100:

            if usergues > SECRET:
                print(
                    "Your guess",
                    usergues,
                    "is higher than secret.\nYou have",
                    11 - (loopvalue + 1),
                    "guesses left",
                )

            elif usergues < SECRET:
                print(
                    "Your guess",
                    usergues,
                    "is lower than secret.\nYou have",
                    11 - (loopvalue + 1),
                    "guesses left",
                )

            if usergues == SECRET:
                print("You guessed correctly! \nIt took you", loopvalue + 1, "times")
                exit()

            loopvalue = loopvalue + 1
        # invalid input
        else:
            print("Invalid input.\nYou have", 11 - (loopvalue + 1), "guesses left")
            loopvalue = loopvalue + 1
    else:
        print("Secret value was:", SECRET)
        exit()


if __name__ == "__main__":
    sys.exit(main())
