#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a1.py
@Time       :   2023/04/26 14:23:19
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Create a custom iterator for the Student class so that when iterated over it returns the names attribute one by one.

from datetime import date

class Student:
    def __init__(self, bdate, *names):
        self.bdate = bdate
        self.names = names


Test the iterator with the following code:

 
s = Student(date(2000, 1, 1), 'Luoto', 'Sanna', 'Tuuli', 'Meri', 'Aalto', 'Loiske')

for name in s:
    print(name)
print(s)

 
Resulting printout is:

Luoto
Sanna
Tuuli
Meri
Aalto
Loiske
'''

from datetime import date

class Student:
    def __init__(self, bdate, *names):
        self.bdate = bdate
        self.names = names

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.names):
            raise StopIteration
        name = self.names[self.current_index]
        self.current_index += 1
        return name

if __name__ == "__main__":
    s = Student(date(2000, 1, 1), 'Luoto', 'Sanna', 'Tuuli', 'Meri', 'Aalto', 'Loiske')

    for name in s:
        print(name)
    print(s)