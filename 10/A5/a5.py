#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a5.py
@Time       :   2023/05/10 13:03:42
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a script using regular expressions that extracts a valid email address (of form yyy@xxx.zzz where yyy and xxx can contain characters . - or _ but not as first or last) and print the address.
e.g. 
If there are mesages:
'Ja lähetäthän tiedon vielä osoitteeseen kalle-jukola.heitto-valmennus@sul_yu.fi'
'tiedoksi pjukola.heitto-valmennus@sul_yu.fi, heitto-valmennus@sul_yu.fi, hannukka.suvi@sul.fi'
the script extracts and prints the email adresses:
mail: pjukola.heitto-valmennus@sul_yu.fi
mail: heitto-valmennus@sul_yu.fi
mail: hannukka.suvi@sul.fi
mail: pjukola.heitto-valmennus@sul_yu.fi
mail: heitto-valmennus@sul_yu.fi
mail: hannukka.suvi@sul.fi
'''

import re

messages =[
    'Ja lähetäthän tiedon vielä osoitteeseen kalle-jukola.heitto-valmennus@sul_yu.fi',
    'tiedoksi pjukola.heitto-valmennus@sul_yu.fi, heitto-valmennus@sul_yu.fi, hannukka.suvi@sul.fi'
]

# Define the regular expression pattern for a valid email address
pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+"

# Loop through each message and extract any valid email addresses using the pattern
for message in messages:
    emails = re.findall(pattern, message)
    # Loop through each email address and print it out
    for email in emails:
        print("mail:", email)
