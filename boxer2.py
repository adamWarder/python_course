#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Writes framed text centered on the terminal.
"""
import sys
import shutil


def main(args):
    """
    Gets `width` from `shutil.get_terminal_size()`, Prompts for `text`
    to center in a box, if a command line argument is not present. It
    uses ANSI/VT100 colours on output.
    """
    width = shutil.get_terminal_size().columns
    print('\x1B[2J\x1B[0H')

    if len(args) > 1:  # ←if argument available, use it.
        text = args[1]
    else:  # ←else prompt the user.
        text = input("Text?: ")

    txtlen = len(text)
    boxsze = txtlen + 6
    margin = " " * ((width - boxsze) // 2)

    hue_border = "\x1b[90m"  # ←dark gray
    hue_text = "\x1b[92m"  # ←green

    print(hue_border)
    print(margin + "┌" + "─" * (boxsze - 2) + "┐")
    print(margin + "│" + hue_text + " " * 2 + text +
          " " * 2 + hue_border + "│")
    print(margin + "└" + "─" * (boxsze - 2) + "┘")
    print("\x1b[0m")

    return 0  # ←‘success’ exit code.


if __name__ == "__main__":
    sys.exit(main(sys.argv))
