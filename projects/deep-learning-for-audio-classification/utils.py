import numpy as np
import pandas as pd
from IPython.display import display, Audio


def play_wave(signal, rate):
    audio = Audio(data=signal, rate=rate)
    return display(audio)


def envelope(signal, sample_rate):
    window_size = int(sample_rate / 10)

    rolling_mean_amplitude = (pd.Series(np.abs(signal))
                              .rolling(window=window_size, min_periods=1, center=True)
                              .mean())
    return rolling_mean_amplitude
