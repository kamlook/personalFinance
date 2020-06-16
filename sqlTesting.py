# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:32:33 2020

@author: Kam Look
"""

#Practice using sqlite with python 
import sqlite3
from sqlite3 import Error

'''
try statements: are for testing blocks of code for errors
except statements: are for handling errors that the code may produce 
finally statements: executes code REGARDLESS of the results of the try and except statements
'''

def create_connection(db_name):
    #creating a connection to a SQLite database. if db doesnt exist init it 
    conn = None
    try:
        conn = sqlite3.connect(db_name)
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
        
def add_friend(conn,new_friend):
    """
    Inserts new friend into the friend table
    :param conn: Connection object to db
    :param new_friend: new friend WITH associated data
    :return friend_id: unique identifier for friend
    """
    curs = conn.cursor() #define cursor in this scope 
    new_val = """ INSERT INTO friends(friend_name,game,price)
                    VALUES(?,?,?)"""
    curs.execute(new_val,new_friend)
    return curs.lastrowid

def add_game(conn,new_game):
    """
    Add new game entry to the game table
    """
    #notice how we dont include id key when filling values. they are filled
    #automatically when new values are inserted 
    new_val = """ INSERT INTO games(name,rating,genre,player_id)
                    VALUES(?,?,?,?) """
    
    curs = conn.cursor()
    curs.execute(new_val,new_game)
    return curs.lastrowid # gives id of most recently added entry

def main():
    database = r"D:\sqlite\db\tempTest.db"
    
    new_friend_table = """ CREATE TABLE IF NOT EXISTS friends(
                        pid integer PRIMARY KEY,
                        friend_name text NOT NULL,
                        game text ,
                        price integer
                        );"""
    new_game_table = """ CREATE TABLE IF NOT EXISTS games(
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                rating integer,
                                genre text NOT NULL,
                                player_id integer NOT NULL
                                );"""
    #creating database connection
    conn = create_connection(database)
    
    #create tables 
    if conn is not None: #neat little bit of python syntax here 
        create_table(conn,new_friend_table) #create friends table 
        create_table(conn,new_game_table) #create publisher table 
    else:
        print("Error: canont create database connection!")
    
    #add test games
    game1 = ("Paper Mario: TTYD", 10, 'RPG',2)
    
    with conn:
        bff = ("DJ UNO", "Paper Mario: TTYD", 60)
        statement = 'bff is of type {}'.format(type(bff))
        print(statement)
        friend_id = add_friend(conn,bff)
        game_id = add_game(conn,game1)
        print('id of new game is {}'.format(game_id))
        
        
        
        
if __name__ == '__main__':
    main() # r indicates we are passing a raw string 
    
        #checking 



#if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.