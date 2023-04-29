import numpy as np
import pyaudio

from beeps import *
from alphabet import morse_dict

class MorsePlayer(object):
    def __init__(self):
        configs = read_beeps_config_file()

        if configs is None:
            print("configs was None")
            sys.exit(1)
        else:
            self.sample_rate = configs['sample_rate']
            self.dit_time = configs['dit_time']
            self.frequency = configs['frequency']

        # dit_time comes from config file
        self.char_space_time = self.dit_time * 3
        self.word_space_time = self.dit_time * 7
        self.dah_time = self.char_space_time

        self.py_audio = mk_pyaudio()
        self.stream = open_stream(self.py_audio, self.sample_rate)

    def __del__(self):
        close_stream(self.stream)
        stop_pyaudio(self.py_audio)

    def dit(self):
        tone(self.stream, self.sample_rate, self.dit_time, self.frequency)

    def dah(self):
        tone(self.stream, self.sample_rate, self.dah_time, self.frequency)

def word_space(stream):
    tone(stream, sample_rate, word_space_time, 0)

def char_space(stream):
    tone(stream, sample_rate, char_space_time, 0)

def el_space(stream):
    tone(stream, sample_rate, dit_time, 0)

def dit_or_dah(stream, s):
    if s == '.':
        dit(stream)
    elif s == '-':
        dah(stream)

def play_ditdahs(stream, s):
    if len(s) == 0:
        return
    elif len(s) == 1:
        dit_or_dah(stream, s)
    else: # more than one
        first = s[0]
        rest = s[1:]

        dit_or_dah(stream, first)

        for c in rest:
            el_space(stream)
            dit_or_dah(stream, c)

def play_word(stream, w):
    if len(w) == 0:
        return
    elif len(w) == 1:
        play_ditdahs(stream, morse_dict[w])
    elif len(w) > 1:
        first = w[0]
        rest = w[1:]

        play_ditdahs(stream, morse_dict[first])

        for c in rest:
            char_space(stream)

            play_ditdahs(stream, morse_dict[c])

def play_string(stream, s):
    words = s.split()

    if len(words) == 0:
        return
    elif len(words) == 1:
        play_word(stream, words[0])
    else:
        first = words[0]
        rest = words[1:]

        play_word(stream, first)

        for w in rest:
            word_space(stream)
            play_word(stream, w)
