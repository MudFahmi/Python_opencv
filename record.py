from tkinter import *
import tkinter.messagebox as messagebox
import threading
import cv2
import pyaudio
import wave

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

        global format_type
        global freq_num
        global name
        global fullname

        format_type = formats.get()

        name = nam.get()
        fullname = name + "." + format_type


        try:
            freq_num = float(freq.get())
        except:
            messagebox.showerror(title="error type", message="enter frequency in float or integer")
            return

        if (name != '' and format_type != '' and freq_num != ''):

          mess=messagebox.askyesno(title="Confirmation", message="Name:   " + fullname + "\nFrequncy: " + str(freq_num))

          if mess==1:

              record = Tk()
              record.title("Control Panel")
              record.geometry("637x90+320+638")


              global fpause
              global fstop

              fpause = False
              fstop = False


              def startVideo():

                      global fstop
                      global fpause
                      global fullname
                      global freq_num
                      global name

                      CHUNK = 1024
                      FORMAT = pyaudio.paInt16  # paInt8
                      CHANNELS = 2
                      RATE = 44100  # sample rate
                      #RECORD_SECONDS = 5

                      WAVE_OUTPUT_FILENAME = name+".wav"

                      p = pyaudio.PyAudio()

                      stream = p.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      input=True,
                                      frames_per_buffer=CHUNK)  # buffer

                      frames = []

                      cap = cv2.VideoCapture(0)
                      fourcc = cv2.VideoWriter_fourcc(*'XVID')
                      out = cv2.VideoWriter(fullname , fourcc,freq_num, (640, 480))

                      while True:

                         ret, frame = cap.read()
                         cv2.imshow('frame', frame)
                         out.write(frame)
                         key = cv2.waitKey(1)

                         for i in range(0, 3):
                             data = stream.read(CHUNK)
                             frames.append(data)  # 2 bytes(16 bits) per channel

                         if fstop:
                              fstop = False
                              break
                         if fpause:
                              while fpause:
                                  pass

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

                      #os.system('ffmpeg -i "D:\FCI-H\First Term\Multimedia\Project\"'+fullname+' -i "D:\FCI-H\First Term\Multimedia\Project\"'+WAVE_OUTPUT_FILENAME+ ' -vcodec copy -acodec copy '+fullname)


              def start():
                  threading._start_new_thread(startVideo, ())

              button1 = Button(record, text="Start Video", width=12, fg='black', activebackground='red', bg='gray', font=15 ,command=start)
              button1.place(x='50',y='20')

              def pauseVideo():

                  global fpause

                  if fpause == False:
                      fpause = True

              button2 = Button(record, text="Pause Video", width=12, fg='black', activebackground='red', bg='gray', font=15 ,command=pauseVideo)
              button2.place(x='180',y='20')

              def resumeVideo():

                  global fpause
                  if fpause:
                      fpause = False

              button2 = Button(record, text="Resume Video", width=12, fg='black', activebackground='red', bg='gray', font=15, command=resumeVideo)
              button2.place(x='310',y='20')

              def stopVideo():

                  global fstop
                  fstop = True

              button3 = Button(record, text="Stop Video", width=12, fg='black', activebackground='red', bg='gray', font=15, command=stopVideo)
              button3.place(x='440',y='20')


              record.mainloop()

        else:
           messagebox.showerror(title="Erorr", message="plz complete info")


button_one = Button(text="confirm", width=12, fg='black', activebackground='red', bg='gray', font=15,
                    command=getselected).place(x='210', y='260')


prerecord.mainloop()
