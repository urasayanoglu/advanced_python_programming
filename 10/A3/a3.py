#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a3.py
@Time       :   2023/05/10 13:02:45
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a script using regular expressions that searches all the words starting with a capital scandinavian character and prinst the characters and their starting positions.
e.g. 
if the string is: 'Yökkönen yllä Äänisen yllätti Åken.'
the result is:
Äänisen: 14
Åken: 30
'''

import re

text = "Yökkönen yllä Äänisen yllätti Åken."
pattern = r"\b[ÅÄÖ][a-zA-ZäöüÄÖÅ]*\b"

if __name__ == "__main__":
    matches = re.finditer(pattern, text)

    for match in matches:
        start_index = match.start()
        word = match.group()
        print(f"{word}: {start_index}")