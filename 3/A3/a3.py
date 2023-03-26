#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a3.py
@Time    :   2023/03/22 22:48:51
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Write a script that defines a prime number generator e.g. primegen()  that has a default parameter max with a default value None.
             First, define a function that checks if a number is a prime.
             Prime numbers are integers that are divisible only with 1 and itself. 

Every number n can be written as n = a x b
If n is a perfect square, then a = b = √n.
And if a < b, then, a < √n and b > √n.
Else, if a > b, then a > √n and b < √n.
To test if a number is a prime loop through all integers up to n/2, or more efficiently up to √n. 

 
The generator is an infinite generator if the caller does not provide an integer number for the parameter max.  The generator breaks if the generated number is bigger or equal to the max.

Test the generator and print the prime number smaller than 1000

g = primegen(1000)
for i in g:
    print(i)
'''
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def primegen(max=None):
    n = 2
    while True:
        if max is not None and n >= max:
            break
        if is_prime(n):
            yield n
        n += 1


if __name__ == "__main__":
    g = primegen(1000)
    for i in g:
        print(i)