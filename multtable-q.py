#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module documentation. Write something meaningful here.
"""

import sys

def main(args):
    """
    Documentation for `main`. Write something meaningful here.
    """
    # Get `multiplier` from command-argument, else, prompt the user.
    usrinput = int(input("input multiplier (1-12)?: "))
    print(usrinput)

    if 0 <= usrinput <= 13:
        multiplier = int(usrinput)
        print('12312',multiplier)
    else:
        multiplier = int(input("Multiplier?: "))

    # Validate that `multiplier` is in the range `1`..`12` inclusive.
    if 1 >= multiplier <= 12:
        print("Error. Out of range.", file=sys.stderr)
        return 1

    for n in range(1, 12+1):
        print(n, 'x', multiplier , '= ', n*multiplier)

    return 0

if __name__ == '__main__':
   sys.exit(main(sys.argv))