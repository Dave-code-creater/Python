import sqlite3


"""
Module Name: db.py
Description: This module contains the functions to interact with db
- create_connection(db_file)
- insert_book(conn, book)
- select_all_books(conn)
- delete_book(conn, id)
"""

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def insert_book(conn, book):
    sql = ''' INSERT INTO books(title, author, published_date, isbn)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, book)
    return cur.lastrowid

def select_all_books(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    return rows



def delete_book(conn, id):
    sql = 'DELETE FROM books WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


