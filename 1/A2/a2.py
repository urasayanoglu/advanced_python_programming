#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a2.py
@Time    :   2023/03/08 14:34:25
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Write a decorator copyright that prints “copyright - [your name]” when a decorated function is called. 
             Decorated function takes parameters both positional and with a keyword and returns a value.
'''

from functools import wraps

def copyright(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("copyright - Ayanoglu Uras")
        return func(*args, **kwargs)
    return wrapper

@copyright
def foo(a, b, c='Donald Duck'):
    return (a, b, c)


if __name__ == "__main__":
    x = foo('Aku Ankka', 'Kalle Anka')
    print(*x)