#!/usr/bin/env python3
# Adapted from WolfSound video on YouTube
# Code a Wavetable Synth with Python in 6 Minutes Tutorial 
# https://www.youtube.com/watch?v=zBFeT8fkjfI&list=PLJLybGgHYEIeW8OaapEOVelSm-gP9d0MV&index=2

import numpy as np
import scipy.io.wavfile as wav
def main():
    sample_rate = 44100
    f = 440
    t = 2.06666
    waveform = np.sin
    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))
    for n in range(wavetable_length):
        wave_table[n] = waveform(2 * np.pi * n / wavetable_length)
    total_samples = round(t * sample_rate)
    output = np.zeros((total_samples,))
    index = 0
    indexIncrement = f * wavetable_length / sample_rate
    for n in range(output.shape[0]):
        output[n] = wave_table[int(np.floor(index))]
        index += indexIncrement
        index %= wavetable_length
    wav.write('sine440Hz_2.wav', sample_rate, output.astype(np.float32))
if __name__ == '__main__':
    main()

