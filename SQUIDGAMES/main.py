import tkinter
import random
import time
from PIL import Image
from PIL import ImageTk
from pydub import AudioSegment
from pydub.playback import play

root = tkinter.Tk()
root.title("RED LIGHT GREEN LIGHT")
root.geometry('1280x720+288+88')

img1=ImageTk.PhotoImage(Image.open("css.png"))
img2=ImageTk.PhotoImage(Image.open("csi.png"))
rg =[0,1]
t = [2000,3000,4000,5000]#6000,7000,8000,9000

l = tkinter.Label(root,font="bold")
l.pack()


def chngs():
    green = AudioSegment.from_mp3('green.mp3')
    red = AudioSegment.from_mp3('red.mp3')
    x = random.choice(rg)
    if x==0:
        l.config(image=img1)
        play(red)
        print("red")
    elif x==1:
        l.config(image=img2)
        play(green)
        print("green")
    ms = random.choice(t)
    print(ms)
    root.after(ms,chngs)
    


chngs()

root.mainloop()