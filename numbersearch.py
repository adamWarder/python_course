#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NUMBER SEARCH
VERSION 1 
generate list from 1-100
computer draws number search from list.
"""

import sys
import random
from time import process_time


def main():
    """
    get generated list find middle value
    sort list if not sorted - but list is generated
    """

    MIN, MAX = 1, 80000
    selected = random.randint(MIN, MAX)
    genlist = list(range(MIN, MAX))
    count = 1

    # print(genlist)
    print(selected)

    # loop through genlist
    #  if selected is smaller than middle change MIN to middle
    #  if selected is larger than middle change MIN to middle

    # get list lenght
    lowwer = 0
    upper = len(genlist) - 1

    # start loop
    while lowwer <= upper:
        # start timer
        starttime = process_time()
        # find middle of list
        middle = round((lowwer + upper) / 2)
        # found the selected value
        if selected == middle:
            count = count + 1
            print("Found: ", selected, ", in:", count, "loops")
            # end timer
            endtime = process_time()
            print("\ntotal time to compleate search:", endtime - starttime)
            exit()
        elif selected < middle:
            upper = middle - 1
            count = count + 1
        else:
            lowwer = middle + 1
            count = count + 1

    print("middle: ", middle)
    print("count: ", count)

    return 0


if __name__ == "__main__":
    sys.exit(main())
