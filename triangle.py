#!/usr/bin/env python3
# -*- coding utf-8 -*-
# vim: set fenc=utf-8 et ts=4 sw=4 sts=4 :
"""
Triangle program

  #              #
 ###            ###
#####          #####
              #######
             #########
"""

import sys

def main(args):
    """
    Print a triangle given a base from args or the user input
    """
    if len(args) > 1:
        height = int(args)
    else:
        height = int(input("Height: "))

    for wdth in range(height):
        if not wdth % 2 == 0:
            spc = wdth*"#"
            print( spc.center(height))

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))