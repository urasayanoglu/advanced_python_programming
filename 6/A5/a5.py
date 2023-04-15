#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a5.py
@Time       :   2023/04/12 14:36:32
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Rewrite the following class definitions using a class factory function create_Circle that returns type Circle, a subclass of Shape.

import math

def init(self, base: float):
    self.base = base

def area(self):
    pass

Shape = type('Shape', (), {
    '__doc__':"""uppermost class to geometrical shapes""",
    '__init__': init,
    'area': area,})

def carea(self):
    return math.pi * self.base**2

Circle = type('Circle', (Shape,), {
    '__doc__':"""circle""",
    'area': carea,
})


Test the class faactory function with the following code that creates an object of type Circle and calculates and prins its area

c = create_Circle()(1.0)
print(type(c), c.__dict__, c.area())

#<class '__main__.Circle'> {'base': 1.0} 3.141592653589793
'''

import math

def create_Circle():

    def init(self, base: float):
        self.base = base

    def area(self):
        pass

    Shape = type('Shape', (), {
        '__doc__': """uppermost class to geometrical shapes""",
        '__init__': init,
        'area': area, })

    def carea(self):
        return math.pi * self.base**2

    Circle = type('Circle', (Shape,), {
        '__doc__': """circle""",
        'area': carea,
    })
    return Circle

if __name__ == "__main__":
    c = create_Circle()(1.0)
    print(type(c), c.__dict__, c.area())