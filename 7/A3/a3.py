#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a3.py
@Time       :   2023/04/20 10:25:03
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Define classes:

MyNum that has one attribute x whose initial value is given when an object is instantiated a method __index__ that returns the value of attribute x as an integer

MyStr that has one attribute x whose initial value is given when an object is instantiated a method __str__ that returns the value of attribute x as a str

MyX that has one attribute xl whose initial value is a list of argument x ([x, ]) when an object is instantiated [x, ] a method x that returns the attribute xl

Define a class AbstractX of type ABCMeta that uses subclasshook to check if all registered classes have x attribute (not callable).

 

Test the classes by instantiating them and checking is they are instances of AbstractX.

e.g.

mn = MyNum(700)
ms = MyStr(700)
mx = MyX(700)

print(isinstance(mn, AbstractX)) #  prints: True
print(isinstance(ms, AbstractX)) #  prints: True
print(isinstance(mx, AbstractX)) #  prints: False
'''
from abc import ABCMeta, abstractclassmethod

class AbstractX(metaclass=ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is AbstractX:
            if hasattr(subclass, 'x') and not callable(subclass.x):
                return True

    @abstractclassmethod
    def x(cls):
        pass


class MyNum(AbstractX):
    def __init__(self, x):
        self.x = x

    def __index__(self):
        return int(self.x)
    
    @classmethod
    def x(cls):
        pass


class MyStr(AbstractX):
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)
    
    @classmethod
    def x(cls):
        pass


class MyX(AbstractX):
    def __init__(self, x):
        self.xl = [x, ]

    def x(self):
        return self.xl
    
    @classmethod
    def x(cls):
        pass
    

if __name__ == "__main__":
    mn = MyNum(700)
    ms = MyStr(700)
    mx = MyX(700)

    print(isinstance(mn, AbstractX)) #  prints: True
    print(isinstance(ms, AbstractX)) #  prints: True
    print(isinstance(mx, AbstractX)) #  prints: False
