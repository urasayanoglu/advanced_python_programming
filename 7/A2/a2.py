#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a2.py
@Time       :   2023/04/20 10:14:51
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Define a class MyStr that has one attribute x whose initial value is given when an object is instantiated
                a method __str__ that returns the value of attribute x as a str
                Define a class AbstractStr that has ABC.Metaclass as type.
                Register MyStr to AbstractStr using register decorator. 

 

Test the registering with creating a list of integer and MyStr values and printing first only strings (no values are printed) and then all objects that are instances of AbstractStr.

e.g.

ms = [MyStr(10*i) if i%3==0 else i for i in range(10)]

for i in ms:
    if isinstance(i, str):
        print(i, end=' ') #  prints: 
print()
for i in ms:
    if isinstance(i, AbstractStr):
        print(str(i), end=' ') # prints: 0 30 60 90
print()
'''

from abc import ABC, ABCMeta

class MyStr:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return str(self.x)

class AbstractStr(ABC, metaclass=ABCMeta):
    pass


AbstractStr.register(MyStr)


if __name__ == "__main__":
    ms = [MyStr(10*i) if i%3==0 else i for i in range(10)]

    for i in ms:
        if isinstance(i, str):
            print(i, end=' ') #  prints: 
    print()
    for i in ms:
        if isinstance(i, AbstractStr):
            print(str(i), end=' ') # prints: 0 30 60 90
    print()