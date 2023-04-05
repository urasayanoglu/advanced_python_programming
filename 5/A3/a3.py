#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File       :   a3.py
@Time       :   2023/04/05 13:31:31
@Author(s)  :   Uras Ayanoglu 
@Version    :   1.0
@Contact    :   uras.ayanoglu@edu.turkuamk.fi
@License    :   ©Copyright 2023, Uras Ayanoglu
@Desc       :   Rewrite the function apds so that when called only with the first argument the returned value is a list with only the given argument. 
                If the function is called with two arguments the first is appended to the list given as the second argument.

                e.g.

                calling with only one argument:


                print(apds('s'))
                ss = 'cutie pie'
                print(apds(ss))

                result is:

                ['s']
                ['s', 'cutie pie']

                

                calling with two areguments:

                st = 'hello there'
                l = [list(s) for s in st.split()]
                print(apds('***', l))
                print(apds('!!!', list(range(4))))

                

                result is:

                [['h', 'e', 'l', 'l', 'o'], ['t', 'h', 'e', 'r', 'e'], '***']
                [0, 1, 2, 3, '!!!']


                def apds(c, s=[]):
                    s.append(c)
                    return s


'''

def apds(c, s=[]):
    if not s:
        s = []
    s.append(c)
    return s



if __name__ == "__main__":

    print(apds('s'))
    ss = 'cutie pie'
    print(apds(ss))


    st = 'hello there'
    l = [list(s) for s in st.split()]
    print(apds('***', l))
    print(apds('!!!', list(range(4))))

