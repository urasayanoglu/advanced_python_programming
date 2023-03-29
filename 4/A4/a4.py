#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a4.py
@Time    :   2023/03/29 15:48:59
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Sort students list to alphabetical order based on the names and age and print each student’s name and age into one separate line.

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
        return self.names < other.names    


    

students = [Student(date(1995, 3, 6), 'Ella', 'Maria', 'Kukka', 'Helenius'), \
            Student(date(1992, 10, 16), 'Aleksi', 'Jokkeri', 'Halme'),\
            Student(date(1990, 1, 2), 'Alisa', 'Ilmi', 'Virtanen'),\
            Student(date(1999, 11, 12), 'Anna', 'Kristiina', 'Sjöblom'),\
            Student(date(2000, 7, 27), 'Maaria', 'Aava', 'Tyyne', 'Laine'),\
            Student(date(1998, 4, 19), 'Wilhelmi', 'Weikko', 'Kuukasjärvi')]

students.sort()
for student in students:
    print(student)