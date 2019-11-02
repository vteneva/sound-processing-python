import os
import os.path as p

import librosa
import pandas as pd
from scipy.io import wavfile

from utils import envelope

DATA_DIR = r'../../data/freesound-audio-tagging/audio_train'
DEST_DIR = r'clean'
NOISE_AMPLITUDE_THRESHOLD = 0.005
DOWNSAMPLED_SAMPLE_RATE = 16000
DATA_CHUNKS_PER_SECOND = 10


def process_signal(filename):
    signal, sample_rate = librosa.load(p.join(DATA_DIR, filename), sr=DOWNSAMPLED_SAMPLE_RATE)
    rolling_mean_signal = envelope(signal, sample_rate, DATA_CHUNKS_PER_SECOND)
    noise_mask = rolling_mean_signal > NOISE_AMPLITUDE_THRESHOLD
    wavfile.write(filename=p.join(DEST_DIR, filename),
                  rate=DOWNSAMPLED_SAMPLE_RATE,
                  data=signal[noise_mask])


if __name__ == '__main__':
    audio_data = pd.read_csv('instruments.csv')

    os.makedirs(DEST_DIR)
    audio_data.fname.apply(process_signal)
