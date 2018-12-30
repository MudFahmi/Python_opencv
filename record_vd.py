from tkinter import *
import tkinter.messagebox as messagebox
import threading


import numpy as np
import cv2

record = Tk()

record.title("  Recording now  ")

record.geometry("540x300+400+50")

Label(record, text="VIDEO RECORDING ", bg="red", fg="black", font=300).pack(side="top", fill="x")


cap = cv2.VideoCapture(0)

name=" "
freq_num = 0
format=" "

fullname = name+"."+ format

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
dspause=False
stop=False

while(not(stop)):
    ret, frame = cap.read()
    if ret==True:

        if (not (pause)):
            out.write(frame)

            cv2.imshow('frame',frame)
        key=cv2.waitKey(5)
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

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


def startrecording():
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
        else:
            break


def pauserecording():
    while (cap.isOpened()):
        ret, frame = cap.read()


def stoprecording():
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    panel.quit()
    panel.destroy()


panel = Tk()
panel.title("Control Panel")

panel.geometry("540x300+400+50")

Label(panel, text="VIDEO RECORDING APP", bg="red", fg="black", font=300).pack(side="top", fill="x")

Button(panel, text="puase", width=10, fg='black', activebackground='red', bg='gray', font=15,
       command=pauserecording).place(x='210', y='260')
res = Button(panel, text="resume", width=10, fg='black', activebackground='red', bg='gray', font=15,
             command=startrecording).place(x='280', y='260')

sto = Button(panel, text="stop", width=10, fg='black', activebackground='red', bg='gray', font=15,
             command=stoprecording).place(x='360', y='260')

panel.mainloop()




# record.destroy()
# import recordnow
