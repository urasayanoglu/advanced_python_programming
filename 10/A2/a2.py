#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a2.py
@Time       :   2023/05/10 13:02:03
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a regular expression that finds if a word Finland has been used and in which place (starting index) in any given text.
e.g.
if a given string is: Welcome to Finland!
the result (starting index)  is: 11
'''

import re

text = "Welcome to Finland!"
pattern = r"\bFinland\b"



if __name__ == "__main__":

    match = re.search(pattern, text)

    if match:
        start_index = match.start()
        print(f"The result (starting index) is: {start_index}")
    else:
        print("The word 'Finland' was not found in the text.")
