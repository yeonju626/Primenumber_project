#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:33:33 2021

@author: yanzhujiang
"""

from math import floor, sqrt

def primes(n):
    #Returns the set of primes between 2 and n, inclusive.
    primes = set(range(2, n+1)) #set contains all the integers between 2 and n
    for k in range(2, floor(sqrt(n))+1): #for every integer in the range of 2 and square root of n
        if k in primes: 
            primes.difference_update( range(k**2, n+1, k) ) #compares the set primes and the set of the integers whose square root is k and can be devided by k (bigger than k)
                                                            #and take out the repeated integer from primes
    return primes



def which_prime(n):
    var = primes(n) #save the prime set into val
    if n in var: #if the n is in the set then print the length of the set 
        var = len(primes(n))
        print("The number is ", len(primes(n)), "th prime number" )
        

        #print(len(primes(n)))
val = input("Enter your value:")
print(primes(int(val)))
if int(val) in primes(int(val)): #if the user's input is in the prime set
    which_prime(int(val)) #print where the prime number is in the set
else:
    print("This is not a prime number") #if the input is not a prime number than tell the closest  prime number of the input
    print("The closest prime number is ",max(primes(int(val))))
    
# End of provided functions