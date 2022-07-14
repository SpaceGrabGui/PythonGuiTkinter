
from cefpython3 import cefpython as cef
from tkinter import *
import os

# from tkinter import filedialog
from tkinter import ttk
from tkwebview2.tkwebview2 import WebView2
# import urllib
# import tkinterweb as tkinterweb
# !! from tkhtmlview import HTMLLabel
import threading
import sys
# import webbrowser
import time
from datetime import datetime, timedelta
from PIL import ImageTk, Image
import locale
import subprocess
locale.setlocale(locale.LC_ALL, '')

global frameHeight
global frameWidth
from tkinterweb import HtmlFrame #import the HTML browser
try:
  import tkinter as tk #python3
except ImportError:
  import Tkinter as tk #python2

# For full screen view depends on PC window size
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<Escape>', self.toggle_geom)
    def toggle_geom(self,event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

# To open web browser In Frame 3,5,6,
def embed_browser_thread():
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo(frame5.winfo_id())
    window_info.SetAsChild(frame5.winfo_id(), [0, 0, frameWidth, frameHeight])
    window_info2 = cef.WindowInfo(frame6.winfo_id())
    window_info2.SetAsChild(frame6.winfo_id(), [0, 0, frameWidth, frameHeight])
    window_info3 = cef.WindowInfo(frame3.winfo_id())
    window_info3.SetAsChild(frame3.winfo_id(), [0, 0,
                                                frameWidth, frameHeight])
    cef.Initialize()
    cef.CreateBrowserSync(window_info, url=frame5Url)
    cef.CreateBrowserSync(window_info2, url=frame6Url)
    cef.CreateBrowserSync(window_info3, url=frame3Url)
    cef.MessageLoop()
#To call web view in tkinter frame
def webBrowser():
    embed_browser_thread()

def open_win():

    # This is used to open the respective folder when press 前回 button　
    subprocess.Popen('explorer "C:\path\of\folder"')

 # This function is used to change the image to backwards
def back():
    global m
    global totalNoOfPhotos
    global noOfPhotosPerTime
    global PreviousPhotoIdentifier
    global Frame7imglabel
    global buttonback
    global buttonForward
    global Frame7Image
    global Frame7img
    global previous
    global previous_time
    global filename
    # Get previous photo filename when backward button is press
    if int(filename) % 2 == 0 :
        filename = str(int(filename)-1)
    else:
        previous = datetime.today() - timedelta(days=m)
        previous_time = previous.strftime("%Y%m%d")
        filename = previous_time + "2"
        m += 1

    print(filename)
    # Use Hyperlink to shows the Image in Frame7
    try:
        Frame7img = Image.open('/Users/AW1/OneDrive - 山口電気工事株式会社　＊/デスクトップ' + filename + ".png")
        resize = Frame7img.resize((400, 250))
        Frame7Image = ImageTk.PhotoImage(resize)
        Frame7imglabel = Label(frame7, image=Frame7Image)
        # mylabel.grid(row=0, column=0, columnspan=3)

        Frame7imglabel.place(height=frameHeight - 20, width=frameWidth - 10, relx=0.01, rely=0)
        NameOfPhotosName = Label(frame7, text=filename, bg="black", fg="white")
        NameOfPhotosName.place(height=30, width=100, relx=0.01, rely=0.92)
    except:
        print("error at back button")
#This function command is used to change the image to forward
def front():
    global totalNoOfPhotos
    global m
    global PreviousPhotoIdentifier
    global Frame7imglabel
    global buttonback
    global buttonForward
    global Frame7Image
    global previous
    global previous_time
    global Frame7img
    global filename
    # Get previous photo filename when forward is press
    if int(filename) % 2 == 0:
        previous = datetime.today() - timedelta(days=(m - 1))
        previous_time = previous.strftime("%Y%m%d")
        filename = previous_time + "1"

    else:
        filename = str(int(filename) + 1)
        m -= 1

    print(filename)
    # Use Hyperlink to show the Image in Frame7
    try:
        Frame7img = Image.open('/Users/AW1/OneDrive - 山口電気工事株式会社　＊/デスクトップ' + filename + ".png")
        Frame7resize = Frame7img.resize((400, 250))
        Frame7Image = ImageTk.PhotoImage(Frame7resize)
        Frame7imglabel = Label(frame7, image=Frame7Image)
        # mylabel.grid(row=0, column=0, columnspan=3)
        Frame7imglabel.place(height=frameHeight - 20, width=frameWidth - 10, relx=0.01, rely=0)
        Frame7fileName = Label(frame7, text=filename, bg="black", fg="white")
        Frame7fileName.place(height=30, width=100, relx=0.01, rely=0.92)
    except:
        print("error at forward button ")

# This function is used to reload the whole application for every second
def update_info():
    global now
    global totalNoOfPhotos
    global PreviousPhotoIdentifier
    now = datetime.now()
    global current_time
    global Frame8imgLabel
    global Frame8Image
    global Frame8Img
    global Frame8resize
    global yesterday
    global yesterday_time
    global Frame9ImgLabel
    global Frame9Image
    global Frame9img
    global Frame9Resize
    global previous
    global previous_time
    global Frame7imglabel
    global buttonback
    global buttonForward
    global Frame7Image
    global resize
    global Frame2imgLabel
    global Frame2Image
    global Frame2img
    global Frame2resize
    global noOfPhotosPerTime
    global filename
    global x
    global x1
    global x2
    global y
    global c
    global y1
    global c1
    global y2
    global c2
    global x3
    global y3
    global c3
    global x4
    global y4
    global c4
    global x5
    global y5
    global c5

    print(yesterday_time)
    # Get Todays date to Identify the file name of current image screen.
    current_time = now.strftime("%Y%m%d")
    print(current_time)
    # Schedule screen variables and design
    scheduleLabel = Label(frame4, text="Spot -スケジュール", bg="black", fg="white", )
    scheduleLabel.place(height=30, width=120, relx=0.01, rely=0.01)
    # It's used to show the current Time
    live = datetime.now()
    # livetiming = live.strftime("%Y年%m月%d日 %H時%M分")
    # This format does the same as the previous, it just calls the unicode characters after the call
    livetiming = live.strftime('%Y{0}%m{1}%d{2} %H{3}%M{4}').format(*'年月日時分')
    timeLabel = Label(frame4, text=livetiming, bg="black", fg="white")
    timeLabel.place(height=30, width=220, relx=0.6, rely=0.01)
    missonlabel = Label(frame4,text="ミッション",bg="black", fg="white")
    missonlabel.place(height=30, width=60, relx=0.02, rely=0.1)
    progressLabel = Label(frame4, text="進捗", bg="black", fg="white")
    progressLabel.place(height=30, width=50, relx=0.45, rely=0.1)
    statusLabel = Label(frame4,text="状態",bg="black", fg="white")
    statusLabel.place(height=30, width=50, relx=0.85, rely=0.1)
    stLabel = Label(frame4, text ="ST室", bg="black", fg="white")
    stLabel.place(height=30, width=50, relx=0.02, rely=0.25)
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("blue.Horizontal.TProgressbar", troughcolor="black", foreground='light green', background='light green')
    stProgress = ttk.Progressbar(frame4, style="blue.Horizontal.TProgressbar", mode='determinate',length=330, maximum=16, value=x)
    stProgress.place(height=20, relx=0.18, rely=0.26)
    stStatus = Label(frame4, text=y, bg="black", fg=c)
    stStatus.place(height=30, width=50, relx=0.86, rely=0.25)
    #gas turbine
    GTLabel = Label(frame4, text="GT室", bg="black", fg="white")
    GTLabel.place(height=30, width=50, relx=0.02, rely=0.35)
    GTProgress = ttk.Progressbar(frame4, style="blue.Horizontal.TProgressbar", mode='determinate', length=330,
                                 maximum=12, value=x1)
    GTProgress.place(height=20, relx=0.18, rely=0.36)
    GTStatus = Label(frame4, text=y1, bg="black", fg=c1)
    GTStatus.place(height=30, width=50, relx=0.86, rely=0.35)
    BoilerLabel = Label(frame4, text="ボイラー", bg="black", fg="white")
    BoilerLabel.place(height=30, width=50, relx=0.02, rely=0.45)
    BoilerProgress = ttk.Progressbar(frame4, style="blue.Horizontal.TProgressbar", mode='determinate', length=330,
                                 maximum=12, value=x2)
    BoilerProgress.place(height=20, relx=0.18, rely=0.46)
    BoilerStatus = Label(frame4, text=y2, bg="black", fg=c2)
    BoilerStatus.place(height=30, width=50, relx=0.86, rely=0.45)
    # For second time inspection

    stLabel1 = Label(frame4, text="ST室2回", bg="black", fg="white")
    stLabel1.place(height=30, width=70, relx=0.02, rely=0.55)
    stProgress1 = ttk.Progressbar(frame4, style="blue.Horizontal.TProgressbar", mode='determinate', length=330,
                                 maximum=16, value=x3)
    stProgress1.place(height=20, relx=0.18, rely=0.56)
    stStatus1 = Label(frame4, text=y3, bg="black", fg=c3)
    stStatus1.place(height=30, width=50, relx=0.86, rely=0.55)
    GTLabel1 = Label(frame4, text="GT室2回", bg="black", fg="white")
    GTLabel1.place(height=30, width=70, relx=0.02, rely=0.65)
    GTProgress1 = ttk.Progressbar(frame4, style="blue.Horizontal.TProgressbar", mode='determinate', length=330,
                                 maximum=12, value=x4)
    GTProgress1.place(height=20, relx=0.18, rely=0.66)
    GTStatus1 = Label(frame4, text=y4, bg="black", fg=c4)
    GTStatus1.place(height=30, width=50, relx=0.86, rely=0.65)
    BoilerLabel1 = Label(frame4, text="ボイラー2回", bg="black", fg="white")
    BoilerLabel1.place(height=30, width=70, relx=0.02, rely=0.75)
    BoilerProgress1 = ttk.Progressbar(frame4, style="blue.Horizontal.TProgressbar", mode='determinate', length=330,
                                     maximum=12, value=x5)
    BoilerProgress1.place(height=20, relx=0.18, rely=0.76)
    BoilerStatus1 = Label(frame4, text=y5, bg="black", fg=c5)
    BoilerStatus1.place(height=30, width=50, relx=0.86, rely=0.75)
    # This is used to identify the Filename for respective screen ↓↓↓
    # Get image from NasDatabase to Actual image Screen (frame9)

    try:

        Frame9img = Image.open('/Users/AW1/OneDrive - 山口電気工事株式会社　＊/デスクトップ' + current_time + str(noOfPhotosPerTime) + ".png")
        Frame9Resize = Frame9img.resize((400, 300))
        Frame9Image = ImageTk.PhotoImage(Frame9Resize)
        Frame9ImgLabel = Label(frame9, image=Frame9Image)
        Frame9ImgLabel.place(height=frameHeight - 20, width=frameWidth - 10, relx=0.01, rely=0)
    except:
        print("frame9 No photos")
   # mylabel_now.grid_forget()

    # Get image from NasDatabase to Previous Image screen (frame7)
    try:
        #Get yesterday date to Identify the file name of Previous image screen (Frame 7).
        img = Image.open('/Users/AW1/OneDrive - 山口電気工事株式会社　＊/デスクトップ' + yesterday_time + str(noOfPhotosPerTime) + ".png")
        resize = img.resize((400, 250))
        Frame7Image = ImageTk.PhotoImage(resize)
        Frame7imglabel = Label(frame7, image=Frame7Image)
        # mylabel.grid(row=0, column=0, columnspan=3)
        Frame7imglabel.place(height=frameHeight - 20, width=frameWidth - 10, relx=0.01, rely=0)
    except:
        print("error")
    try:
        Frame2img = Image.open('/Users/AW1/OneDrive - 山口電気工事株式会社　＊/デスクトップ' + current_time + str(noOfPhotosPerTime) + ".png")
        Frame2resize = Frame2img.resize((400, 300))
        Frame2Image = ImageTk.PhotoImage(Frame2resize)
        Frame2imgLabel = Label(frame2, image=Frame2Image)
        Frame2imgLabel.place(height=frameHeight - 20, width=frameWidth - 10, relx=0.01, rely=0)

    except:
        print("frame2 No photos")
    # get image from NasDatabase to Current Image screen (frame8)
    try:
        Frame8Img = Image.open('/Users/AW1/OneDrive - 山口電気工事株式会社　＊/デスクトップ/test1/' + current_time + str(totalNoOfPhotos) + ".png")
        Frame8resize = Frame8Img.resize((400, 300))
        Frame8Image = ImageTk.PhotoImage(Frame8resize)
        Frame8imgLabel = Label(frame8, image=Frame8Image)
        Frame8imgLabel.place(height=frameHeight - 20, width=frameWidth - 10, relx=0.01, rely=0)
        totalNoOfPhotos += 1
        noOfPhotosPerTime += 1
        PreviousPhotoIdentifier += 1
        if totalNoOfPhotos >= 11:
            yesterday = datetime.today() - timedelta(days=-1)
            yesterday_time = yesterday.strftime("%Y%m%d")
            totalNoOfPhotos = 1
            noOfPhotosPerTime = 1
            PreviousPhotoIdentifier = 6
        elif totalNoOfPhotos == 6:
            yesterday = datetime.now()
            yesterday_time = yesterday.strftime("%Y%m%d")
            noOfPhotosPerTime = 1
            PreviousPhotoIdentifier = 1
        print(totalNoOfPhotos, noOfPhotosPerTime)
        if totalNoOfPhotos > 6:
            filename=current_time + "2"
        else:
            filename = current_time + "1"
    except:
        print("frame8 No photos")
 # change the value of progress bar in Scheduling screen,Here use the count of Photos per Mission to progress the Progress Bar

    if x >= 79:
        y5 = "完了"
        c5 = "red"
        x=-1
        x1=0
        x2=0
        x3=0
        x4=0
        x5=0
    elif x >= 67:
        y4 = "完了"
        c4 = "red"
        x5 += 1
        y5 = "進行中"
        c5 = "white"
    elif x >= 55:
        y3 = "完了"
        c3 = "red"
        x4 += 1
        y4 = "進行中"
        c4 = "white"
    elif x >= 39:
        y2 = "完了"
        c2 = "red"
        x3 += 1
        y3 = "進行中"
        c3 = "white"

    elif x >=27:
        y1 = "完了"
        c1 = "red"
        x2 += 1
        y2 = "進行中"
        c2 = "white"
    elif x >=15:
        x1 += 1
        y = "完了"
        c = "red"
        y1 = "進行中"
        c1 = "white"
    elif x >= 0:
        y = "進行中"
        c = "white"
        y1 = "＿＿"
        c1 = "white"
        y2 = "＿＿"
        c2 = "white"
        y3 = "＿＿"
        c3 = "white"
        y4 = "＿＿"
        c4 = "white"
        y5 = "＿＿"
        c5 = "white"



    x+=1

    root.after(1000, update_info)

if __name__ == '__main__':
    noOfPhotosPerTime = 1
    f = []
    filename = ""
    root = Tk()
    # GUI TITLE
    root.title("Ipc Spot Inspection")
    # root.geometry("%dx%d" % (root.winfo_width(), root.winfo_height()))
    # Set the frame height and width
    # Both the frameHeight and frameWidth should be resized based on the size of the window
    # Each frame is set to a specific height and width, therefore by resizing it's attempting to remain in that size
    frameHeight = (root.winfo_height() - 50) / 3
    frameWidth = (root.winfo_width() - 50) / 3.25
    frame = Frame(root, bg="black")
    frame.place(height=frameHeight, width=frameWidth, relx=0.01, rely=0.01)

    # frame.grid(row=0, column=0, sticky='nesw')
    frame2 = Frame(root, bg="#EEEEEE")
    # frame2.grid(row=0, column=1, sticky='nesw')
    frame2.place(height=frameHeight, width=frameWidth, relx=0.34, rely=0.01)
    frame3 = Frame(root, bg="#EEEEEE")
    # frame3.grid(row=0, column=2, sticky='nesw')
    frame3.place(height=frameHeight, width=frameWidth, relx=0.67, rely=0.01)
    'Here using webpage libraries for call webrtc url to retrieve '

    web3 =HtmlFrame(frame3, 500, 500)
    # try with tkwebviewFrame
    "This is URL to call live camera feed"
    web3.load_website('http://192.168.10.24:31102/h264.sdp.html')
    web3.pack(fill="both", expand=True)

    frame4 = Frame(root, bg="black")
    # frame4.grid(row=1, column=0, sticky='nesw')
    frame4.place(height=frameHeight, width=frameWidth, relx=0.01, rely=0.33)
    frame5 = Frame(root, bg="#EEEEEE")
    # frame5.grid(row=1, column=1, sticky='nesw')
    frame5.place(height=frameHeight, width=frameWidth, relx=0.34, rely=0.33)
    web5 = HtmlFrame(frame5)
    # try with tkwebviewFrame
    web5.load_website('http://tkhtml.tcl.tk/tkhtml.html')
    web5.pack()
    frame6 = Frame(root, bg="#EEEEEE")
    # frame6.grid(row=1, column=2, sticky='nesw')
    frame6.place(height=frameHeight, width=frameWidth, relx=0.67, rely=0.33)
    web6 = HtmlFrame(frame6, 500, 500)
    # try with tkwebviewFrame
    web6.load_url("https://www.compadre.org/osp/pwa/soundanalyzer/")
    web6.pack(fill="both", expand=True)
    frame7 = Frame(root, bg="#EEEEEE")
    # frame7.grid(row=2, column=0, sticky='nesw')
    frame7.place(height=frameHeight, width=frameWidth, relx=0.01, rely=0.65)
    frame8 = Frame(root, bg="#EEEEEE")
    # frame8.grid(row=2, column=1, sticky='nesw')
    frame8.place(height=frameHeight, width=frameWidth, relx=0.34, rely=0.65)
    frame9 = Frame(root, bg="#EEEEEE")
    # frame9.grid(row=2, column=2, sticky='nesw')
    frame9.place(height=frameHeight, width=frameWidth, relx=0.67, rely=0.65)
    # schedule...
    scheduleLabel = Label(frame4, text="Spot -スケジュール", bg="black", fg="white", )
    scheduleLabel.place(height=30, width=120, relx=0.01, rely=0.01)
    live = datetime.now()
    # This command is used for run live timing
    livetiming = live.strftime("%Y{0}%m{1}%d{2}　　%H{3}%M{４}").format(*'年月日時分')
    timeLabel = Label(frame4, text=livetiming, bg="black", fg="white")
    timeLabel.place(height=30, width=220, relx=0.6, rely=0.01)
    totalNoOfPhotos = 1
    m = 1
    PreviousPhotoIdentifier = 6
    previous = datetime.today() - timedelta(minutes=2)
    previous_time = previous.strftime("%H-%M")
    # This command is used to display the image in frame 7
    try:
        Frame7img = Image.open('/Users/AW1/OneDrive - 山口電気工事株式会社　＊/デスクトップ' + previous_time + ".png")
        resize = Frame7img.resize((400, 250))
        Frame7Image = ImageTk.PhotoImage(resize)
        Frame7imglabel = Label(frame7, image=Frame7Image)
        # mylabel.grid(row=0, column=0, columnspan=3)
        Frame7imglabel.place(height=frameHeight - 20, width=frameWidth - 10, relx=0.01, rely=0)
    except:
        print("error")
    # Backward button
    buttonback = Button(frame7, text="前へ", fg="white", bg="black", command=back)
    # buttonback.grid(row=1, column=0)
    buttonback.place(relheight=0.10, relwidth=0.10, relx=0.23, rely=0.92)
    # Open folder button
    openFolderButton = Button(frame7, text="前回", fg="white", bg="black", command=open_win)
    # buttonExit.grid(row=1, column=1)
    openFolderButton.place(relheight=0.10, relwidth=0.10, relx=0.46, rely=0.92)
    buttonForward = Button(frame7, text="次へ", fg="white", bg="black", command=front)
    # buttonForward.grid(row=1, column=2)
    buttonForward.place(relheight=0.10, relwidth=0.10, relx=0.69, rely=0.92)
    # File name button
    NameOfPhotosName = Label(frame7, text="202204151", bg="black", fg="white")
    NameOfPhotosName.place(height=30, width=100, relx=0.01, rely=0.92)
    # This is used to identify the Filename for respective screen ↓↓↓

    now = datetime.now()
    current_time = now.strftime("%Y%m%d")
    filename = current_time + "1"
    yesterday = datetime.today() - timedelta(days=1)
    yesterday_time = yesterday.strftime("%Y%m%d")

    '''try:
        img_now = Image.open('/Users/denkiyamakuchi/Desktop/Images/' + "13-04" + ".png")
        resize_now = img_now.resize((400, 300))
        myImage_now = ImageTk.PhotoImage(resize_now)
        mylabel_now = Label(frame8,image=myImage_now)
        mylabel_now.place(height=frameHeight-20, width=frameWidth-10, relx=0.01, rely=0)
    except:
        print("error")'''
    # These variable are used to make change in schedule display screen
    x = 0
    x1 = 0
    x2 = 0
    y = "進行中"
    c = "white"
    y1 = "進行中"
    c1 = "white"
    y2 = "進行中"
    c2 = "white"
    x3 = 0
    y3 = "進行中"
    c3 = "white"
    x4 = 0
    y4 = "進行中"
    c4 = "white"
    x5 = 0
    y5 = "進行中"
    c5 = "white"
    update_info()
    # update_yes()
    app = FullScreenApp(root)
    rect = [0, 0, frameWidth, frameHeight]
    #Call URL
    frame5Url = 'https://www.youtube.com/watch?v=_uQrJ0TkZlc'
    frame6Url = 'https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV'
    frame3Url = 'https://192.168.10.166/'
    # thread = threading.Thread(target=webBrowser)
    # thread1 = threading.Thread(target=embed_browser_thread1, args=(frame6, rect, frame6Url))
    # thread2 = threading.Thread(target=embed_browser_thread2, args=(frame3, rect, frame3Url))

    # thread.start()
    def update_frames():
        newframewidth = (root.winfo_width() - 50) / 3
        newframeheight = (root.winfo_height() - 50) / 3.25

        frame.place(width=newframewidth, height=newframeheight)
        frame2.place(width=newframewidth, height=newframeheight)
        frame3.place(width=newframewidth, height=newframeheight)
        frame4.place(width=newframewidth, height=newframeheight)
        frame5.place(width=newframewidth, height=newframeheight)
        frame6.place(width=newframewidth, height=newframeheight)
        frame7.place(width=newframewidth, height=newframeheight)
        frame8.place(width=newframewidth, height=newframeheight)
        frame9.place(width=newframewidth, height=newframeheight)
        root.after(1, update_frames)

    root.after(1, update_frames)
    root.mainloop()