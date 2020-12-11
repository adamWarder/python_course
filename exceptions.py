#!/usr/bin/env python3
# -*- coding utf-8 -*-
# vim: set fenc=utf-8 et ts=4 sw=4 sts=4 :
"""
Multiple functions and exceptions
"""

import sys

def func():
    print("func() called...")
    raise ValueError("some error from some function")

def main():
    try:
        print("start of main()...")
        func()
    except ValueError as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return

    print("end of main()...")

if __name__ == "__main__":
    main()