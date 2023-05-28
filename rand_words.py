#! /usr/bin/env python3

import random

from morse import MorsePlayer
from read_word_list import mk_word_list

word_list = mk_word_list()

list_to_send = random.choices(word_list, k=25)

str_to_send = " ".join(list_to_send)

mp = MorsePlayer()

mp.play_string(str_to_send)
