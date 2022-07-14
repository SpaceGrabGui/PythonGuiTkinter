
from cefpython3 import cefpython as cef
from tkinter import *
#import os
#from tkinter import ttk
#from tkinter import messagebox
import tkinter as tk
#import threading
#import multiprocessing
#import sys
import time
#from time import sleep
#from datetime import datetime, timedelta
#from PIL import ImageTk, Image
import locale
#import subprocess
import pyaudio
import struct
import numpy as np
from scipy.fftpack import fft
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
locale.setlocale(locale.LC_ALL, '')

#from threading import Thread
#from tkinterweb import HtmlFrame #import the HTML browser


# constants
CHUNK = 1024                 # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100   

# First line
root = Tk()
font_size = tk.IntVar(value=12)

# configure root
root.title('IPC Spot Inspection')
root.geometry('800x600+300+300')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.configure(bg='#888')

#################################################
#           MENU                                #
#################################################

menubar = tk.Menu(root)
root.configure(menu=menubar)
file = Menu(menubar, tearoff=False)
file.add_command(label="Language")
file.add_command(label="Setting")
file.add_command(label="Folder")
file.add_command(label="Camera")
file.add_command(label="Microphone")
file.add_separator()
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file)
helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label="User Guide", command=root.quit)
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

# Create the status bar on the bottom to show the X,Y coords (in respect to RAW image coords)
status = Label(root, text="X,Y", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

########################################################################
#                           FRAME                                      #
########################################################################
frameHeight = 300
frameWidth = 620

frame = Frame(root)
frame = LabelFrame(root, text="Live Map View")
frame.place(height=frameHeight, width=frameWidth, relx=0.01, rely=0.01)

frame2 = Frame(root)
frame2 = LabelFrame(root, text="Specification Sheet")
frame2.place(height=frameHeight, width=frameWidth, relx=0.34, rely=0.01)

frame3 = Frame(root)
frame3 = LabelFrame(root, text="Audio Feed")
frame3.place(height=frameHeight, width=frameWidth, relx=0.67, rely=0.01)

########################################################################
#                       PLOT AUDIO SPECTRUM                            #
########################################################################

# create matplotlib figure and axes
fig, ax = plt.subplots(1, figsize=(15, 7))

# pyaudio class instance
p = pyaudio.PyAudio()

# get list of availble inputs
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print ("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

# select input
audio_input = input("\n\nSelect input by Device id: ")

# stream object to get data from microphone
stream = p.open(
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
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

# basic formatting for the axes
ax.set_title('AUDIO WAVEFORM')
ax.set_xlabel('samples')
ax.set_ylabel('volume')
ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

canvas = FigureCanvasTkAgg(fig, master=frame3)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.X)
toolbar = NavigationToolbar2Tk(canvas, frame3)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP)

# show the plot
#plt.show(block=False)

print('stream started')

# for measuring frame rate
frame_count = 0
start_time = time.time()

while True:

    # binary data
    data = stream.read(CHUNK)

    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = np.array(data_int, dtype='b')[::2] + 128

    line.set_ydata(data_np)

    #update figure canvas
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
    except TclError:

        # calculate average frame rate
        frame_rate = frame_count / (time.time() - start_time)

        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break

frame4 = Frame(root, bg="grey")
frame4 = LabelFrame(root, text="Mission Progress Status")
frame4.place(height=frameHeight, width=frameWidth, relx=0.01, rely=0.33)

frame5 = Frame(root, bg="grey")
frame5 = LabelFrame(root, text="IR Camera Feed")
frame5.place(height=frameHeight, width=frameWidth, relx=0.34, rely=0.33)
    
frame6 = Frame(root, bg="grey")
frame6 = LabelFrame(root, text="Eqipment Images - Screen 1")
frame6.place(height=frameHeight, width=frameWidth, relx=0.67, rely=0.33)
    
frame7 = Frame(root, bg="grey")
frame7 = LabelFrame(root, text="Eqipment Images - Screen 1")
frame7.place(height=frameHeight, width=frameWidth, relx=0.01, rely=0.65)

frame8 = Frame(root, bg="grey")
frame8 = LabelFrame(root, text="Eqipment Images - Screen 2")
frame8.place(height=frameHeight, width=frameWidth, relx=0.34, rely=0.65)
    
frame9 = Frame(root, bg="grey")
frame9 = LabelFrame(root, text="Eqipment Images - Screen 3")
frame9.place(height=frameHeight, width=frameWidth, relx=0.67, rely=0.65)
        

#################################################
#         FUNCTION AND BINDINGS                 #
#################################################


#################################################
#            MAIN LOOP                         #
#################################################

root.mainloop()

