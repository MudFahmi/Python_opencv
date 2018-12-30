from tkinter import *
import tkinter.messagebox as messagebox
import threading
import cv2

prerecord = Tk()
prerecord.title("  Recording  ")

prerecord.geometry("540x300+400+50")

Label(prerecord, text="VIDEO RECORDING APP", bg="red", fg="black", font=300).pack(side="top", fill="x")

formats = StringVar()
formats.set('mp4')
Label(prerecord, text="Choose a video format", padx=25, justify='left', font=130).pack(anchor='w')
Radiobutton(prerecord, text='mp4', padx=30, variable=formats, value='mp4').pack(anchor=W)
Radiobutton(prerecord, text='avi', padx=30, variable=formats, value='avi').pack(anchor=W)
Radiobutton(prerecord, text='3gp', padx=30, variable=formats, value='3gp').pack(anchor=W)
Radiobutton(prerecord, text='flv', padx=30, variable=formats, value='flv').pack(anchor=W)

Label(prerecord,text="Enter a video frequncy",padx=100,font=130).place(x='220',y='25')
freq=StringVar()
text=Entry(textvariable=freq).place(x='320',y='80')

Label(prerecord, text="Enter video name :", padx=30, pady=20, font=30).pack(anchor='w')
nam = StringVar()

text = Entry(textvariable=nam).place(x='180', y='170')

voic = IntVar()
Checkbutton(prerecord, text="voice record", font=30, variable=voic).place(x='330', y='170')


def getselected():
    try:
        global format_type
        global freq_num
        global name
        global fullname

        format_type = formats.get()
        freq_num = float(freq.get())
        name = nam.get()
        fullname = name + "." + format_type

    except:
       messagebox.showerror(title="error type",messagebox="enter frequency in float or integer")

    if (name != '' and format_type != '' and freq_num != ''):



          mess=messagebox.askyesno(title="Confirmation", message="Name:   " + fullname + "\nFrequncy: " + str(freq_num))

          if mess==1:

              record = Tk()

             # fstart = False

              global fpause
              global fstop

              fpause = False
              fstop = False

              # ntext = eText.get()

              def startVideo():

                      global fstop
                      global fpause
                      global fullname
                      global freq_num

                      cap = cv2.VideoCapture(0)
                      fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                      out = cv2.VideoWriter(fullname , fourcc,freq_num, (640, 480))
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

              def start():
                  threading._start_new_thread(startVideo, ())

              button1 = Button(record, text="Take Video", command=start)
              button1.pack()

              def pauseVideo():

                  global fpause
                  if fpause == False:
                      fpause = True

              button2 = Button(record, text="Pause Video", command=pauseVideo)
              button2.pack()

              def resumeVideo():

                  global fpause
                  if fpause:
                      fpause = False

              button2 = Button(record, text="resume Video", command=resumeVideo)
              button2.pack()

              def stopVideo():
                  # print("stop");
                  # cv2.imshow('frame', frame)
                  global fstop
                  fstop = True

              button3 = Button(record, text="Stop Video", command=stopVideo)
              button3.pack();

              record.mainloop()

    else:
        messagebox.showinfo(title="Erorr", message="plz complete info")


button_one = Button(text="confirm", width=10, fg='black', activebackground='red', bg='gray', font=15,
                    command=getselected).place(x='310', y='260')


#def back():
 #   record.destroy()
  #  import interfaceone


#button_one = Button(text="back", width=10, fg='black', activebackground='red', bg='gray', font=15, command=back).place(x='110', y='260')

prerecord.mainloop()
