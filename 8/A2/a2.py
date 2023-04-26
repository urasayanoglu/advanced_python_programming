#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a5.py
@Time       :   2023/04/26 14:34:47
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Create a generator expression that generates multiples of 2’s powers until a num is reached e.g. if the num = 6 the generator generates 20 , 21 ,,26
                Test the generator with the following code where the gen is your generator expression

for j in gen:
    print(j)
'''

if __name__ == "__main__":

    num = 6
    gen = (2**i * j for i in range(num) for j in range(1, 2**(num-i)))

    for j in gen:
        print(j)