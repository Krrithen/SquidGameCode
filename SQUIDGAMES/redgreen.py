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

root = tkinter.Tk()
root.title("RED LIGHT GREEN LIGHT")
root.geometry('1280x720+288+88')

cnvs = Canvas(root,height=60,width=50) 
cnvs.pack()

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("30")
second.set("00")

hourEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=hour)
hourEntry.place(x=80,y=20)
minuteEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=minute)
minuteEntry.place(x=130,y=20)
secondEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=second)
secondEntry.place(x=180,y=20)

img1=ImageTk.PhotoImage(Image.open("css.png"))
img2=ImageTk.PhotoImage(Image.open("csi.png"))
rg =[0,1]
t = [6000,3000,4000,5000]#6000,7000,8000,9000

l = tkinter.Label(root,font="bold")
l.pack()


wave_object1 = sa.WaveObject.from_wave_file('green.wav')
wave_object2 = sa.WaveObject.from_wave_file('red.wav')



def chngs():
       
    x = random.choice(rg)
    if x==0:
        l.config(image=img1)
        wave_object2.play()
        print("red")
    elif x==1:
        l.config(image=img2)
        wave_object1.play()
        print("green")
    root.after(random.choice(t),chngs)
    
    
def submit():    
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")  
    while temp >-1:
        mins,secs = divmod(temp,60) 
        hours=0   
        if mins >60:
            hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
        temp -= 1

#btn = Button(root, text='Set Time Countdown', bd='5',command= submit)
#btn.place(x = 70,y = 120)



intro = AudioSegment.from_mp3('intro.mp3')
play(intro)
chngs()
submit()

root.mainloop()