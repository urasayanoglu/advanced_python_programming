#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a4.py
@Time       :   2023/04/20 11:14:58
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Define an abstract class Age that defines an abstract method age.
                Define a class Student that has attributes name and birthdate registers Age using decorator

                
Create a list of Student objects and print their names and ages.

e.g.

students = [Student(date(1995, 3, 6), 'Ella', 'Maria', 'Kukka', 'Helenius'), \
            Student(date(1992, 10, 16), 'Aleksi', 'Jokkeri', 'Halme'),\
            Student(date(1990, 1, 2), 'Alisa', 'Ilmi' 'Virtanen'),\
            Student(date(1999, 11, 12), 'Anna', 'Kristiina', 'Sjöblom'),\
            Student(date(2000, 7, 27), 'Maaria', 'Aava', 'Tyyne', 'Laine'),\
            Student(date(1998, 4, 19), 'Wilhelmi', 'Weikko', 'Kuukasjärvi')]

print([f'{item}, age {item.age()}' for item in students])

 

 

prints:

['Ella Maria Kukka Helenius, 1995-03-06, age 28', 'Aleksi Jokkeri Halme, 1992-10-16, age 30', 'Alisa IlmiVirtanen, 1990-01-02, age 33', 'Anna Kristiina Sjöblom, 1999-11-12, age 23', 'Maaria Aava Tyyne Laine, 2000-07-27, age 22', 'Wilhelmi Weikko Kuukasjärvi, 1998-04-19, age 24']

'''
from abc import ABC, abstractmethod
from datetime import date

class Age(ABC):
    @abstractmethod
    def age(self):
        pass

class Student:
    
    def __init__(self, birthdate, *names):
        self.birthdate = birthdate
        self.names = names
    
    @property
    def name(self):
        return ' '.join(list(self.names))
    
    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))


if __name__ == "__main__":
    students = [
        Student(date(1995, 3, 6), 'Ella', 'Maria', 'Kukka', 'Helenius'),
        Student(date(1992, 10, 16), 'Aleksi', 'Jokkeri', 'Halme'),
        Student(date(1990, 1, 2), 'Alisa', 'Ilmi', 'Virtanen'),
        Student(date(1999, 11, 12), 'Anna', 'Kristiina', 'Sjöblom'),
        Student(date(2000, 7, 27), 'Maaria', 'Aava', 'Tyyne', 'Laine'),
        Student(date(1998, 4, 19), 'Wilhelmi', 'Weikko', 'Kuukasjärvi')
    ]

    print([f'{item.name}, age {item.age()}' for item in students])
