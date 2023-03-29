#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a3.py
@Time    :   2023/03/29 15:45:24
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite the following low-level code using high-level code (=recommended python code). 
             from random import random

              x = random() * 100000
              x1 = x.__round__(3)
              x2 = x.__mul__(1000).__trunc__().__truediv__(1000)

              print(x, x1, x2, sep='\n')
'''

# High-level code

from random import random

x = random() * 100000
x1 = round(x, 3)
x2 = round(x * 1000) / 1000
print(x, x1, x2, sep='\n')

