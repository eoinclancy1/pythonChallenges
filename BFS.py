# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 00:49:45 2018

@author: Eoin Clancy
"""
import queue
class Node(object):
    
    def __init__(self, id):
        self.adjacent = []
        self.id = id
        
    def getId(self):
        return self.id
    
    def setAdjacent(self,node):
        self.adjacent.append(node)
        
    def getAdjacent(self):
        return self.adjacent
    
    
class Graph(object):
    
    
    
    def __init__(self, n):
        self.nodeLookup = {}
        self.nodeDistance = {}
        for i in range(n):
            self.nodeDistance[i] = -1      #Has no distance at the min
            self.nodeLookup[i] = Node(i)
    
    def getNode(self, id):
        return self.nodeLookup[id]
    
    
    def addEdge(self, source, destination):
        s = self.getNode(source)
        d = self.getNode(destination)
        
        s.setAdjacent(d)
        d.setAdjacent(s)
        
    def find_all_distances(self, source):
        
        nextToVisit = queue.Queue()
        visited = []
        nextToVisit.put(self.nodeLookup[source])
        self.nodeDistance[source] = 0 
        visited.append(self.nodeLookup[source])
        
        while not nextToVisit.empty():
            
            node = nextToVisit.get()
            
            for child in (node.getAdjacent()):
                if child not in visited:
                    
                    nextToVisit.put(child)
                    visited.append(child)
                    self.nodeDistance[child.getId()] = 6 + self.nodeDistance[node.getId()]
                    
                
              
        del self.nodeDistance[source]
        result = ''.join(str(val) + ' ' for key, val in self.nodeDistance.items())
        print(result)
    
    
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.addEdge(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)    
