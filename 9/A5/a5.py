#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a5.py
@Time       :   2023/05/04 00:16:48
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write a python function iscopy that has two binary files as parameters, reads both files (using blocksize = 1024 to handle also very big files) and if the files are identical in their content returns true else false.

 

e.g. with the example files

result = iscopy('Testing.pdf','Testing.pdf')         
print("Files match" if result else "Files do not match.")

 

the result is Files match

 

 

result = iscopy('Testing.pdf','Testing_2.pdf')         
print("Files match" if result else "Files do not match.") 

 

the result is Files do not match.
'''

import os
import hashlib

def iscopy(file1, file2):
    blocksize = 1024
    md5_1 = hashlib.md5()
    md5_2 = hashlib.md5()
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            data1 = f1.read(blocksize)
            data2 = f2.read(blocksize)
            if not data1 and not data2:
                break
            md5_1.update(data1)
            md5_2.update(data2)
    return md5_1.digest() == md5_2.digest() and os.path.getsize(file1) == os.path.getsize(file2)


if __name__ == "__main__":

    # Get the absolute path of the current directory
    dir_path = os.path.abspath(os.path.dirname(__file__))

    # Build the absolute path of the PDF file
    pdf_file1 = os.path.join(dir_path, 'Testing.pdf')
    pdf_file2 = os.path.join(dir_path, 'Testing_2.pdf')

    result = iscopy(pdf_file1, pdf_file1)
    print("Files match" if result else "Files do not match.")

    result2 = iscopy(pdf_file1, pdf_file2)
    print("Files match" if result2 else "Files do not match.")

