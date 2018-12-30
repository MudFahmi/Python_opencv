from tkinter import *
import tkinter.messagebox as messagebox
import threading
import pyaudio
import wave
import numpy as np
import cv2


CHUNK = 1024
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 2
RATE = 44100 #sample rate
RECORD_SECONDS = 5


WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

print("* recording")
frames = []


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640,480))
pause=False
stop=False


while(not(stop)):
    ret, frame = cap.read()
    if ret==True:

        if (not (pause)):
            out.write(frame)
            cv2.imshow('frame', frame)

            for i in range(0,3):
                data = stream.read(CHUNK)
                frames.append(data)  # 2 bytes(16 bits) per channel

        key=cv2.waitKey(1)
        if(key==112):
            pause=True
        elif(key==99):
            pause=False
        elif(key==115):
            stop=True
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

