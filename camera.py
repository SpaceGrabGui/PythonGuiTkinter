#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter as tk
import threading
import multiprocessing
import sys
import time
from configfile import *
import cv2
import PIL.Image, PIL.ImageTk
import locale
import audio
import pyaudio
import struct
import numpy as np
from scipy.fftpack import fft
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
locale.setlocale(locale.LC_ALL, '')
import subprocess
from imutils.video import VideoStream

inifile = "config.ini"

# First line
root = Tk()

# configure root
appTitle = root.title('IPC Spot Inspection')

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

screen_resolution = str(width)+'x'+str(height)

#if width <= 1366:
#    height = 768
#    width = 1366
#    root.geometry(screen_resolution)
#if width <= 3286:
#    height = 1080
#    width = 3286

root.geometry(screen_resolution)

#root.geometry('800x600+300+300')
root.resizable(1, 1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.configure(bg='#888')

LoadPreferences(inifile)
root.update()

#Get the USER INFO
userinfo = get_UserInfo(inifile, True)
serverinfo = get_ServerInfo(inifile, True)

frameHeight = (root.winfo_height() - 100) / 3
frameWidth = (root.winfo_width()) / 3.1

#frameHeight = (height - 390) / 3
#frameWidth = (width - 400) / 3

print("Width : ", width)
print("Height : ", height)

print("Frame Height : ", frameHeight)
print("Frame Width : ", frameWidth)

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
status = Label(root, text="User : {}".format(userinfo["user"]), bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

########################################################################
#                           FRAME                                      #
########################################################################
#frameHeight = 300
#frameWidth = 620

frame = Frame(root)
frame = LabelFrame(root, text="Live Map View")
frame.place(height=frameHeight, width=frameWidth, relx=0.01, rely=0.01)

frame2 = Frame(root)
frame2 = LabelFrame(root, text="Specification Sheet")
frame2.place(height=frameHeight, width=frameWidth, relx=0.34, rely=0.01)

frame3 = Frame(root)
frame3 = LabelFrame(root, text="Audio Feed")
frame3.place(height=frameHeight, width=frameWidth, relx=0.67, rely=0.01)

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

########################################################################
#                          AUDIO STREAMING                             #
########################################################################

########################################################################
#                      VIDEO STREAMING                                 #
########################################################################

frame5Lable = tk.Label(root)

frame5Lable.place(height=frameHeight-25, width=frameWidth-10, relx=0.343, rely=0.35)

print("Start Video Streaming")
#vs = cv2.VideoCapture(0)

#Get Username, Password and Server Info
username = userinfo["username"]
password = userinfo["password"]
ip = serverinfo["ipaddr"]
port = serverinfo["port"]
proto = serverinfo["proto"]

spotCamera = 'rtsp://'+username+':'+password+'@'+ip+':'+port+'/'
print(spotCamera)

videostream = cv2.VideoCapture(spotCamera, cv2.CAP_GSTREAMER)

if not videostream.isOpened():
    frame5Lable = Label(root, text="Cannot Connect to the Robot Camera", fg="red", font = ('Helvetica', 12, 'bold'))
    frame5Lable.place(height=frameHeight-25, width=frameWidth-10, relx=0.343, rely=0.35)
#    print('Cannot open RTSP stream')
    videostream.release()

def video_stream(): 
#    vs = cv2.VideoCapture('rtsp://admin:pg7ggc385h84@192.168.10.24:31102/h264.sdp.html')
    ok, frame = videostream.read()
    if ok:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        current_image = PIL.Image.fromarray(cv2image)  # convert image for PIL
        imgtk = PIL.ImageTk.PhotoImage(image=current_image)  # convert image for tkinter
        frame5Lable.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        frame5Lable.config(image=imgtk)  # show the image

    root.after(20, video_stream)  # call the same function after 30 milliseconds

#################################################
#         FUNCTION AND BINDINGS                 #
#################################################

if __name__ == "__main__":
  

#################################################
#            MAIN LOOP                         #
#################################################

    #audio_stream()
    video_stream()
    root.mainloop()

