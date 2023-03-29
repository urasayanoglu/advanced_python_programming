#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a5.py
@Time    :   2023/03/29 15:55:52
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Modify the Student class so that students list can be sorted based on the age.

 
Code to be modified:
from datetime import date

class Student:
    def __init__(self, bdate, *names):
        self.bdate = bdate
        self.names = names

    def __str__(self):
        age = (date.today()).year-(self.bdate).year
        if date.today() < date(date.today().year, self.bdate.month, self.bdate.day):
            age -= 1
        return f"{' '.join(self.names)}, age {age}"


    

students = [Student(date(1995, 3, 6), 'Ella', 'Maria', 'Kukka', 'Helenius'), \
            Student(date(1992, 10, 16), 'Aleksi', 'Jokkeri', 'Halme'),\
            Student(date(1990, 1, 2), 'Alisa', 'Ilmi' 'Virtanen'),\
            Student(date(1999, 11, 12), 'Anna', 'Kristiina', 'Sjöblom'),\
            Student(date(2000, 7, 27), 'Maaria', 'Aava', 'Tyyne', 'Laine'),\
            Student(date(1998, 4, 19), 'Wilhelmi', 'Weikko', 'Kuukasjärvi')]


'''

from datetime import date

class Student:
    def __init__(self, bdate, *names):
        self.bdate = bdate
        self.names = names

    def __str__(self):
        age = (date.today()).year-(self.bdate).year
        if date.today() < date(date.today().year, self.bdate.month, self.bdate.day):
            age -= 1
        return f"{' '.join(self.names)}, age {age}"
    
    def __lt__(self, other):
        return self.bdate < other.bdate


    

students = [Student(date(1995, 3, 6), 'Ella', 'Maria', 'Kukka', 'Helenius'), \
            Student(date(1992, 10, 16), 'Aleksi', 'Jokkeri', 'Halme'),\
            Student(date(1990, 1, 2), 'Alisa', 'Ilmi', 'Virtanen'),\
            Student(date(1999, 11, 12), 'Anna', 'Kristiina', 'Sjöblom'),\
            Student(date(2000, 7, 27), 'Maaria', 'Aava', 'Tyyne', 'Laine'),\
            Student(date(1998, 4, 19), 'Wilhelmi', 'Weikko', 'Kuukasjärvi')]

students.sort() # Sorts the list based on the age, method can take reverse=True as a parameter if you want to sort in descending order
for student in students:
    print(student)