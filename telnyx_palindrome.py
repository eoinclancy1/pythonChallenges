# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:39:33 2018

@author: Eoin Clancy
"""

import pandas as pd

def palindromeCheck(x):
    """
    Check that x is read the same both forwards and backwards
    input: x of type int or string
    output: boolean
    """
    
    str_x = str(x)
    return str_x == str_x[::-1]

def convert_to_base(num, base):
    """
    Covert number to specified base
    input: num as int
           base as int
    output: num to base as string
    """
    
    if num < base:
        return num
    
    dividing = True
    result = []
    quotient = num
    
    while dividing:
        
        rem = quotient % base
        quotient = quotient // base
        
        result.append(rem)
        
        if quotient == base:
            result.append(0)
            result.append(1)
            dividing = False
        elif quotient < base:
            result.append(quotient)
            dividing = False 
    
    return ''.join(str(n) for n in result[::-1])



def get_palindrome_using_bases(start, end):
    """
    Specify range of number for which to find the smallest base 
         in which each individual number is a palindrome
    input: start as int - first number in range to use
           end as int - last number in range to use
    output: list of dictionaries of form
            {'decimal' : n, 
            'smallest base in which the number is a palindrome' : b}
    """
    
    answers = []
    
    for n in range(start, end+1):
        
        b = 1
        converged = False
        while not converged:
            b = b + 1
            val = convert_to_base(n, b)
            converged = palindromeCheck(val)
            
        answers.append({'decimal' : n, 'smallest base in which the number is a palindrome' : b})
    return answers
    


answer = get_palindrome_using_bases(1,1000)
df = pd.DataFrame(answer)
df.to_csv("data.csv", index=False)

