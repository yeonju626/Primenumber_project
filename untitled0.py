#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:33:33 2021

@author: yanzhujiang
"""

from math import floor, sqrt

def primes(n):
    '''Returns the set of primes between 2 and n, inclusive.'''
    primes = set(range(2, n+1))
    for k in range(2, floor(sqrt(n))+1):
        if k in primes:
            primes.difference_update( range(k**2, n+1, k) )
    return primes


val = input("Enter your value:")
print(primes(int(val)))
 
# End of provided functions