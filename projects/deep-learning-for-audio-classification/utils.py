import numpy as np
import pandas as pd
from IPython.display import display, Audio


def play_wave(signal, rate):
    audio = Audio(data=signal, rate=rate)
    return display(audio)


def envelope(signal, sample_rate, chunks_per_second):
    """
    chunks_per_second: Number of chunks in 1 second
    """
    window_size = int(sample_rate / chunks_per_second)

    rolling_mean_amplitude = (pd.Series(np.abs(signal))
                              .rolling(window=window_size, min_periods=1, center=True)
                              .mean())
    return rolling_mean_amplitude
