#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   a5.py
@Time    :   2023/03/19 23:16:10
@Author  :   Uras Ayanoglu 
@Version :   1.0
@Contact :   uras.ayanoglu@edu.turkuamk.fi
@License :   (C)Copyright 2023, Uras Ayanoglu
@Desc    :   Rewrite A4 script so that the opening and closing of the connection to the database is handled in one function 
             e.g. main using a separate class to handle the context management. 

            The class defines __enter__  method which, in case there was an exception when opening the connection, calls a method that handles the exception and calls __exit__. 
            Other exceptions raised when the connection is open are handled in __exit__ method prior to closing the connection. If the exception type is sqlite3 error (test: issubclass(exc_type, sqlite3.Error), the exception is handled and the method returns True. 
            Other exceptions are not handled but passed on and the return value is False.

Code to be rewriten:


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

'''

import sqlite3
from contextlib import closing


class DatabaseManager:
    def __init__(self, db):
        self.db = db
        self.connection = None

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.db)
        except sqlite3.Error as e:
            self.handle_exception(e)
            self.__exit__()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if issubclass(exc_type, sqlite3.Error):
                self.handle_exception(exc_val)
                return True
            else:
                return False
        else:
            self.connection.commit()
            self.connection.close()

    def handle_exception(self, e):
        print('error: ', e)
        self.connection.rollback()


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

    with DatabaseManager(db) as db_manager:
        for i in range(1, 3):
            try:
                rows_affected = update_measurements(db_manager, data_set[i][0], data_set[i][1], data_set[i][2])
                print(f"{rows_affected} row(s) affected")
            except Exception as e:
                print('error: ', e)

        show_database_content(db_manager)


if __name__ == '__main__':
    db = "devicecontrol.db"
    main(db)