# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 01:14:42 2018

@author: Eoin Clancy
"""

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        if not self.stack2:
            self.moveStack1ToStack2()
        return (self.stack2[len(self.stack2)-1])
        
    def pop(self):
        if not self.stack2:
            self.moveStack1ToStack2()
        return self.stack2.pop()
        
    def put(self, value):
        self.stack1.append(value)
        
    def moveStack1ToStack2(self):
        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        
        


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())