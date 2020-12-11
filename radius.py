#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program that 
calculates the 
area and
circumference of a circle, 
given a radius. 
Prompt the user for the radius. 
Validate the input. 
Remember, a radius cannot be negative. 
Hint: use math.pi
"""

import sys
import math


def main():

    # request usr input
    usrNum = to_float(input(
        "Please input  circle radius. \nSelect a number in the range from (1..10)?: "))

    # iput validaion
    if usrNum is None:
        print("Input is not a number", file=sys.stderr)
        sys.exit(1)
    if usrNum < 1 or usrNum > 10:
        print("Input is not in the 1 - 10 range", file=sys.stderr)
        sys.exit(2)

    print("Valid input, radius is: ", usrNum)

    # send user input to function
    circ = round(get_circumference(usrNum), 2)
    area = round(get_area(usrNum), 2)

    print("Circumference: ", circ)
    print("Area is: ", area)


def get_circumference(radius):
    '''
    Calculate circumference given a radius
    '''
    return 2 * math.pi * radius


def get_area(radius):
    '''
    Calculate area given a radius.
    '''
    return math.pi * pow(radius, 2)


def to_float(s, fail=None):
    """
    An exception-free “conversion” from a string to an `float`. Optionally,
    caller can specify what to return for invalid input (a default).
    """
    try:
        return float(s)
    except:
        return fail


if __name__ == '__main__':
    main()
