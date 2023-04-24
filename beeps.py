import pyaudio
import numpy as np

def mk_pyaudio():
    py_audio = pyaudio.PyAudio()

    return py_audio

def stop_pyaudio(py_audio):
    py_audio.terminate()

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

def close_stream(stream):
    stream.stop_stream()
    stream.close()

def tone_wavtbl(wave_table, stream, sample_rate, tone_dur, tone_freq):
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
