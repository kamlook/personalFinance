# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:32:33 2020

@author: Kam Look
"""

#Practice using sqlite with python 
import sqlite3
from sqlite3 import Error

def create_connection(db_name):
    #creating a connection to a SQLite database 
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        print("sucessful connection!")
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table):
    """ create a table from the create_table input using connection to db
    :param conn: Connection object
    :param create_table: a CREATE TABLE statement
    :return:
    """
    try:
        curs = conn.cursor() #cursor is class with several useful methods
        curs.execute(create_table)
    except Error as e:
        print(e)
        
def main():
    database = r"D:\sqlite\db\tempTest.db"
    
    new_friend_table = """ CREATE TABLE IF NOT EXISTS friends(
                        pid integer PRIMARY KEY,
                        friend_name text NOT NULL,
                        game text ,
                        price integer
                        );"""
    new_publisher_table = """ CREATE TABLE IF NOT EXISTS publisher(
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                rating integer,
                                genre_id text NOT NULL,
                                player_id integer NOT NULL
                                );"""
    #creating database connection
    conn = create_connection(database)
    
    #create tables 
    if conn is not None: #neat little bit of python syntax here 
        create_table(conn,new_friend_table) #create friends table 
        create_table(conn,new_publisher_table) #create publisher table 
    else:
        print("Error: canont create database connection!")
        
if __name__ == '__main__':
    main() # r indicates we are passing a raw string 









#if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.