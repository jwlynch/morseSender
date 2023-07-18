#! /usr/bin/env python3

import os, re, sqlite3

def opendb():
    word_list_db_pathlist = [os.path.expanduser('~'), 'sqlite-dbs', 'amer_engl_wordlist.db']
    word_list_db_filename = os.path.join(*word_list_db_pathlist)

    conn = sqlite3.connect(word_list_db_filename)

    return conn

def get_cursor(conn):
    c = conn.cursor()

    return c

def mk_word_list(conn, c):

    # add table to the database, with col for word, and col (primary key) for index
    c.execute('''
        create table words (
            word text,
            idex integer primary key
        )
    ''')

    word_list_index = 0

    with open(word_list_filename, 'r') as word_list_h:
        for w in word_list_h:
            a_word = w.strip()

            # if the word contains only letters, word is good to go into the db
            if re.match('^[A-Za-z]+$', a_word):
                # insert word (and index) into database
                c.execute(f"insert into words values ('{a_word}', {word_list_index})")

                # increment index
                word_list_index += 1

                conn.commit()

def get_word(conn, c):
    c.execute(f"select word, idex from words where idex = 3000")

    row = c.fetchone()

    return row[0]

if __name__ == '__main__':
    
    # create empty sqlite database
    conn = opendb()
    c = get_cursor(conn)

    #mk_word_list(conn, c)

    #print(repr(word_list[:125]))

    word = get_word(conn, c)

print(word)
