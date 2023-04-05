#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a4.py
@Time       :   2023/04/05 13:31:35
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a function recaman that calculates and returns Recaman’s sequncenumbers given as parameter e.g.  
                recaman(70) returns a list 70 first numbers in the Recaman’s sequence.
                Use type annotations for parameter and the return value.
                Reference: https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence 
'''

from typing import List

def recaman(n: int) -> List[int]:
    """
    Calculates and returns the first n numbers in Recaman's sequence.
    """
    seq = [0]
    used = set([0])
    for i in range(1, n):
        prev = seq[i-1]
        next = prev - i
        if next < 0 or next in used:
            next = prev + i
        seq.append(next)
        used.add(next)
    return seq[:n]

if __name__ == "__main__":
    print(recaman(70))