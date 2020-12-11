#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Experimenting with List
"""

import sys


def main():
    '''
    count
    '''
    a = ['to', 'be', 'or', 'not', 'to', 'be']
    print(a.count('to'))

    b = [[1, 2], 1, 1, [2, 1, [1, 2]]]
    print(b.count(1))
    print(b.count([1, 2]))
    print("\n")

    '''
    extend
    '''
    c = [1, 2, 3]
    d = [4, 5, 6]

    c.extend(d)
    print(c)
    print("\n")

    '''
    index
    '''
    knights = ["We", "are", "the", "knights", "who", "say", "ni"]
    print("knights = ", knights.index("who"))
    print("\n")

    x = [1, 2, 3, 4, 5, 6]
    x.pop()
    print(x)

    x.append(x.pop())
    print(x)

    '''
    reverse
    '''
    x.reverse()
    print(x)
    print("\n")

    '''
    sort
    '''
    y = [2, 5, 7, 4, 9, 8, 1, 3]
    print(y)
    y.sort()
    print(y)

    return 0


if __name__ == '__main__':
    main()
