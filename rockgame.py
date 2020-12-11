#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROCK - PAPER - SCISSORS
computer draws number
number assigned to element
user inputs their choice
program runs check assigns winner
"""

import sys
import math
import random


def main():
    # generate random number
    compRand = int(random.randint(0, 10))

    # call set function, pass generated number
    element = set_element(compRand)

    # get user input
    usrElement = str(input("Choose element \nrock, paper or scissors: "))

    # function testElement input against 3 elements
    def test_element(usrElement):
        if usrElement == "rock" and element == "paper":
            winner = "computer wins"
            return winner
        elif useElement == "rock" and element == "scissors":
            winner = "you win"
            return winner
            else:
                winner = "draw"
                return winner

        if usrElement == "paper":
            if element == "scissors":
                winner = "computer wins"
                return winner
            if element == "rock":
                winner = "you win"
                return winner
            else:
                winner = "draw"
                return winner

        if usrElement == "scissors":
            if element == "rock":
                winner = "computer wins"
                return winner
            if element == "paper":
                winner = "you win"
                return winner
            else:
                winner = "draw"
                return winner

        # not a valid input check
        else:
            winner = "invalid input"
            return winner

    winner = test_element(usrElement)

    # show the comp selection and user
    print(compRand, element, usrElement)

    # check fir invalid input
    if winner == "invalid input":
        print(winner)
        return main()
    else:
        print("\n\ncomputer drew: ", element,
              "\nyou drew: " + usrElement + "\n" + winner)

    return 0

# funtion to set generated number to element


def set_element(compRand):
    if 0 <= compRand <= 3:
        element = "paper"
        return element
    if 4 <= compRand <= 6:
        element = "scissors"
        return element
    # if 7 <= compRand <= 10:
    #     element = "rock"
    #     return element
    else:
        element = "rock"
        return element


if __name__ == '__main__':
    main()
