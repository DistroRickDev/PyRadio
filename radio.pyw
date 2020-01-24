import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import time
from tkinter import *

url = ['http://45.79.186.124/proxy/megatoncafe?mp=/stream', 'http://frontend.stream.rawfm.net.au:6060/syd-stream-64k.ogg'] #this will allow to store more radio stations
songPosix = 0
numOfSongs = 0

for x in url:
    numOfSongs= numOfSongs+1

media_player = vlc.MediaPlayer(url[songPosix])
#media_player.play()

root = Tk() #instanciate a Tk object called root
root.title("PyRadio") 
root.iconbitmap(r"E:\Python_Projects\PyRadio + GUI\images\RADIO_1.ico")
root.geometry("640x480")
root.resizable(0,0)
root.configure(background="SteelBlue3")

def playRadio():
    media_player.play()

def stopRadio():
    media_player.stop()

def previousSong():
    media_player.stop()
    if(songPosix == 0):
        songPosix=0
        media_player = vlc.MediaPlayer(url[songPosix])   
        media_player.play()
    else:
        songPosix= songPosix - 1
        media_player = vlc.MediaPlayer(url[songPosix])   
        media_player.play()

def nextSong():
    media_player.stop()
    if(songPosix >= numOfSongs):
        songPosix=numOfSongs
        media_player = vlc.MediaPlayer(url[songPosix])   
        media_player.play()
    else:
        songPosix= songPosix + 1
        media_player = vlc.MediaPlayer(url[songPosix])   
        media_player.play()            

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

playImage = PhotoImage(file = r"E:\Python_Projects\PyRadio + GUI\images\PLAY.png")
stopImage = PhotoImage(file = r"E:\Python_Projects\PyRadio + GUI\images\STOP.png")
addImage = PhotoImage(file = r"E:\Python_Projects\PyRadio + GUI\images\ADD.png")
previousImage = PhotoImage(file = r"E:\Python_Projects\PyRadio + GUI\images\PREVIOUS.png")
nextImage = PhotoImage(file = r"E:\Python_Projects\PyRadio + GUI\images\NEXT.png")

buttonPlay= Button(bottomFrame, image = playImage, border = "0" ,bg="azure2", activebackground = "lightgrey", command=playRadio)
buttonStop= Button(bottomFrame, image = stopImage, border = "0",bg="azure2",  activebackground = "lightgrey", command= stopRadio)
buttonAdd = Button(topFrame, image = addImage, border = "0",bg="azure2", activebackground = "lightgrey")
buttonPrevious = Button(bottomFrame, image = previousImage, border = "0",bg="azure2", activebackground = "lightgrey", command = previousSong)
buttonNext = Button(bottomFrame, image = nextImage, border = "0",bg="azure2", activebackground = "lightgrey", command= nextSong)

buttonPrevious.pack(side=LEFT)
buttonPlay.pack(side=LEFT)
buttonStop.pack(side=LEFT)
buttonAdd.pack(side=RIGHT)
buttonNext.pack(side=RIGHT)

root.mainloop()   
