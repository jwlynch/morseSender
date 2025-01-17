#! /usr/bin/env python3

import os, re

# param lvl should range from 1 to 9

def mk_intl_morse_str(lvl):
    intl_list = ['eti5', 'man0', 'sor1', 'kdw2', 'vug8', 'hbf9', 'pcq3', 'yjl4', 'xz7']

    return "".join(intl_list[:lvl])

def mk_word_list(match_str=None):

    if match_str is None:
        match_str = 'a-z'
    
    matcher = re.compile( f'^[{match_str}]+$' )

    word_list_pathlist = [os.path.sep, "usr", "share", "dict", "american-english"]

    word_list_filename = os.path.join(*word_list_pathlist)

    word_list = []

    with open(word_list_filename, 'r') as word_list_h:
        for w in word_list_h:
            a_word = w.strip().lower()

            if re.match(matcher, a_word):
                word_list.append(a_word)

    return word_list

if __name__ == '__main__':
    word_list = mk_word_list()

    print(repr(word_list[:125]))
