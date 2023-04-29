#!/usr/bin/env python3
# Adapted From YouTube StackOverflow
# https://stackoverflow.com/questions/31674416/python-realtime-audio-streaming-with-pyaudio-or-something-else
# https://people.csail.mit.edu/hubert/pyaudio/#examples

import pyaudio
import sys
import numpy as np

from beeps import open_stream, close_stream, tone_wavtbl, mk_pyaudio, stop_pyaudio, read_beeps_config_file
from alphabet import morse_dict
from morse import play_string

print("before reading config file")
configs = read_beeps_config_file()
print("after reading config file")

print("before p = pyaudio.PyAudio()")

p = mk_pyaudio()

print("after p = pyaudio.PyAudio()")

print("now create stream")

stream = open_stream(p, sample_rate)

print("done creating stream")

def cq(stream):
    play_string(stream, "CQ CQ CQ")

print("before calling cq()")

cq(stream)

print("after calling cq()")

print("before close_stream(stream)")

close_stream(stream)

print('after close_stream(stream)')

print("before stop_pyaudio(p)")

stop_pyaudio(p)

print("after stop_pyaudio(p)")

