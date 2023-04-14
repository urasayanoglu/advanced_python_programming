#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a2.py
@Time       :   2023/04/12 14:33:52
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Rewrite the following definition of Shape class using a class factory function create_Shape()

def init(self, base: float):
    self.base = base

def area(self):
    pass

Shape = type('Shape', (), {
    '__doc__':"""uppermost class to geometrical shapes""",
    '__init__': init,
    'area': area,})

 

Test the class factory function with the following code that creates two objects both of type created using the create_Shape function and prints their dictionary and type

s1, s2 = create_Shape()(4.5), create_Shape()(3.14)
print(s1.__dict__, s2.__dict__, type(s1), type(s2))

#  {'base': 4.5} {'base': 3.14} <class '__main__.Shape'> <class '__main__.Shape'>
'''
def create_Shape():
    """A basic attempt to model a shape"""

    def __init__(self, base):
        """Initializer for the class Shape"""
        self.base = base

    def area(self):
        pass

    return type('Shape', (), {
        '__doc__':"""uppermost class to geometrical shapes""",
        '__init__': __init__,
        'area': area,})
    

if __name__ == "__main__":
    s1, s2 = create_Shape()(4.5), create_Shape()(3.14)
    print(s1.__dict__, s2.__dict__, type(s1), type(s2))