#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a1.py
@Time    :   2023/03/08 13:58:04
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Write a decorator copyright that prints “copyright - [your name]” when a decorated function is called.
             Decorated function does not take any parameters nor return any value.
'''
from functools import wraps

def copyright(func):
    @wraps(func)
    def wrapper():
        print("copyright - Ayanoglu Uras")
        func()
    return wrapper

@copyright
def foo():
    print("This is a decorated function.")

if __name__ == "__main__":
    foo()
