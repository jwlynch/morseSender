#!/usr/bin/env python3
# Adapted From YouTube StackOverflow
# https://stackoverflow.com/questions/31674416/python-realtime-audio-streaming-with-pyaudio-or-something-else
# https://people.csail.mit.edu/hubert/pyaudio/#examples

import pyaudio
import sys
import numpy as np

from beeps import open_stream, close_stream, tone_wavtbl, mk_pyaudio, stop_pyaudio, read_beeps_config_file
from alphabet import morse

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
        play_ditdahs(morse[w])
    elif len(w) > 1:
        first = w[0]
        rest = w[1:]

        play_ditdahs(morse[first])

        for c in rest:
            char_space()

            play_ditdahs(morse[c])

def play_string(s):
    words = s.split()

    if len(words) == 0:
        return
    elif len(s) == 1:
        play_ditdahs(words[0])
    else:
        first = words[0]
        rest = words[1:]

        play_word(first)

        for w in rest:
            word_space()
            play_word(w)

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

def tone(stream, sample_rate, tone_dur, tone_freq):
    # Sine table
    wave_table = mk_sine_table()

    tone_wavtbl(wave_table, stream, sample_rate, tone_dur, tone_freq)

print("before p = pyaudio.PyAudio()")

p = mk_pyaudio()

print("after p = pyaudio.PyAudio()")

print("now create stream")

stream = open_stream(p, sample_rate)

print("done creating stream")

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

def cq():
    play_string("CQ CQ CQ")

print("before calling cq()")

cq()

print("after calling cq()")

print("before close_stream(stream)")

close_stream(stream)

print('after close_stream(stream)')

print("before stop_pyaudio(p)")

stop_pyaudio(p)

print("after stop_pyaudio(p)")

