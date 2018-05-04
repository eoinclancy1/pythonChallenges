# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 01:44:38 2018

@author: Eoin Clancy
"""





#!/bin/python3

import sys

def lonely_integer(a):
    
    value = 0
    for i in a:
        value ^= i    ## if you xor everything, eventually the odd number drops out
    return value


def lonely_integer1(a):
    
    while(len(a) > 0):
        
        first = a[0]
        del a[0]
        if first in a:
            del a[a.index(first)]
        else:
            return first
    
    return a[0]
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
