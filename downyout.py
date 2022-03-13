#pip install tkinter
#pip install pytube3

from pytube import YouTube
from tkinter import *
from tkinter import messagebox as mb
# Creating the main window
wn = Tk()
wn.title("Python Youtube Downloader by ProjectGurukul")
wn.geometry('700x300')
wn.config(bg='honeydew2')
res = StringVar()
# Heading label
Label(wn, text="Youtube Video Downloader by ProjectGurukul", font=('Courier', 15), fg='grey19').place(x=100,y=15)
#Getting youtube link
Label(wn, text='Enter the Youtube link:', font=("Courier", 13)).place(relx=0.05, rely=0.3)
yt_link = StringVar(wn)
link_entry = Entry(wn, width=50, textvariable=yt_link)
link_entry.place(relx=0.5, rely=0.3)
#Getting destination location
Label(wn, text='Enter the save location:', font=("Courier", 13)).place(relx=0.05, rely=0.5)
destination = StringVar(wn)
dir_entry = Entry(wn, width=50, textvariable=destination)
dir_entry.place(relx=0.5, rely=0.5)
#Buttons
resolutionBtn = Button(wn, text='Find Resolution', font=7, fg='grey19',
command=getResolution).place(relx=0.3, rely=0.75)
resetBtn= Button(wn, text='Reset', font=7, fg='grey19',
command=reset).place(relx=0.6, rely=0.75)
wn.mainloop()

def getResolution():
url= yt_link.get() #getting link from the user
resolutions = set() #set that holds the resolutions available
try:
yt = YouTube(url) #creating the object that stores information about the video
for stream in yt.streams.filter(type="video"): # Only look for video streams
resolutions.add(stream.resolution) #Adding all resolutions available
resolutions=list(resolutions) #list containing all resolutions
except Exception as e:
mb.showerror('Error',e)
return
#creating a new window
wn = Tk()
wn.title("Youtube Video Downloader by ProjectGurukul")
wn.geometry('700x500')
wn.config(bg='honeydew2')
# Heading label
Label(wn, text="Youtube Video Downloader by ProjectGurukul", font=('Courier', 15), fg='grey19').place(x=100,y=15)
Label(wn, text="The available resolutions are checkable. \n Please choose one of the resolutions and click on the download button",
font=('Courier', 10), fg='grey19').place(x=20,y=50)
#Creating a radio button for each resolution
R1 = Radiobutton(wn, text='144p', variable=res, value='144p')
R1.place(x=100,y=100)
R1.deselect()
R2=Radiobutton(wn, text='240p', variable=res, value='240p')
R2.place(x=100,y=130)
R2.deselect()
R3=Radiobutton(wn, text='360p', variable=res, value='360p')
R3.place(x=100,y=160)
R3.deselect()
R4=Radiobutton(wn, text='480p', variable=res, value='480p')
R4.place(x=100,y=190)
R4.deselect()
R5=Radiobutton(wn, text='720p', variable=res, value='720p')
R5.place(x=100,y=220)
R5.deselect()
R6=Radiobutton(wn, text='1080p', variable=res, value='1080p')
R6.place(x=100,y=250)
R6.deselect()
R7=Radiobutton(wn, text='2016p', variable=res, value='2016p')
R7.place(x=100,y=280)
R7.deselect()
#disabling those radio buttons that are not available in the video
if('144p' not in resolutions):
R1.config(state = DISABLED)
elif('240p' not in resolutions):
R2.config(state = DISABLED)
elif('360p' not in resolutions):
R3.config(state = DISABLED)
elif('480p' not in resolutions):
R4.config(state = DISABLED)
elif('720p' not in resolutions):
R5.config(state = DISABLED)
elif('1080p' not in resolutions):
R6.config(state = DISABLED)
elif('2016p' not in resolutions):
R7.config(state = DISABLED)
downloadBtn = Button(wn, text='Download', font=7, fg='grey19',
command=downloadVideo).place(x=100,y=350)
quitBtn = Button(wn, text='Quit', font=7, fg='grey19',
command=wn.destroy).place(x=350,y=350)

def reset():
yt_link.set('')
destination.set('')

def downloadVideo():
resol=res.get() #getting resolution based on the radio button selected
path = destination.get() #getting the location where the video needs to be downloaded
try: #downloading the video of selected resolution
ys=yt.streams.filter(resolution=resol)
ys.first().download(path)
except Exception as e:
mb.showerror('Error',e)

