#! /usr/bin/python3

import pyaudio
import time
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

#init du rec mic
stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

#start du rec mic
stream.start_stream()

#boucle inf: check ur db
while stream.is_active():
    if (rms > 1):
        db = 40 * log10(rms)
    else:
        db = 0
    print(f"RMS: {rms} DB: {db}") 
    # refresh every 0.3 seconds 
    time.sleep(0.1)

#fin du rec mic
stream.stop_stream()
stream.close()

p.terminate()