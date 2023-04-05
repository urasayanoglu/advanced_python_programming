#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a2.py
@Time       :   2023/04/05 13:31:27
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Rewrite function squared so that it returns a new object of a given object with all integers and floats power to 2

                e.g. 

                t = triangle(2.5, 1.7)
                tt = squared(t)
                print(t.__dict__, tt.__dict__)

                

                result is:

                {'base': 2.5, 'height': 1.7} {'base': 6.25, 'height': 2.8899999999999997}

                
                class triangle:
                    def __init__(self, base, height):
                        self.base = base
                        self.height = height

                

                def squared(c):
                    for key, value in c.__dict__.items():
                        if isinstance(value, int) or isinstance(value, float):
                            c.__dict__[key] = value**2
                    return c
'''
import copy

class triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height



def squared(c):
    new_object = copy.deepcopy(c)
    for key, value in new_object.__dict__.items():
        if isinstance(value, int) or isinstance(value, float):
            new_object.__dict__[key] = value**2
    return new_object


if __name__ == "__main__":
    
    t = triangle(2.5, 1.7)
    tt = squared(t)
    print(t.__dict__, tt.__dict__)