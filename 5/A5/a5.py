#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a5.py
@Time       :   2023/04/05 13:31:38
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Write using type annotations functions

                1. foo that takes one parameter of type str and returns it after literal ‘foo’ 
                e.g. if the given parameter was ‘hello’ it returns ‘foo: hello’
                
                2. bar that takes one parameter of type str and returns it and its length after literal ‘bar’ 
                e.g. if the given parameter was ‘world’ it returns ‘bar: world, 5’ 


                - foobar that takes two parameters a sequence of callables taking str as a parameter a sequence of str 
                returns no value
                - calls each callable in the first parameter passing str from the second parameter as an argument, 
                collects the returned values to a list and finally prints the list.
                
                Test the functions with:

                foobar([foo, bar], ['Kana Kananen', 'Pupu Tupuna'])

                the printed result should be:

                ['foo: Kana Kananen', 'bar: Pupu Tupuna, 11']
'''
