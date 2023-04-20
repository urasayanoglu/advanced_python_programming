#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a1.py
@Time       :   2023/04/20 09:52:58
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Define a class MyNum that has one attribute x whose initial value is given when an object is instantiated
                a method __index__ that returns the value of attribute x as an integer
                Define a class AbstractInt that has ABC.Metaclass as type.
                Register types int and MyNum to AbstractInt using register function. 

 

Test the registering with creating a list of integer and MyNum values and printing first only integers and then all objects that are instances of AbstractInt.

e.g.

mn = [MyNum(10*i) if i%3==0 else i for i in range(10)]
for i in mn:
    if isinstance(i, int):
        print(i, end=' ') #  prints: 1 2 4 5 7 8 
print()
for i in mn:
    if isinstance(i, AbstractInt):
        print(int(i), end=' ') #  prints: 0 1 2 30 4 5 60 7 8 90 
print()
'''

from abc import ABC, ABCMeta

class MyNum:

    def __init__(self, x):
        self.x = x
    
    def __index__(self):
        return int(self.x)

class AbstractInt(ABC, metaclass=ABCMeta):
    pass

AbstractInt.register(int)
AbstractInt.register(MyNum)

if __name__ == "__main__":
    mn = [MyNum(10*i) if i%3==0 else i for i in range(10)]
    for i in mn:
        if isinstance(i, int):
            print(i, end=' ') #  prints: 1 2 4 5 7 8 
    print()
    for i in mn:
        if isinstance(i, AbstractInt):
            print(int(i), end=' ') #  prints: 0 1 2 30 4 5 60 7 8 90 
    print()

