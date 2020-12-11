#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
multiplier program.
"""

import sys


def main(args):
    """
    multiply the args from 1 - 12 and provide answer.
    """
    # Get `multiplier` from command-argument, else, prompt the user.
    if len(args) > 1:
        multiplier = int(args)
    else:
        multiplier = int(input("Multiplier?: "))

    # Validate that `multiplier` is in the range `1`..`12` inclusive.
    if 1 < multiplier > 12:
        print("Error. Out of range.", file=sys.stderr)
        return 1

    # print loop vrom 1 till 12
    for n in range(1, 12 + 1):
        print("{} x {} = {}".format(n, multiplier, n * multiplier))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
