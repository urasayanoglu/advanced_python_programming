#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a4.py
@Time       :   2023/04/26 15:06:45
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Create a list of 1000 random integers from 1...100000 (hint: random sample) and using map function create a list of even numbers from the original list and change the numbers to capital letters from A-Z (hint: ord(‘A’) is 65 chr(90) is Z.
'''
import random


if __name__ == "__main__":

    # Create a list of 1000 random integers from 65 .... 9
    lst = [random.randint(65, 90) for _ in range(1000)]

    # Use map() to create a list of even numbers and change them to capital letters from A-Z
    new_list = list(map(lambda x: chr(x) if x % 2 == 0 else x, lst))
    print(new_list)
