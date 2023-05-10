#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a2.py
@Time       :   2023/05/10 13:02:03
@Author(s)  :   Uras Ayanoglu
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a regular expression to verify if a string contains any (capital or small) scandinavian characters (ä, ö, å) 
e.g. 
if a given string is:'Yökkönen yllä Äänisen yllätti Åken.'
the result is: 'the string contains scandinavian characters'
if a given string is: 'Yliopistomme on maan vanhin.'
the result is: 'there are no scandinavian characters'
'''

import re

scandinavian_pattern = re.compile("[äöåÄÖÅ]")

def check_scandinavian(string):
    if scandinavian_pattern.search(string):
        return "the string contains scandinavian characters"
    else:
        return "there are no scandinavian characters"


if __name__ == "__main__":

    string1 = "Yökkönen yllä Äänisen yllätti Åken."
    string2 = "Yliopistomme on maan vanhin."

    print(check_scandinavian(string1)) # the string contains scandinavian characters
    print(check_scandinavian(string2)) # there are no scandinavian characters
