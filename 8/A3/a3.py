#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a3.py
@Time       :   2023/04/26 15:00:08
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Define an infinite generator function that generates powers of two starting from a given integer or if none is given from 1 e.g. 21, 22,...
                Using list comprehension generate a list of tuples of exponents and powers of 2 from -2 to 2. 
                The printed list should be [(-2, 0.25), (-1, 0.5), (0, 1), (1, 2), (2, 4)]
'''

def powers_of_two(start=1):
    i = start
    while True:
        yield 2**i
        i += 1

if __name__ == "__main__":

    my_gen = powers_of_two(-2) 
    lst = [(i, my_gen.__next__()) for i in range(-2, 3)]
    print(lst)
