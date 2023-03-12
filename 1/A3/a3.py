#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a3.py
@Time    :   2023/03/08 14:42:20
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Write a decorator magazine_info that checks the number and types of keyword arguments of a decorated function.
             The keywords should be year: int, price:float and name:str. If the number or type fails, the decorator raises a ValueError.
             The decorator returns the value decorated function returns.
'''
from functools import wraps

def magazine_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(kwargs) != 3:
            raise ValueError("The number of keyword arguments is not 3.")
        if not isinstance(kwargs['year'], int):
            raise ValueError("The type of year is not int.")
        if not isinstance(kwargs['price'], float):
            raise ValueError("The type of price is not float.")
        if not isinstance(kwargs['name'], str):
            raise ValueError("The type of name is not str.")
        return func(*args, **kwargs)
    return wrapper

@magazine_info
def magazine(*, year: int, price:float, name:str='Donald Duck')-> str:
    return f"The first {name} sold {year} in Finland with {price} (old) marks."


if __name__ == "__main__":
    try:
        print(magazine(year=1951, price=50.0, name='Aku Ankka')) #  ok
        print(magazine(year=1951, price=50, name='Aku Ankka')) #  fails
    except Exception as error:
        print('There was an error', error)