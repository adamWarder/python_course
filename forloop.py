#!/usr/bin/env python3
# -*- coding utf-8 -*-
# vim: set fenc=utf-8 et ts=4 sw=4 sts=4 :
"""
for loop in lists
"""

import sys


def main():
    mylist = ["A" * i for i in range(1, 10)]
    print("1", mylist)  # ⇒['A', 'AA', 'AAA']

    mylist2 = []
    for i in range(1, 14):
        mylist2.append("A" * i)
        print()
    print("2:", mylist2)

    print()
    mylist3 = []
    for i in range(1, 8):
        mylist3.append((i, i ** 2))
        print(i, ":\n", mylist3)

    lst4 = [i ** 2 for i in range(7) if i % 2 == 0]
    print()
    print("4:", i, lst4)
    return 0


if __name__ == "__main__":
    sys.exit(main())