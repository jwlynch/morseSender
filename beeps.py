import pyaudio
import numpy as np

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
