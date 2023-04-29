import numpy as np

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

