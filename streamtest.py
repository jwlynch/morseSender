#!/usr/bin/env python3
# Adapted From YouTube StackOverflow
# https://stackoverflow.com/questions/31674416/python-realtime-audio-streaming-with-pyaudio-or-something-else
# https://people.csail.mit.edu/hubert/pyaudio/#examples

import pyaudio
import sys
import numpy as np

def mk_sine_table():
    waveform = np.sin
    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))
    for n in range(wavetable_length):
        wave_table[n] = waveform(2 * np.pi * n / wavetable_length)

    return wave_table

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

p = pyaudio.PyAudio()

# sample_format = p.get_format_from_width(sample_width)
# print(f"sample format is {sample_format}")

print("after p = pyaudio.PyAudio()")

print("now create stream")

def open_stream(py_audio, sample_rate):
    # samples are 32 bit floats
    sample_width = 4
    sample_format = py_audio.get_format_from_width(sample_width)

    # Stream should have one channel
    channels = 1
    stream = py_audio.open(
                        format=sample_format,
                        channels=channels,
                        rate=sample_rate,
                        output=True
                          )

    return stream

print("done creating stream")

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

def tone(stream, sample_rate, tone_dur, tone_freq):
    # Sine table
    wave_table = mk_sine_table()

    # Length of wave table
    wavetable_length = len(wave_table)

    # Current index into sine table
    index = 0.0

    # How much to increment index for each sample
    indexIncrement = tone_freq * wavetable_length / sample_rate

    # Total number of samples to send to the stream
    total_samples = round(tone_dur * sample_rate)

    for n in range(total_samples):
        sample_container = np.zeros((1,))
        sample_container[0] = wave_table[int(np.floor(index))]
        stream.write(sample_container.astype(np.float32), 1)
        index += indexIncrement
        index %= wavetable_length

print("before stop and close stream")

def close_stream(stream):
    stream.stop_stream()
    stream.close()

print('after stop and close stream')

print("before p.terminate()")

p.terminate()

print("after p.terminate()")

