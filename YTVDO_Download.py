# import modules

from tkinter import *
import tkinter as tk
import yt_dlp

# splash screen

splash = Tk()
splash.title ('YT Video Downloader')
splash.geometry ('400x400')
splash.resizable (0,0)
splash.configure (background = 'red')
spl_lab = Label (splash, text = 'GodARD Devos \n YT Video Download', bg = 'yellow', fg = 'blue', font = ('vendana', 20, 'bold'))
spl_lab.pack (pady = 150)

# main window YT

def main_window_YT():
    splash.destroy()
    yt = tk.Tk()
    yt.geometry ('500x500')
    yt.title ("GOD DOWNLOADS")
    yt.configure (background = 'gray')
    yt.resizable (0,0)
    yt.minsize (width = 500, height = 500)
    
    # Clear 
    
    def clear():
        urll.delete(0,END)
        show.destroy()
    
    # Video Downloader 
    
    def download():
        global show
        url = urll.get()
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        # label
        show = Label(yt, text = "Video Downloaded", bg = 'blue', fg = 'white', font = ('vendana',15,'bold'))
        show.place(x = 160, y = 230)
    
    # URL
    
    urll = Entry (yt, width = 25, bg = '#7FFFD4', fg = 'red', borderwidth = 2,
    font = ('vendana', 20,'italic'))
    urll.insert (0,"Enter URL here ... ")
    urll.place(x= 60, y = 100)
    
    # label
    
    ins = Label(yt, text = "It downloads the video in the folder in which \nyou are running the current code file", bg = 'blue', fg = 'white', font = ('vendana',15,'bold'))
    ins.place(x = 30, y = 20)
    
    last = Label(yt, text = "After clicking download give JUST CHILL and wait\ntill 'Video Downloaded' Pops Up", bg = 'springgreen', fg = 'black', font = ('vendana',15,'bold'))
    last.place(x = 10, y = 400)

    # Button
    
    down = Button (yt, width = 10, height = 1, text = "Download", bg = 'red', fg = 'white', command = download, font = ('vendana',10,'bold'))
    down.place(x = 140, y = 170)
    
    clearr = Button (yt, width = 10, height = 1, text = "clear", bg = 'brown', fg = 'white', command = clear, font = ('vendana',10,'bold'))
    clearr.place(x = 270, y = 170)

# splash disappear

splash.after ( 2500, main_window_YT)

# run app

mainloop()