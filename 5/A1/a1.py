#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a1.py
@Time       :   2023/04/05 13:30:55
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Re-write the function inv so that it returns a  new list of numbers where each item is 1/num e.g.

                if original list is l = [1, 2, 5, 10, 20, 25, 50, 100] 
                the new list is [1.0, 0.5, 0.2, 0.14285714285714285, 0.1, 0.05, 0.04, 0.013333333333333334, 0.01] 
                and the original list is unchanged.

 
def inv(nums):
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i] = 1/(nums[i])
    return nums
'''
import copy

def inv(nums):
    local = copy.deepcopy(nums)
    for i in range(len(local)):
        if local[i] != 0:
            local[i] = 1/(local[i])
    return local

if __name__ == "__main__":
    l = [1, 2, 5, 10, 20, 25, 50, 100] 
    new_list = inv(l)
    
    # Print the unmodified list
    print(l)
    
    #Print the modified list
    print(new_list)