#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a3.py
@Time       :   2023/04/12 14:34:54
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Rewrite the following definition of Shape class using a class factory function create_Shape_class() using keyword class and returning the class

def init(self, base: float):
    self.base = base

def area(self):
    pass

Shape = type('Shape', (), {
    '__doc__':"""uppermost class to geometrical shapes""",
    '__init__': init,
    'area': area,})

 

 

Test the class factory function with the following code that creates an object of type created using the create_Shape_class function and prints its dictionary and type

S = create_Shape_class()
s3 = S(1.75)
print(s3.__dict__, type(s3))

# {'base': 1.75} <class '__main__.create_Shape_class.<locals>.Shape'>
'''
def create_Shape_class():
    """A basic attempt to model a shape"""

    class Shape:
        """uppermost class to geometrical shapes"""
        def __init__(self, base):
            """Initializer for the class Shape"""
            self.base = base

        def area(self):
            pass

    return Shape

if __name__ == "__main__":
    S = create_Shape_class()
    s3 = S(1.75)
    print(s3.__dict__, type(s3))
