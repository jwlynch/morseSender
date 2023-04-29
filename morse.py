import numpy as np

def mk_sine_table():
    waveform = np.sin
    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))
    for n in range(wavetable_length):
        wave_table[n] = waveform(2 * np.pi * n / wavetable_length)

    return wave_table

