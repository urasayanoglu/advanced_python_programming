#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a4.py
@Time       :   2023/05/03 23:28:58
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a function cipher that has parameters a text string and an integer. 
                A text string is to be ciphered using a ceasar cipher and the integer tells how many steps to use in cipher.  
                The text string is ciphered using lowcase characters only and removing all whitespaces from the text. 
                After the original text the function adds ending mark ‘aqz’ and ciphers that too.
                
                A decipher function that takes the ciphered text string as a parameter. 
                It tries with different steps until the given text is deciphered back and it returns the ciphered text without the ending mark.
                Ceasar cipher replaces every letter in text with a letter that is a step ahead or before in the alphabets. e.g.

                step 3 text attack Monday is dwwdfnprqgd| Hint! use ord and chr
'''

def cipher(text, step):
    text = text.lower().replace(" ", "").strip() + "aqz" # Convert to lowercase and remove whitespace and add an ending mark
    result = ""
    for char in text:
        # Shift the character by the specified number of steps
        shifted_char = chr((ord(char) - 97 + step) % 26 + 97)
        result += shifted_char
    return result


def decipher(ciphered_text):

    for step in range(26):
        result = ""
        for char in ciphered_text:
            if char.isalpha():
                # Shift the character back by the current step
                shifted_char = chr((ord(char) - 97 - step) % 26 + 97)
            else:
                shifted_char = char
            result += shifted_char
        if result[-3:] == "aqz":
            # The ending mark was found at the end of the decrypted text
            # Only return the text before the ending mark
            return result[:-3]
    # If we get here, we couldn't decypher the text with any of the steps
    return ciphered_text


if __name__ == "__main__":
    
    text = "attack Monday"
    step = 3
    ciphered_text = cipher(text, step)
    print(ciphered_text)  # Output: "dwwdfnprqgd|aqz"
    deciphered_text = decipher(ciphered_text)
    print(deciphered_text)  # Output: "attackmonday"
