#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple ‘addition’ program in Python
"""


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
    Promt the user for 2 numbers, 
    storing the results
    in order `A` & `B`. then 
    Calculate the sum of A + B storing C.
    Print the sum
    """
    print('Start adder.py')

    num = int(input("number (1..10)?: "))
    if num >= 1 and num <= 10:
        print("number = ", num)
    else:
        print("bad input")

    return 1


if __name__ == '__main__':
    main()
