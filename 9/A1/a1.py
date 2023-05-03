#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a5.py
@Time       :   2023/05/03 15:05:22
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a script that turns any text string into a list of ASCII code characters. If the original Unicode character is not in ASCII set the character is replaced with  ASCII coded letter A.

e.g.

'AabBcCd' is coded to [b'A', b'a', b'b', b'B', b'c', b'C', b'd']

and

'yökkönen' is coded to [b'y', b'A', b'k', b'k', b'A', b'n', b'e', b'n']
'''

def to_ascii(s):
    ascii_list = []
    for c in s:
        if ord(c) < 128:  # ASCII character
            ascii_list.append(c.encode('ascii'))
        else:
            ascii_list.append(b'A')  # non-ASCII character
    return ascii_list


if __name__ == "__main__":

    print(to_ascii('AabBcCd'))
    print(to_ascii('yökkönen'))