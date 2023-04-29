import numpy as np

from beeps import *
from alphabet import morse_dict

print("before reading config file")
configs = read_beeps_config_file()
print("after reading config file")

if configs is None:
    print("configs was None")
    sys.exit(1)
else:
    sample_rate = configs['sample_rate']
    dit_time = configs['dit_time']
    frequency = configs['frequency']

# dit_time comes from config file
char_space_time = dit_time * 3
word_space_time = dit_time * 7
dah_time = char_space_time

def dit():
    tone(stream, sample_rate, dit_time, frequency)

def dah():
    tone(stream, sample_rate, dah_time, frequency)

def word_space():
    tone(stream, sample_rate, word_space_time, 0)

def char_space():
    tone(stream, sample_rate, char_space_time, 0)

def el_space():
    tone(stream, sample_rate, dit_time, 0)

def dit_or_dah(s):
    if s == '.':
        dit()
    elif s == '-':
        dah()

def play_ditdahs(s):
    if len(s) == 0:
        return
    elif len(s) == 1:
        dit_or_dah(s)
    else: # more than one
        first = s[0]
        rest = s[1:]

        dit_or_dah(first)

        for c in rest:
            el_space()
            dit_or_dah(c)

def play_word(w):
    if len(w) == 0:
        return
    elif len(w) == 1:
        play_ditdahs(morse_dict[w])
    elif len(w) > 1:
        first = w[0]
        rest = w[1:]

        play_ditdahs(morse_dict[first])

        for c in rest:
            char_space()

            play_ditdahs(morse_dict[c])

def play_string(s):
    words = s.split()

    if len(words) == 0:
        return
    elif len(words) == 1:
        play_ditdahs(words[0])
    else:
        first = words[0]
        rest = words[1:]

        play_word(first)

        for w in rest:
            word_space()
            play_word(w)
