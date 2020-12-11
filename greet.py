#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fenc=utf-8 et ts=4 sts=4 sw=4 :
'''
Greet user/entity with a hearty ‘Hello’.
'''
import sys

def main(args):
    '''
    Calls `greet` function with command-line argument, or value
    obtained from user input.
    '''

    if len(sys.argv) > 2:
        subject = args[1]
        greeting = args[2]
    elif len(sys.argv) > 1:
        subject = args[1]
        greeting = None
    else:
        subject = input("Who to greet?: ")
        greeting = input("Greeting to use?: ")

    greet(subject, greeting)

    return 0


def greet (who, salutation='Hello'):
    '''
    Writes a greeting to standard output. If `None` or an empty
    string is passed, will use `World`.
    '''
    if not who:
        who = 'World'
    if not salutation:
        salutation = 'Hello'

    print(f'{salutation}, {who}!')


if __name__ == '__main__':
    sys.exit(main(sys.argv))
    