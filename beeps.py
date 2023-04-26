import os, sys
from configparser import ConfigParser

import pyaudio
import numpy as np

def read_beeps_config_file():
    # first, find config file if it exists, in one of three places:

    home_dir = os.path.expanduser('~')

    # start with cfg_path being an empty string, the next three ifs might set it to a path
    # but if not, it means no config file was found (this is an error condition)
    cfg_path = ""

    # first possibility, the example config file
    if os.path.exists('beeps-cfg-example.cfg'):
        cfg_path = "beeps-cfg-example.cfg"
    # second possibility, beeps.cfg in same dir as script file
    elif os.path.exists("beeps.cfg"):
        # cfg file is in same dir with python script
        cfg_path = "beeps.cfg"
    # third possibility, beeps.cfg in ~/.config/beeps/beeps.cfg
    elif os.path.exists(f"{home_dir}/.config/beeps/beeps.cfg"):
        # cfg file is in home/.config/beeps/beeps.cfg
        cfg_path = f"{home_dir}/.config/beeps/beeps.cfg"

    if cfg_path == "":
        # no config file found
        cfg = False
    else:
        # config file found and path in cfg_path
        cfg = True

    if cfg:
        # read config file
        pass
    else:
        print("Error: No config file found")
        sys.exit(1)

def mk_pyaudio():
    """make and return a pyaudio object"""
    py_audio = pyaudio.PyAudio()

    return py_audio

def stop_pyaudio(py_audio):
    """close/terminate a pyaudio object"""
    py_audio.terminate()

def open_stream(py_audio, sample_rate):
    """create and return a stream object at specified sample rate"""
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

def close_stream(stream):
    """close a stream"""
    stream.stop_stream()
    stream.close()

def tone_wavtbl(wave_table, stream, sample_rate, tone_dur, tone_freq):
    """play tone with wave in wave_table, and with specified sample rate, duration and frequency"""
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
