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


def write_single_audio_file(write_locn, audio, sampling_rate):
    try:
        librosa.output.write_wav(write_locn, audio, sampling_rate)
    except Exception as e:
        print(traceback.format_exc())
        raise e


def resample_audio(audio, sampling_rate, new_sampling_rate):
    try:
        return librosa.resample(audio, sampling_rate, new_sampling_rate)
    except Exception as e:
        print(traceback.format_exc())
        raise e


def break_audio_by_beats(file_locn, write_locn):
    try:
        audio, sampling_rate = load_single_audio_file(file_locn)
        tempo, beat_frames = librosa.beat.beat_track(audio, sr=sampling_rate)
        beat_times = librosa.frames_to_time(beat_frames, sr=sampling_rate)
        total_duration = audio.shape[0]/sampling_rate
        beat_indices = np.int64(beat_times*audio.shape[0]/total_duration)
        for idx in range(beat_indices.shape[0]):
            if idx == beat_indices.shape[0]-1:
                break
            nslice = data_resample[beat_indices[idx]:beat_indices[idx+1]]
            write_single_audio_file(os.path.join(write_locn, os.path.basename(file_locn)+'_'+str(idx)+'.wav'), nslice,sampling_rate)
    except Exception as e:
        print(traceback.format_exc())
        raise e
