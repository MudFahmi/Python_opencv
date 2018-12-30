from tkinter import *
import tkinter.messagebox as messagebox
import cv2
import threading
import time
import numpy as np
from bokeh.models.glyphs import Text
import sys
import re

root = Tk()
eText = StringVar()
fstart = False
fpause = False
fstop = False
#ntext = eText.get()


def fun():

    try:
        ntext = float(eText.get())
        nlabel2 = Label(root, text=ntext).pack()
        return
    except:
        print("Please type in a number!")

mlabel = Label(root,text="Please Enter The Frequancy").pack()
mentry = Entry(root, textvariable=eText).pack()
mbutton = Button(root, text="Ok", command=fun, fg='red', bg='blue').pack()


def startVideo():

  if float(eText.get() != ""):

    global fstop
    global fpause
    # global ntext
    # float(ntext)
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('123t.avi',fourcc, float(eText.get()), (640, 480))
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        out.write(frame)
        key = cv2.waitKey(1);
        if fstop:
            fstop = False
            break
        if fpause:
            while fpause:
                pass

    cap.release()
    out.release()
    cv2.destroyAllWindows()
  else:
    messagebox.showerror(title="error",message="  enter frequancy value ")


def start():
    threading._start_new_thread(startVideo, ())

button1 = Button(root, text="Take Video", command=start)
button1.pack()




def pauseVideo():

    global fpause
    if fpause == False:
        fpause = True



button2 = Button(root, text="Pause Video", command=pauseVideo)
button2.pack()

def resumeVideo():

    global fpause
    if fpause:
        fpause = False


button2 = Button(root, text="resume Video", command=resumeVideo)
button2.pack()


def stopVideo():
    # print("stop");
    # cv2.imshow('frame', frame)
    global fstop
    fstop = True


button3 = Button(root, text="Stop Video", command=stopVideo)
button3.pack();

root.mainloop()
