import pandas as pd
import librosa
import traceback
from librosa import display
from matplotlib import pyplot as plt


def load_single_audio_file(file_locn, duration=None):
    try:
        data, sampling_rate = librosa.load(file_locn, duration=duration, res_type='kaiser_fast')
        return data, sampling_rate
    except Exception as e:
        print(traceback.format_exc())
        raise e


def display_plot(data):
    try:
        plt.figure(figsize = (12, 4))
        display.waveplot(data, sr=sampling_rate)
        plt.show()
    except Exception as e:
        print(traceback.format_exc())
        raise e
