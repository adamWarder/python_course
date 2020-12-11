#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Experimenting with print
Excersize 1

"""

import sys


def main():
    print("First text", end="")
    print(" more text", end=" ")
    print("last text")
    print('\n')

    print("ONE", "TWO", "THREE", "FOUR")
    print("ONE", "TWO", "THREE", "FOUR", sep=", ")
    print("ONE", "TWO", "THREE", "FOUR", sep=", ", end=".\n")
    print("ONE", "TWO", "THREE", "FOUR", end="!!\n", sep="; ")
    print('\n')

    print("On the next line")
    print("1) Written to standard output.")
    print("2) Written to standard output too.", file=sys.stdout)
    print("3) Written to standard error.", file=sys.stderr)

    return 0


if __name__ == '__main__':
    main()
