#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a5.py
@Time       :   2023/05/03 15:13:44
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a script that turns any text string into a list of latin-1 code characters. If the original Unicode character is not in ASCII set the character is replaced with  latin-1 coded letter Z

e.g.

yökkönen! is coded to [b'y', b'\xf6', b'k', b'k', b'\xf6', b'n', b'e', b'n', b'!']

and

£$€ is coded to [b'\xa3', b'$', b'Z']
'''

def to_latin1(s):
    latin1_list = []
    for c in s:
        if ord(c) < 256:  # latin-1 character
            latin1_list.append(c.encode('latin-1'))
        else:
            latin1_list.append(b'Z')  # non-latin-1 character
    return latin1_list


if __name__ == "__main__":

    print(to_latin1("yökkönen!"))
    print(to_latin1("£$€"))
    
