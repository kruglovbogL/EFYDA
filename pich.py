import parselmouth
from IPython.display import Audio
import numpy as np
import matplotlib.pyplot as plt
from parselmouth.praat import call

import winsound


def get_pich():
    # Plot nice figures using Python's "standard" matplotlib library
    morning = "D:\EFYDA\sound.wav"
    snd = parselmouth.Sound(morning)
    # If desired, pre-emphasize the sound fragment before calculating the spectrogram
    pre_emphasized_snd = snd.copy()
    pre_emphasized_snd.pre_emphasize()
    Audio(data=snd.values, rate=snd.sampling_frequency)
    manipulation = call(snd, "To Manipulation", 0.01, 75, 600)
    pitch_tier = call(manipulation, "Extract pitch tier")
    call(pitch_tier, "Multiply frequencies", snd.xmin, snd.xmax, 2.07)  #2 it number pitch 
    call([pitch_tier, manipulation], "Replace pitch tier")
    sound_octave_up = call(manipulation, "Get resynthesis (overlap-add)")
    type(sound_octave_up)
    Audio(data=sound_octave_up.values, rate=sound_octave_up.sampling_frequency)
    sound_octave_up.save("4_b_octave_up.wav", "WAV")
    up_sound = "4_b_octave_up.wav"
    winsound.PlaySound(up_sound, winsound.SND_FILENAME)


