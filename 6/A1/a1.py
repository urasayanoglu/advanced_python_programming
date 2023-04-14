#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a1.py
@Time       :   2023/04/12 14:32:14
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Rewrite the following definition of a class 

def init(self, base: float):
    self.base = base

def area(self):
    pass

Shape = type('Shape', (), {
    '__doc__':"""uppermost class to geometrical shapes""",
    '__init__': init,
    'area': area,})
            
Test the definition with the  following code that creates a Shape object and prints its directory

s = Shape(5.4)

print(s.__dict__) #  prints {'base': 5.4}
'''

class Shape():
    """A basic attempt to model a shape"""

    def __init__(self, base):
        """Initializer for the class Shape"""
        self.base = base

    def area(self):
        pass
        
if __name__ == "__main__":
    s = Shape(5.4)
    print(s.__dict__) #  prints {'base': 5.4}
