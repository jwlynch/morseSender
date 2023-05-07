import os, sys
from configparser import ConfigParser

import pyaudio
import numpy as np

def read_beeps_config_file():
    """read config file. return a dict with the config params."""
    result = {} # default

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
        result = {} # put config values in this dict

        # read config file
        config = ConfigParser()

        config.read(cfg_path)

        if config.has_section("audio"):
            if config.has_option('audio', 'sample_rate'):
                smpl_rate = config['audio']['sample_rate']
            else:
                smpl_rate = '12000' # default
        
            if config.has_option('audio', 'frequency'):
                frq = config['audio']['frequency']
            else:
                frq = '440' # default

            if config.has_option('audio', 'dit_time'):
                dt_tm = config['audio']['dit_time']
            else:
                dt_tm = '.060' # default, 60 ms
        else:
            # all defaults
            smpl_rate = '12000' # default
            frq = '440' # default
            dt_tm = '.060' # default

        # convert config data from strings to numeric
        result['sample_rate'] = int(smpl_rate)
        result['dit_time'] = float(dt_tm)
        result['frequency'] = int(frq)

        if config.has_section("morse"):
        else: # no morse section in config file (so take defaults)
            result['char_space_mult'] = 3
            result['word_space_mult'] = 7
            result['dah_mult'] = 3
    else:
        print("Error: No config file found")
        raise FileNotFoundError("beeps config file")
    
    return result

def mk_sine_table():
    waveform = np.sin
    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))
    for n in range(wavetable_length):
        wave_table[n] = waveform(2 * np.pi * n / wavetable_length)

    return wave_table

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

def tone(stream, sample_rate, tone_dur, tone_freq):
    # Sine table
    wave_table = mk_sine_table()

    tone_wavtbl(wave_table, stream, sample_rate, tone_dur, tone_freq)

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
