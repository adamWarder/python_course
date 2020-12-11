#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dictionary Excersise
"""
import itertools

def main():
    """
    Dictionary Excersise
    """
    d = {"one": 1, "two": 2, "three": 3, "four": 4}
    print('d: ', d)

    dvalues = list(d.values())
    print('list(d.values()): ', dvalues)

    # reverse list and items
    revd = list(reversed(d))
    revditems = list(reversed(d.items()))
    print('reversed d: ', revd, '\nreversed d items: ', revditems)

    # iteration
    print('\n\niteration')
    dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
    keys = dishes.keys()
    values = dishes.values()
    n = 0
    for val in values:
        n += val
    print(n)
    
    # iteration over dictionaries
    print('\n\n iteration in dictionaries')
    r = {'x': 1, 'y': 2, 'z': 3}
    for key in r:
        print(key, 'corresponds to', r[key])

     # parallel iteration over dictionaries
    print('\n\n parallel iteration in dictionaries')
    j = 0
    names = {'adam', 'mervin', 'nev', 'briliant'}
    age = {30, 28, 33, 38}
    for j in range(len(names)):
        print(names[j], 'is', ages[j], 'years old')

    return 0


if __name__ == "__main__":
    main()
 