#! /usr/bin/python3

import pyaudio
import time
import pygame
from math import log10
import audioop

p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
rms = 1
db = 0

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH)
    return in_data, pyaudio.paContinue

stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

def use_mic():
    if (rms > 1):
        db = 40 * log10(rms)
    else:
        db = 0
    return db

def close_mic():
    stream.stop_stream()
    stream.close()
    p.terminate()
