# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 01:42:59 2018

@author: Eoin Clancy
"""

#def make_change(coins, n):
#    lookup = [1] + [0] * n
#    print(lookup)
#    for coin in coins:
#        for i in range(n+1-coin):
#            lookup[i+coin] += lookup[i]
#            #print("coin: " +str(coin))
#            #print("i: " +str(i))
#            #print("lookup[i]: " +str(lookup[i]))
#            #print("lookup[i+coin]: " + str(lookup[i+coin]))
#            print(lookup)
#    return lookup[n]
#
#
#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]
#coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
#print(make_change(coins, n))


#my way - help from video - https://www.youtube.com/watch?v=jaNZ83Q3QGc

def make_change(coins, n):
    combinations = [1] + [0]*n 
    for coin in coins:
        for i in range(len(combinations)):
            if i >= coin:
                combinations[i] += combinations[i-coin]
    return combinations[n]
    
    
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))