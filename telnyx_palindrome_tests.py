# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:56:21 2018

@author: Eoin Clancy
"""

import unittest
from telnyx_palindrome import palindromeCheck, convert_to_base, get_palindrome_using_bases


class TestFunctions(unittest.TestCase):
    
    def test_palindrom(self):
        """
        Tests validity of palindrome function
        Number/Word should read same forwards and backwards
        """
        
        pal1 = palindromeCheck("racecar")
        self.assertTrue(pal1)
        
        pal2 = palindromeCheck("notpalindrome")
        self.assertFalse(pal2)
        
        pal3 = palindromeCheck(111)
        self.assertTrue(pal3)
        
        pal4 = palindromeCheck(12345)
        self.assertFalse(pal4)
        
        pal5 = palindromeCheck("race_car")
        self.assertFalse(pal5)
        
        pal6 = palindromeCheck("1")
        self.assertTrue(pal6)
        
    def test_base_converter(self):
        """
        Tests validity of base converter function
        Current form returns solution as string
        """
        
        bconv1 = convert_to_base(17,2)
        self.assertEqual(bconv1, '10001')
        
        bconv2 = convert_to_base(16, 3)
        self.assertEqual(bconv2, '121')
        
        bconv3 = convert_to_base(567, 6)
        self.assertEqual(bconv3, '2343')
        
        
    def test_full_pal_func(self):
        """
        Run the function to check for smallest base where number is palindrome
        """
        
        first_twenty = [2,3,2,3,2,5,2,3,2,3,10,5,3,6,2,3,2,5,18,3]
        
        test_res = get_palindrome_using_bases(1, 20)
        
        for x in test_res:
            number = (x['decimal'])
            base = (x['smallest base in which the number is a palindrome'])
            self.assertTrue(first_twenty[number-1], base)
            
                
    
    
if __name__ == '__main__':
    unittest.main()
        