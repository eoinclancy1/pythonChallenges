# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:41:57 2018

@author: Eoin Clancy
"""


import sys

def solve1(arr, money):
    
    values = arr.copy()
    values.sort()
    
    
    #visited list
    #if val not in it -> delete all common values from the arr
    for x in range(len(values)):
        moneyRemaining = money - values[x]
        if (moneyRemaining > 0):
            result = findCostIndex(values, moneyRemaining)
            if (result > 0):
                first = arr.index(values[x])
                del arr[first]
                second = arr.index(values[result])
                if first < second:
                    print(str(first+1) + ' ' + str(second+2))
                else:
                    print(str(second+1) + ' ' + str(first+1))
                break


def findCostIndex(arr, money):
    
    ### array is pre-sorted, look for the value money, return true if found
    
    left = 0
    right = len(arr)-1

    while (left <= right):
        
        mid = int((left + right) / 2)
        
        if arr[mid] == money:
            return mid
        elif arr[mid] < money:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def solve(arr, money): ####### doesnt account for expansion to case where have to return 
    map = {}
    for pos in range(len(arr)):
        moneyRemaining = money - arr[pos]
        if moneyRemaining in arr:
            secondPos = arr.index(moneyRemaining)
            if pos < secondPos:
                print(str(pos+1) + ' ' + str(secondPos+1))
                break
            else:
                print(str(secondPos+1) + ' ' + str(pos+1))
                break


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
