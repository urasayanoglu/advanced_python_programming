#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a4.py
@Time    :   2023/03/22 22:50:58
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   A lottery ticket is a list  that consists of 7 unique marks and 2 marks picked from the unique set of marks. 
             Each ticket has a unique identifier (integer number starting from 10000 up).

A winning ticket has three same marks in any position e.g. 

§ § § 

! @ $

& ? €

and 

§ @€ 

! § $

& ? §

are both winning tickets.

Write a function e.g. getperm that generates all possible tickets (9! = 362880) based on the following array:

marks = '§', '@', '#', '£', '¤', '&', '€'

array = list(marks) + [marks[0] + marks[0]] #  winning combination

the function returns a tuple of ticket’s id and the actual generated ticket.

 

Use permutations generator function from itertools to obtain possible arrays one by one, calculate identifier (integer number) for given array. 

 

The function itertool.permutations() takes an iterator and ‘r’ (length of permutation needed) as input and assumes ‘r’ as default length of iterator if not mentioned and returns all possible permutations of length ‘r’ each. 

a = 'Hello'

p = permutations(a, len(a)-3)  #  if no length is given the length is the same as len(a)
 
# Print the obtained permutations
for j in p:
  print(''.join(j))

 

prints:

He
Hl
Hl
Ho
eH
el
el
eo
lH
le
ll
lo
lH
le
ll
lo
oH
oe
ol
ol

 

Test you generator function with the following lines of code:

marks = '§', '@', '#', '£', '¤', '&', '€' 
array = list(marks) + [marks[0],  marks[0]] #  winning combination
id = 10000 #  each generated ticket (array permutation) will add 1 to the id
gen = getperm(array, id) #  use your generator function


printed = 0
for i in range(math.factorial(len(array))): #  9!
    id, ticket = next(gen) #  generator return a tuple of id and ticket
    if id%1000 == 0: #  print every 1000th ticket
        print(f'{id}: {ticket}')
        printed += 1

print(printed , ' tickets printed')  #  the test will print 362 tickets out of 362880 generated.
'''

import itertools
import math

def getperm(array, id):
    perm = itertools.permutations(array)
    permlist = []
    num = 1
    for j in perm:
        permlist.append(','.join(j))

    while True:
    
        idnum = id + num
        ticket = permlist[num-1]

        num += 1

        yield (idnum, ticket)

        
if __name__ == "__main__":
    
    marks = '§', '@', '#', '£', '¤', '&', '€' 
    array = list(marks) + [marks[0],  marks[0]] #  winning combination
    id = 10000 #  each generated ticket (array permutation) will add 1 to the id
    gen = getperm(array, id) #  use your generator function


    printed = 0
    for i in range(math.factorial(len(array))): #  9!
        id, ticket = next(gen) #  generator return a tuple of id and ticket
        if id%1000 == 0: #  print every 1000th ticket
            print(f'{id}: {ticket}')
            printed += 1

    print(printed , ' tickets printed')  #  the test will print 362 tickets out of 362880 generated.


