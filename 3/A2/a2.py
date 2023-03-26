#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a2.py
@Time    :   2023/03/22 22:47:23
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Write a script that defines a prime number generator e.g. primegen()  that has a parameter max with a default value None.
             First, define a function that checks if a number is a prime.
             Prime numbers are integers that are divisible only with 1 and itself. 

Every number n can be written as n = a x b
If n is a perfect square, then a = b = √n.
And if a < b, then, a < √n and b > √n.
Else, if a > b, then a > √n and b < √n.
To test if a number is a prime loop through all integers up to n/2, or more efficiently up to √n. 

 

The generator is an infinite generator if the caller does not provide an integer number for the parameter max.  
If the generated number is bigger or equal to the max, the generator raises StopIteration error:

raise StopIteration()

Test the generator and print the prime number smaller than 1000

g = primegen(1000)
while True:
    try:
        print(next(g))
    except Exception as ex:
        print(ex)
        break
'''
import math

def is_prime(num):
    """
    Checks if a number is prime or not.
    """
    if num < 2:
        return False
    
    # Check divisibility up to the square root of num
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True

def primegen(max=None):
    """Generates prime numbers up to a maximum value (if provided)."""
    n = 2
    while True:
        if max is not None and n > max:
            raise StopIteration()
        if is_prime(n):
            yield n
        n += 1

if __name__ == "__main__":
    g = primegen(1000)
    while True:
        try:
            print(next(g))
        except Exception as ex:
            print(ex)
            break