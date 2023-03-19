#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a2.py
@Time    :   2023/03/18 21:22:14
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite A1 script so that the execution of the sql statement (update) is moved to a function that takes parameters:
             1. connection  to database (devicecontrol)
             2. sql statement using either ? or :par for data
             3. data in the statement
            The function uses context manager to handle commit if the statement is executed successfully or rollback if not.

Code to be rewriten:

import sqlite3

    db = "devicecontrol.db"
    data = 50.5, 1, "Experimental"
    sql_statement = """
        UPDATE measurements
        SET amplitude = ?
        WHERE device= ? and treatment=?;
        """

    try:
        with sqlite3.connect(db) as conn:
            conn.execute(sql_statement, data)
            conn.commit()

    except Exception as e:
        print('error: ', e)

'''


import sqlite3


def execute_sql(connection, sql, data):
    try:
        with connection:
            connection.execute(sql, data)
    except Exception as e:
        print('error: ', e)
        connection.rollback()
    else:
        connection.commit()


if __name__ == "__main__":
    
    db = "devicecontrol.db"
    data = 50.5, 1, "Experimental"
    sql_statement = '''
        UPDATE measurements
        SET amplitude = ?
        WHERE device= ? and treatment=?;
        '''

    try:
        with sqlite3.connect(db) as conn:
            execute_sql(conn, sql_statement, data)

    except Exception as e:
        print('error: ', e)

