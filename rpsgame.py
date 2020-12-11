#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROCK - PAPER - SCISSORS
VERSION 2 
computer draws number
number assigned to element
user inputs their choice
program runs check assigns winner
"""

import random


def main():
    """
    comp draws element
    """
    # generate random number
    #   assign element to number
    elements = {1: "scissors", 2: "paper", 3: "rock"}
    compelement = random.randint(0, 10)

    if 0 < compelement > 3:
        compelement = str("scissors")
    elif 3 < compelement > 6:
        compelement = str("paper")
    else:
        compelement = str("rock")

    # user input element
    #   check if elelment is valid
    #   check if user element and comp element are matching
    userelement = input("Input rock, paper or scissors: ")

    # check if userinout is in dictionary
    if userelement in elements.values():
        print("good")
    else:
        # request new input
        userelement = input("Input rock, paper or scissors: ")

    # if input is valid
    #   do winner check

    # check for draw
    if userelement == compelement:
        print("comp:", compelement, ", user: ", userelement)
        print("DRAW")

    # user element rock
    elif userelement == "rock" and compelement == "scissors":
        print("comp:", compelement, ", user: ", userelement)
        print("WIN")
    elif userelement == "rock" and compelement == "paper":
        print("comp:", compelement, ", user: ", userelement)
        print("LOSE")

    # user element paper
    elif userelement == "paper" and compelement == "rock":
        print("comp:", compelement, ", user: ", userelement)
        print("WIN")
    elif userelement == "paper" and compelement == "scissors":
        print("comp:", compelement, ", user: ", userelement)
        print("LOSE")

    # user element scissors
    elif userelement == "scissors" and compelement == "rock":
        print("comp:", compelement, ", user: ", userelement)
        print("WIN")
    elif userelement == "scissors" and compelement == "paper":
        print("comp:", compelement, ", user: ", userelement)
        print("LOSE")

    return 0


if __name__ == "__main__":
    main()
