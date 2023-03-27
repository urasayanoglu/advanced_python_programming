#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a5.py
@Time    :   2023/03/22 22:52:41
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite the a4 so that you have generator functions to:

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


1. generate all permutations one by one in a given array and yield in a tuple (id and ticket) (= one permutation of the array)
2. generate all possible tickets from all possible arrays (7*7=49 possible arrays of which 7 are winning and 9! permutations for each array).  
The function gets as arguments marks, the unique tuple of 7 characters, and gnumber (how many numbers to leave apart when yeilding generated tickets. 
The returned value from the function is a tuple ticket id, ticket and 0 or 1 to mark if the ticket is a winner (=1) or not (=0)
 

Test you generator function with the following lines of code:

marks = '§', '@', '#', '£', '¤', '&', '€' #  unique marks
gnumber = 100000 #  how many tickets to generate without returninng
gen = ticketgen(marks, gnumber)
tickets = {} # key=id, value=(ticket, 0 or 1)
winners = 0
while True:
    try:
        id, ticket, winner = next(gen)
        tickets[id] = ticket, winner
        winners += winner # 0 if not 1 if yes
        print(id, ticket, winner)
    except:
        break
print(f'total {len(tickets)} generated, {winners} tickets wins') #  total 177 generated, 21 tickets wins


'''
import itertools


def get_permutations(symbol_array, ticket_id):
    # a set does not accept duplicate tickets
    unique_ticket_permutations = set()
    # set is needed because itertools.permutations does not handle duplicate symbols in symbol_array correctly
    ticket_permutations = itertools.permutations(symbol_array)
    for generated_ticket in ticket_permutations:
        if generated_ticket not in unique_ticket_permutations:
            unique_ticket_permutations.add(generated_ticket)
            ticket_id += 1
            yield ticket_id, generated_ticket


def possible_tickets(symbols, spacing):
    generated_tickets_count = 0
    symbol_pair_id = int(1.2574*10e6)  # because amount of total possible tickets is of magnitude 10e5
    unique_symbol_pairs = itertools.combinations_with_replacement(symbols, 2)  # yields 28 unique pairs (7+6+5+4+3+2+1)
    for pair in unique_symbol_pairs:
        if pair[0] == pair[1]:
            winning_pair = True
        else:
            winning_pair = False
        array = list(symbols) + list(pair)
        pair_ticket_permutations = get_permutations(array, symbol_pair_id)
        for ticket_id, ticket in pair_ticket_permutations:
            generated_tickets_count += 1
            if generated_tickets_count % spacing == 0:
                yield ticket_id, ticket, winning_pair
        symbol_pair_id += int(3.1276*10e5)  # because amount of ticket permutations is of magnitude 10e4



if __name__ == "__main__":
    symbols = '§', '@', '#', '£', '¤', '&', '€'
    ticket_spacing = 13129  # pseudorandom ticket_ids
    count = 0
    count_winners = 0
    printed_tickets = {}

    ticket_generator = possible_tickets(symbols, ticket_spacing)
    for ticket_id, ticket, winner in ticket_generator:
        printed_tickets[int(ticket_id)] = (*ticket, winner)
        count += 1
        if winner:
            count_winners += 1
    #for key in printed_tickets:
        #print(key, *printed_tickets[key])
    print(f'total {count} generated, {count_winners} tickets wins')
