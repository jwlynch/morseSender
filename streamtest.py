#!/usr/bin/env python3
# Adapted From YouTube StackOverflow
# https://stackoverflow.com/questions/31674416/python-realtime-audio-streaming-with-pyaudio-or-something-else
# https://people.csail.mit.edu/hubert/pyaudio/#examples

import pyaudio
import sys
import numpy as np

from beeps import open_stream, close_stream, tone_wavtbl, mk_pyaudio, stop_pyaudio

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

#CHUNK = 1024

#if len(sys.argv) < 2:
#    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#    sys.exit(-1)

# sample_rate = 44100
# sample_width = 4
# channels = 1
# t = 3
# f = 440

# index = 0.0
# indexIncrement = f * wavetable_length / sample_rate

# total_samples = round(t * sample_rate)

# wf = wave.open(sys.argv[1], 'rb')

# sample_format = p.get_format_from_width(sample_width)
# print(f"sample format is {sample_format}")

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

#data = wf.readframes(CHUNK)

#while data != '':
#    stream.write(data)
#    data = wf.readframes(CHUNK)

# print(f"type of wave_table element is {type(wave_table[0])}")
# sample_container = np.zeros((1,))
# print(f"tuple fed to stream.write is {(sample_container, 1)}")

# for n in range(total_samples):
#     print(f"sin: {wave_table[int(np.floor(index))]}, index: {index}")
#     index += indexIncrement
#     index %= wavetable_length

print("before stop and close stream")

close_stream(stream)

print('after stop and close stream')

print("before p.terminate()")

stop_pyaudio(p)

print("after p.terminate()")

