#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple ‘Hello, World’ program in Python
"""


def main():
    """
    Writes a generic greeting, inputs a username whom it also greets
    """
    print('Hello, World!')
    name = input("What's your name?: ")
    print("Well, hello {0}!".format(name))
    return 0


if __name__ == '__main__':
    main()
    # sys.exit(main())

print(type(12.32))
print(type('A'))
print(type("B"))
