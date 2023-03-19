#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a1.py
@Time    :   2023/03/18 13:13:17
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite the following code using a context manager to update one row in the devicecontrol database.

Code to be rewriten:

#  database
db = "devicecontrol.db"

try:
        conn = sqlite3.connect(db)
    
        data = 50.5, 1, "Experimental"
        sql_statement = """
            UPDATE measurements
            SET amplitude = ?
            WHERE device= ? and treatment=?;
            """
        conn.execute(conn, sql_statement, data)
        conn.commit()

except Exception as e:
        print('error: ', e)

finally:
        conn.close()


'''

import sqlite3

if __name__ == '__main__':

    db = "devicecontrol.db"
    data = 50.5, 1, "Experimental"
    sql_statement = '''
        UPDATE measurements
        SET amplitude = ?
        WHERE device= ? and treatment=?;
        '''

    try:
        with sqlite3.connect(db) as conn:
            conn.execute(sql_statement, data)
            conn.commit()

    except Exception as e:
        print('error: ', e)