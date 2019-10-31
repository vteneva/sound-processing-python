from IPython.display import display, Audio


def play_wave(signal, rate):
    audio = Audio(data=signal, rate=rate)
    return display(audio)
