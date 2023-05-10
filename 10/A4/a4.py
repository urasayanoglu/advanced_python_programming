#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a4.py
@Time       :   2023/05/10 13:03:00
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a script using regular expressions that replaces all scandinavian characters in a text with latin ones i.e. Å and Ä with A, Ö with O, å and ä with a, and ö with o
e.g. 
if the string is: 'Yökkönen yllä Äänisen yllätti Åken.'
the result is: Yokkonen ylla Aanisen yllatti Aken.
'''
#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a4.py
@Time       :   2023/05/10 13:03:00
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a script using regular expressions that replaces all scandinavian characters in a text with latin ones i.e. Å and Ä with A, Ö with O, å and ä with a, and ö with o
e.g. 
if the string is: 'Yökkönen yllä Äänisen yllätti Åken.'
the result is: Yokkonen ylla Aanisen yllatti Aken.
'''
import re

text = "Yökkönen yllä Äänisen yllätti Åken."
pattern = r'[ÅÄÖåäö]'

def replace_scandinavian(match):
    char = match.group()
    if char == 'Å' or char == 'Ä':
        return 'A'
    elif char == 'Ö':
        return 'O'
    elif char == 'å' or char == 'ä':
        return 'a'
    elif char == 'ö':
        return 'o'
    
if __name__ == "__main__":

    latin_text = re.sub(pattern, replace_scandinavian, text)
    print(latin_text)
