#! /usr/bin/env python3

import os, re, sqlite3

def mk_word_list():
def opendb():
    word_list_db_pathlist = [os.path.expanduser('~'), 'sqlite-dbs', 'amer_engl_wordlist.db']
    word_list_db_filename = os.path.join(*word_list_db_pathlist)

    # create empty sqlite database
    conn = sqlite3.connect(word_list_db_filename)

    # add table to the database, with col for word, and col (primary key) for index
    return conn

    word_list_pathlist = [os.path.sep, "usr", "share", "dict", "american-english"]

    word_list_filename = os.path.join(*word_list_pathlist)

    word_list = []

    with open(word_list_filename, 'r') as word_list_h:
        for w in word_list_h:
            a_word = w.strip()

            if re.match('^[A-Za-z]+$', a_word):
                word_list.append(a_word)

    return word_list

if __name__ == '__main__':
    pass
    #word_list = mk_word_list()

    #print(repr(word_list[:125]))
