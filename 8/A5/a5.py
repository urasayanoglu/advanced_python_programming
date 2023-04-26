#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a5.py
@Time       :   2023/04/26 15:10:35
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write in one line code that picks all capital letters from any string e.g. "Hello there Opossums, Isn't it a Lovely Day?" maps them into integers (hint ord) calculates their sum and returns it as a hex number. 
                e.g. 
                "Hello there Opossums, Isn't is a Lovely Day?"
                hex value of the sum of capital letters is 0x170
'''

if __name__ == "__main__":
    s = "Hello there Opossums, Isn't it a Lovely Day?"
    result = hex(sum(map(ord, filter(str.isupper, s))))
    print(f"hex value of the sum of capital letters is {result}")
