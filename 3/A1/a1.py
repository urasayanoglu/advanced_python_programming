#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a1.py
@Time    :   2023/03/22 22:44:36
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Write a script that defines an infinite generator e.g. primegen() of prime numbers.
             First, define a function that checks if a number is a prime.
             Prime numbers are integers that are divisible only with 1 and itself. 

Every number n can be written as n = a x b
If n is a perfect square, then a = b = √n.
And if a < b, then, a < √n and b > √n.
Else, if a > b, then a > √n and b < √n.
To test if a number is a prime loop through all integers up to n/2, or more efficiently up to √n. 

 

Then define a function that loops infinitely generating integers from 1 up and verifies if a number is a prime. 
If it is, it returns the number to the caller of the function and continues with the next number.

 

Test the generator and print the prime number smaller than 1000

g = primegen()
while True:
    p = next(g)
    if p >= 1000:
        break
    print(p)


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

def primegen():
    """
    An infinite generator that yields prime numbers.
    """
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


if __name__ == "__main__":
    g = primegen()
    while True:
        p = next(g)
        if p >= 1000:
            break
        print(p)