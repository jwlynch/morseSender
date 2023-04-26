#!/usr/bin/env python3
# Adapted From YouTube StackOverflow
# https://stackoverflow.com/questions/31674416/python-realtime-audio-streaming-with-pyaudio-or-something-else
# https://people.csail.mit.edu/hubert/pyaudio/#examples

import pyaudio
import sys
import numpy as np

from beeps import open_stream, close_stream, tone_wavtbl, mk_pyaudio, stop_pyaudio, read_beeps_config_file

def mk_sine_table():
    waveform = np.sin
    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))
    for n in range(wavetable_length):
        wave_table[n] = waveform(2 * np.pi * n / wavetable_length)

    return wave_table

def tone(stream, sample_rate, tone_dur, tone_freq):
    # Sine table
    wave_table = mk_sine_table()

    tone_wavtbl(wave_table, stream, sample_rate, tone_dur, tone_freq)

print("before p = pyaudio.PyAudio()")

p = mk_pyaudio()

print("after p = pyaudio.PyAudio()")

print("now create stream")

stream = open_stream(p, 48000)

print("done creating stream")

dit_time = 0.06 # 60 ms
char_space_time = dit_time * 3
word_space_time = dit_time * 7
dah_time = char_space_time

def dit():
    tone(stream, 48000, dit_time, 440)

def dah():
    tone(stream, 48000, dah_time, 440)

def word_space():
    tone(stream, 48000, word_space_time, 0)

def char_space():
    tone(stream, 48000, char_space_time, 0)

def el_space():
    tone(stream, 48000, dit_time, 0)

def cq():
    dah()
    el_space()
    dit()
    el_space()
    dah()
    el_space()
    dit()

    char_space()

    dah()
    el_space()
    dah()
    el_space()
    dit()
    el_space()
    dah()

print("before calling cq()")

cq()

print("after calling cq()")

print("before close_stream(stream)")

close_stream(stream)

print('after close_stream(stream)')

print("before stop_pyaudio(p)")

stop_pyaudio(p)

print("after stop_pyaudio(p)")

