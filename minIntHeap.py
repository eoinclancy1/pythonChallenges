# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:11:18 2018

@author: Eoin Clancy
"""

class MinIntHeap(object):
    
    #items = []
    
    def __init__(self, c=10):
        self.capacity = c
        self.size = 0
        self.items = []
        
    def getLeftChildIndex(self, parentIndex):
        return parentIndex*2 + 1
    
    def getRightChildIndex(self, parentIndex):
        return parentIndex*2 + 2
    
    def getParentIndex(self, childIndex):
        return int((childIndex-1)/2)
    
    def hasLeftChild(self, index):
        return (self.getLeftChildIndex(index) < self.size)
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]
    
    def parent(self, index):
        return self.items[self.getParentIndex(index)]



    def swap(self, indexOne, indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp
        
    def peek(self):
        if self.size == 0:
            raise IndexError
        return self.items[0]
    
    def poll(self):
        if self.size == 0:
            raise IndexError
        item = self.items[0]
        self.items[0] = self.items[self.size-1]
        self.size -= 1
        self.heapifyDown()
        return item
    
    def add(self, item):
        self.items.append(item)
        self.size += 1
        self.heapifyUp()
        
    
    def heapifyDown(self):
        index = 0
        while (self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if (self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            
            if (self.items[index] < self.items[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
                
    
    def heapifyUp(self):
        index = self.size - 1
        while (self.hasParent(index) and self.parent(index) > self.items[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
    
    
        
#    def getMedian(self):
#        if self.size == 0:
#            raise IndexError
#        if (self.size % 2 == 0):
#            halfway = int(self.size/2)
#            print(self.items)
#            print(halfway)
#            return round((self.items[halfway] + self.items[halfway-1])/2, 1)
#        else:
#            halfway = int(self.size/2)
#            print(self.items)
#            print(halfway)
#            return round(float(self.items[halfway]),1)
#    
        
    
#n = int(input().strip())
#a = MinIntHeap()
#a_i = 0
#for a_i in range(n):
#    a_t = int(input().strip())
#    a.add(a_t)
#    print(a.getMedian())
#    
    