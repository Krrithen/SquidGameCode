#imported modules: tkinter for messagebox and widget, time, random
#PIL for image operations, pydub and simpleaudio for audio operations
import tkinter
from tkinter import *
from tkinter import messagebox
import time
import random
from PIL import Image
from PIL import ImageTk
from pydub import AudioSegment
from pydub.playback import play
import simpleaudio as sa
#giving title and dimensions for the output window
root=tkinter.Tk()
root.attributes('-fullscreen',True)
root.title("RED LIGHT GREEN LIGHT")
root.geometry('1280x720+288+88')
root.configure(bg="black")
#canvas for timer
cnvsColor="black"
cnvs=Canvas(root,bg=cnvsColor,height=100,width=1600,bd=0) #
cnvs.pack()
#timer variables
hour=StringVar()
minute=StringVar()
second=StringVar()
#initiated to 30 minutes
hour.set("00")
minute.set("30")
second.set("00")
#font and position for timer
hourEntry=Entry(root,width=3,font=("Helvetica",40,""),textvariable=hour)
hourEntry.configure({"background":"Grey","foreground":"Red"})
hourEntry.place(x=690,y=20)
minuteEntry=Entry(root,width=3,font=("Helvetica",40,""),textvariable=minute)
minuteEntry.configure({"background":"Grey","foreground":"Red"})
minuteEntry.place(x=790,y=20)
secondEntry=Entry(root,width=3,font=("Helvetica",40,""),textvariable=second)
secondEntry.configure({"background":"Grey","foreground":"Red"})
secondEntry.place(x=890,y=20)
#display images
img1=ImageTk.PhotoImage(Image.open("rr.png"))
img2=ImageTk.PhotoImage(Image.open("gg.png"))
rg =[0,1]
t=[9000,10000,12000,7000]#time intervals
tr=[5000,6000,8000,7000]#time intervals for red
#label font
l=tkinter.Label(root,font="bold")
l.pack()
#play audio
wave_object1=sa.WaveObject.from_wave_file('green.wav')
wave_object2=sa.WaveObject.from_wave_file('red.wav')
#function for image and audio transition
def chngs():   
    x=random.choice(rg)
    if x==0:
        l.config(image=img1)
        wave_object2.play()
        print("red")
        root.after(random.choice(tr),chngs)
    elif x==1:
        l.config(image=img2)
        wave_object1.play()
        print("green")
        root.after(random.choice(t),chngs)
#function for timer       
def submit():    
    try:
        temp=int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")  
    while temp>-1:
        mins,secs=divmod(temp,60) 
        hours=0   
        if mins>60:
            hours, mins=divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if (temp==0):
            messagebox.showinfo("Time Countdown", "Time's up ")
            time.sleep(2)
            root.destroy()
        temp-=1
#play intro
intro=AudioSegment.from_mp3('intro1.mp3')
intro1=AudioSegment.from_mp3('intro2.mpeg')
play(intro)
play(intro1)
chngs()
submit()
#loop window for constant ouput
root.mainloop()