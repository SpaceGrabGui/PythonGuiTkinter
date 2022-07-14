import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError

# constants
CHUNK = 1024 *4             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100

# pyaudio class instance
audioClass = pyaudio.PyAudio()

# create matplotlib figure and axes
figure, axes = plt.subplots(1, figsize=(15, 7))

# get list of availble inputs
info = audioClass.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (audioClass.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print ("Input Device ID ", i, " - ", audioClass.get_device_info_by_host_api_device_index(0, i).get('name'))

# select input
audio_input = input("\n\nSelect Input by Device ID : ")

# stream object to get data from microphone
stream = audioClass.open(
    input_device_index=int(audio_input),
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# variable for plotting
x = np.arange(0, 2 * CHUNK, 2)

# create a line object with random data
line, = axes.plot(x, np.random.rand(CHUNK), '-', lw=2)

# basic formatting for the axes
axes.set_title('AUDIO WAVEFORM')
axes.set_xlabel('samples')
axes.set_ylabel('volume')
axes.set_ylim(0, 255)
axes.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

# show the plot
plt.show(block=False)

print('Start Streaming')

# for measuring frame rate
frameCount = 0
start_time = time.time()

while True:

    # Read the sound as binary data
    data = stream.read(CHUNK)

    # convert data to integers, make np array, then offset it by 127
    dataInt = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = np.array(dataInt, dtype='b')[::2] + 128

    line.set_ydata(data_np)

    # update figureure canvas
    try:
        figure.canvas.draw()
        figure.canvas.flush_events()
        frameCount += 1

    except TclError:

        # calculate average frame rate
        frameRate = frameCount / (time.time() - start_time)

        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frameRate))
        break