#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a4.py
@Time    :   2023/03/08 14:54:37
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Write a decorator magazine_info that checks the number and types of the decorated function from the decorator arguments min_number and types.
             The should be at least min_number of keywords with with matching types.If there are less keywords or there types are not a match, the decorator raises a ValueError. 
             If there is no error, the decorator returns the value decorated function returns.
'''

from functools import wraps

def magazine_info(min_number, types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            expected_keywords_and_types = {"year": int, "price" : float, "name": str}
            if len(kwargs) < min_number:
                raise ValueError(f"Expected at least {min_number} keywords, got {len(kwargs)}")
            for keyword in expected_keywords_and_types:
                if keyword not in expected_keywords_and_types:
                    raise ValueError("Unexpexted keyword argument")
                elif not isinstance(kwargs[keyword], expected_keywords_and_types[keyword]):
                    raise ValueError(f"Argument '{keyword}' is a {type(kwargs[keyword])} with a value of {kwargs[keyword]} but it should have been {expected_keywords_and_types[keyword]} type.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@magazine_info(min_number=3, types=(int, float, str))
def magazine(*, year: int, price:float, name:str='Donald Duck', **kwargs)-> str:
    start = f"The first {name} sold {year} in Finland with {price} (old) marks."
    l = []
    for key, value in kwargs.items():
        l.append(f"{key}: {value}")
    return f"{start}\n {''.join(l)}"

if __name__ == "__main__":
    try:
        print(magazine(year=1951, price=50.0, name='Aku Ankka')) #  ok
        print(magazine(year=1951, price=50.0, name='Aku Ankka', circulation=34017)) #  ok
        print(magazine(year=1951, price=50, name='Aku Ankka', circulation=34017)) #  fails
    except Exception as error:
        print('There was an error', error)
