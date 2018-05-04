# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 17:21:19 2018

@author: Eoin Clancy
"""

from heapq import heappush as push, heappushpop as pushpop

class Spliter:
    def __init__(self):
        self.upper = []
        self.lower = []
        
    def median(self):
        if len(self.upper) > len(self.lower):
            return round(self.upper[0]/1.0, 1)
        else:
            return (self.upper[0] - self.lower[0]) / 2.
        
    def add(self, value):
        value = pushpop(self.upper, value)          #pushpop pushes the value first and then pops the smallest value on the heap
        print("value1   " +str(value))         #used to store the largest numbers
        print(self.upper)
        value = -pushpop(self.lower, -value)        #storing the values in their negative form - therefore the more negative a value is, the smaller it is taken to be
        print("value2   " +str(value))         # i.e   -1000 < -9, therefore, it is still a min heap, but the negative sign implements it as a max heap
        print(self.lower)                      # so -1000 would be stored at the top, becuase it is the smallest, but also popping the smallest value here each time
        
        # have found the odd value to be moved, either too small for upper, or too big for lower
        
        if len(self.upper) <= len(self.lower):     # upper should always be 1 greater or equal to lower 
            push(self.upper, value)
        else:
            push(self.lower, -value)                # add to lower
            
            
n = int(input().strip())
a = Spliter()
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.add(a_t)
    print(a.median())
    
    
    