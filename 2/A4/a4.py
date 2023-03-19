#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a4.py
@Time    :   2023/03/19 22:47:20
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite A3 script so that the opening and closing of the connection to the database is handled in one function 
             e.g. main that calls the updating function and the function that is showing the complete database content. 
             The main function has a parameter db, the sqlite3 database to connect to.
             Use contextlib closing to manage the connection. 

Code to be rewriten:

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
    sql = """
        UPDATE measurements
        SET amplitude = ?
        WHERE device = ? AND treatment = ?;
    """
    data = amplitude, device, treatment
    return execute_sql(connection, sql, data)

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



'''

import sqlite3
from contextlib import closing


def execute_sql(connection: sqlite3.Connection, sql, data):
    try:
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
    sql = """
        UPDATE measurements
        SET amplitude = ?
        WHERE device = ? AND treatment = ?;
    """
    data = amplitude, device, treatment
    return execute_sql(connection, sql, data)


def show_database_content(connection):
    sql = """
        SELECT *
        FROM measurements;
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()


def main(db):
    data_set = {
        1: (50.5, 1, "Experimental"),
        2: (50.5, 1, 'Finished'),
    }

    with closing(sqlite3.connect(db)) as connection:
        for i in range(1, 3):
            try:
                rows_affected = update_measurements(connection, data_set[i][0], data_set[i][1], data_set[i][2])
                print(f"{rows_affected} row(s) affected")
            except Exception as e:
                print('error: ', e)

        show_database_content(connection)


if __name__ == '__main__':
    db = "devicecontrol.db"
    main(db)
