#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a4.py
@Time       :   2023/04/12 14:35:39
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Rewrite the following definition of Shape class using a class factory function create_Shape_class() using keyword class, taking base as a parameter that is passed to init function and  returning the class instance

def init(self, base: float):
    self.base = base

def area(self):
    pass

Shape = type('Shape', (), {
    '__doc__':"""uppermost class to geometrical shapes""",
    '__init__': init,
    'area': area,})


Test the class factory function with the following code that creates an object of type created using the create_Shape_class function and prints its dictionary and type

s4 = create_Shape_class(4.9)
print(s4.__dict__, type(s4))

#{'base': 4.9} <class '__main__.create_Shape_class.<locals>.Shape'>
'''
def create_Shape_class(base):
    """A basic attempt to model a shape"""

    class Shape:
        """uppermost class to geometrical shapes"""
        def __init__(self, base):
            """Initializer for the class Shape"""
            self.base = base

        def area(self):
            pass

    return Shape(base)

if __name__ == "__main__":
    s4 = create_Shape_class(4.9)
    print(s4.__dict__, type(s4))