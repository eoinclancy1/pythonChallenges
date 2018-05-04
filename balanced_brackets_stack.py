# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 02:13:51 2018

@author: Eoin Clancy
"""

class Node(object):
    
     def __init__(self, data=None):
        self.data = data
        self.next = None

    


class Stack(object):
    
    def __init__(self):
        self.top = Node()
        self.size = 0
    
    def isEmpty(self):
        return self.top == None
        
    def peek(self):
        return self.top.data
        
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node 
        self.size += 1
        
    def pop(self):
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    def sizeStack(self):
        return self.size


def is_matched(expression):
    
    stack = Stack()
    open = "{ [ ("
    types = {'}':'{', ']':'[', ')':'('}
    for bracket in expression:
        if bracket in open:
            stack.push(bracket)
        else:
            if stack.sizeStack() > 0:
                if (types[bracket] == stack.peek()):
                    stack.pop()
            else:
                return False
    if stack.sizeStack() == 0:
        return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")