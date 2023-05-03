#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a3.py
@Time       :   2023/05/03 15:19:45
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a script that calculates a personal PIN based on 

                sum of set of utf-16 coded letters in user’s name modulo 3
                max of set of utf-16 coded letters in user’s name modulo 5
                product of the sum and max modulo 7
                sum of the previous modulo 9

                e.g. if the name is

Tiina Ferm the PIN is 2 0 3 5

Akseli Galen-Kallela the PIN is 1 0 0 1
'''

def calculate_pin(name):
    # Step 1: Sum of UTF-16 coded letters modulo 3
    set_name = set(name.encode('utf-16'))
    sum_utf16 = sum(set_name)
    mod_sum_utf16 = sum_utf16 % 3
    
    # Step 2: Max of UTF-16 coded letters modulo 5
    max_utf16 = max(set_name)
    mod_max_utf16 = max_utf16 % 5
    
    # Step 3: Product of step 1 and step 2 modulo 7
    product_mod7 = (sum_utf16 * max_utf16) % 7
    
    # Step 4: Sum of step 1, step 2 and step 3 modulo 9
    last_digit = (mod_sum_utf16 + mod_max_utf16 + product_mod7) % 9

    pin_code = f"{mod_sum_utf16} {mod_max_utf16} {product_mod7} {last_digit}"
    
    return pin_code


if __name__ == "__main__":

    user_name1 = "Tiina Ferm"
    user_name2 = "Akseli Galen-Kallela"

    print(f"{user_name1} the PIN is {calculate_pin(user_name1)}")
    print(f"{user_name2} the PIN is {calculate_pin(user_name2)}")