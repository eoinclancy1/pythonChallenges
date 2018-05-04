# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 01:40:45 2018

@author: Eoin Clancy
"""

def FibonacciMemoization(n, table = {}):
    if n <= 1:
        return n
    
    if n in table:
        return table[n]
    
    else:
        result = FibonacciMemoization(n-1) + FibonacciMemoization(n-2)
        table[n] = result
        return result
    
    

n = int(input())
print(FibonacciMemoization(n))
    