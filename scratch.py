from tkinter import *
from alarm_clock import start_video
from alarm_audio2 import start_audio2
from alarm_audio2 import stop_audio2

def cmd_go():
    input_time = edit1.get()
    print("Start playing..." + input_time)
    if(selection.get() == 2):
        start_video(input_time)
    elif(selection.get() == 1):
         start_audio2(input_time)

def cmd_stop():
    print("Stop playing")
    stop_audio2()

root = Tk()

selection = IntVar()
strTime = StringVar()
strTime = "new time"

frame1 = Frame(root)
frame1.pack()

label1 = Label(frame1, text="Play AUDIO / VIDEO", width=50)
label1.grid(row=0,column=0,columnspan=2)

label2 = Label(frame1, text="Time")
label2.grid(row=1,column=0, pady=20)

edit1 = Entry(frame1, textvariable=strTime, bd=5)
edit1.grid(row=1,column=1)

rb1 = Radiobutton(frame1, text="AUDIO",variable=selection, value=1)
rb1.grid(row=2,column=0)

rb2 = Radiobutton(frame1, text="VIDEO",variable=selection, value=2)
rb2.grid(row=2,column=1)

button1 = Button(frame1, text="GO",width=10,command=cmd_go)
button1.grid(row=3,column=0, pady=20)

button2 = Button(frame1,text="STOP",width=10,command=cmd_stop)
button2.grid(row=3,column=1)

root.mainloop()