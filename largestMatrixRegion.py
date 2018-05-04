# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 00:49:37 2018

@author: Eoin Clancy
"""


def getBiggestRegion(grid):
    
    maxValue = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            
            maxValue = max(maxValue, countRegion(i, j, grid))
    
    return maxValue
            
def countRegion(i, j, grid):
    if (not (i in range(len(grid)) and j in range(len(grid[0])))):
        return 0
    if (grid[i][j] == 0):
        return 0
    
    count = 1
    grid[i][j] = 0
    count += countRegion(i-1, j-1, grid)
    count += countRegion(i-1, j, grid)
    count += countRegion(i-1, j+1, grid)
    count += countRegion(i, j-1, grid)
    count += countRegion(i, j+1, grid)
    count += countRegion(i+1, j-1, grid)
    count += countRegion(i+1, j, grid)
    count += countRegion(i+1, j+1, grid)
    
    return count
    
    
    

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))