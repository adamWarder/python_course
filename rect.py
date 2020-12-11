#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Print a rectangle given a width
"""

import sys


def main(args):
    """
    Print a rectangle given a width form args or the user input
    """
    # check if command-line argument is available:
    #   use command-line argument
    # else:
    #   get from user(user `input`)
    if len(args) < 1:
        rectwidth = int(args[1])
    else:
        rectwidth = int(input("Rectangle width?: "))

    # if width is not in range (1 .. 20)
    #   print error messgae and
    #   return a non-zero exit code
    if rectwidth < 1 or rectwidth > 20:
        print("Error. ", rectwidth, " is out of range.", file=sys.stderr)
        return 1

    # print `width` nubmber lines
    #   print `width` number of `#`

    # this will print out a solit rectangle

    for wdth in range(rectwidth):
        print(20 * "#")
    print("\n")

    # the `#` will increase every loop
    for wdth in range(rectwidth):
        print(wdth * "#")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
