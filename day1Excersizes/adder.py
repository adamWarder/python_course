#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple ‘addition’ program in Python
"""


def main():
    """
    Promt the user for 2 numbers, 
    storing the results
    in order `A` & `B`. then 
    Calculate the sum of A + B storing C.
    Print the sum
    """
    print('Start adder.py')

    num = int(input("number (1..10)?: "))›
    if num >= 1 and num <= 10:
        print("number = ", num)
    else:
        print("bad input")

    A = input("Please input a value between 1  - 100: ")
    if int(A) in range(0, 101):
        B = input("Please input a value between 1  - 100: ")
        if int(B) in range(0, 101):
            C = int(A) + int(B)
            print("Answer is = ", C)
            return 1


if __name__ == '__main__':
    main()
