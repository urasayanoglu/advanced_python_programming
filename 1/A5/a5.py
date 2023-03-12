#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :  a5.py
@Time    :  2023/03/11 21:20:30
@Author  :  Uras Ayanoglu 
@Version :  1.0
@Contact :  uras.ayanoglu@edu.turkuamk.fi
@License :  (C)Copyright 2023, Uras Ayanoglu
@Desc    :  Write a decorator class MagazineDecorator that takes arguments for min_number and types when initalized and creates attributes min_number and types of them.
            The overloaded call method checks the number and types of the decorated function from the attributes min_number and types.
            There should be at least min_number of keywords with with matching types.If there are less keywords or there types are not a match decorator raises a ValueError. 
            If there is no error,the decorator returns the value decorated function returns.
'''
from functools import wraps

class MagazineDecorator:
    def __init__(self, min_number, types):
        self.min_number = min_number
        self.types = types

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            num_args = len(kwargs)
            if num_args < self.min_number:
                raise ValueError(f"Expected at least {self.min_number} keywords, got {num_args}")
            for key, value in kwargs.items():
                if type(value) not in self.types:
                    raise ValueError(f"{key}: {value} type not in {self.types}")
            return func(*args, **kwargs)
        return wrapper
    
@MagazineDecorator(min_number=3, types=(int, float, str))
def magazine(*, year:int, price:float, name:str='Donald Duck', **kwargs)->str:
    start = f"The first {name} sold {year} in Finland with {price} (old) marks."
    l = []
    for key,value in kwargs.items():
        l.append(f"{key}={value}")
    return f"{start}\n {''.join(l)}"

if __name__ == "__main__":
    try:
        print(magazine(year=1951, price=50.0, name='Aku Ankka'))
        print(magazine(year=1951, price=50.0, name='Aku Ankka', circulation=34017))
        print(magazine(year=1951, name='Aku Ankka', circulation=34017))
    except Exception as error:
        print('There was an error:', error)




