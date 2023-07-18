#! /usr/bin/env python3

import os, re, sqlite3

def mk_word_list():

    # create empty sqlite database

    # add table to the database, with col for word, and col (primary key) for index

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
