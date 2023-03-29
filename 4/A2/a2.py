#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a2.py
@Time    :   2023/03/29 15:38:30
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite the following low-level code using high-level code (=recommended python code).

             The code assigns dynamically an attribute id with a random integer as value to each instance of A and adds the instance to list l. 

 

            from random import randint

            class A:
                pass

            l = []

            for _ in range(10):
                temp = A()
                temp.__setattr__('id', randint(1000, 10000))
                l.append(temp)

            for item in l:
                print(item.__getattribute__('id'))
'''
# High level code
from random import randint

class A:
    pass

l = []

for _ in range(10):
    temp = A()
    temp.id = randint(1000, 10000)
    l.append(temp)

for item in l:
    print(item.id)
