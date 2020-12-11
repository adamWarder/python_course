#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Excersize with overwrithing list
"""

import sys

names = ['AAAAA', 'BBBBB']
n = names

def change(n):
    n[0] = 'ZZZZ'
    print(n)

names = ['AAAAA', 'BBBBB']
change(n)                   
print(names)                

names = ['AAAAA', 'CCCCC']
change(names[:])            #⇒['ZZZZZ', 'BBBBB']
print(names)                #⇒['AAAAA', 'BBBBB']


