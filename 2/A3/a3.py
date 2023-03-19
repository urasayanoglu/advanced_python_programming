#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a3.py
@Time    :   2023/03/18 21:42:08
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite A2 script so that the function performing the execution e.g. execute of the sql statement (update) is called from a function that forms an update statement 
             e.g. update, and returns the result of the execution of the sql statement. The function to execute the sql statement returns the number of lines affected by the statement. 
             To avoid memory leaks close the cursor before returning from the function. Use contextlib closing for managing the cursor. It i possible to have several context managers in one with statement:

            with A() as X, B() as Y, C() as Z:
                do_something()


Code to be rewriten:

import sqlite3

def sqlconnection(db:str, data, sql_statement):
      with sqlite3.connect(db) as conn:
        conn.execute(sql_statement, data)
        conn.commit()

'''


"""import sqlite3 

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
"""


import sqlite3
from contextlib import closing


def execute_sql(connection:sqlite3.Connection, sql, data):
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute(sql, data)
            result = cursor.rowcount

            if result > 0:
                print('Successful!')
            else:
                print('Failed!')
                
    except Exception as e:
        print('error: ', e)
        connection.rollback()
    else:
        connection.commit()
    finally:
        cursor.close()
    return result


def update_measurements(connection, amplitude, device, treatment):
    sql = '''
        UPDATE measurements
        SET amplitude = ?
        WHERE device = ? AND treatment = ?;
    '''
    data = amplitude, device, treatment
    return execute_sql(connection, sql, data)



if __name__ == "__main__":
    
    db = "devicecontrol.db"

    data_set = {
        1: (50.5, 1, "Experimental"),
        2: (50.5, 1, 'Finished'),
    }

    for i in range(1,3):
        try:
            with sqlite3.connect(db) as conn, closing(conn.cursor()) as cursor:
                rows_affected = update_measurements(conn, data_set[i][0], data_set[i][1], data_set[i][2])
                print(f"{rows_affected} row(s) affected")

        except Exception as e:
            print('error: ', e)


