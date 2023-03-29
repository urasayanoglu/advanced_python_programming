#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a1.py
@Time    :   2023/03/29 15:34:44
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite the following low-level code using high-level code (=recommended python code)

             num = 10
             l = [(i, i.__mul__(num.__sub__(i))) for i in range(1,11)]
'''

# High-level code
num = 10
l = [(i, i*(num-i)) for i in range(1,11)]
print(l)