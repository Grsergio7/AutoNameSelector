import tkinter
from tkinter import *

# Create an instance of tkinter frame
win = Tk()

# Define geometry of the window
win.geometry("700x250")

# Functions
def set_text(field, text):
   field.delete(0,END)
   field.insert(0, text)

# setup Labels
video_label = Label(win, text="Video")
audio_label = Label(win, text="Audio")
av_label = Label(win, text="AV Accomodador")

# Setup Fields
video_field = Entry(win, bg="white", width=20, borderwidth=2)
audio_field = Entry(win, bg="white", width=20, borderwidth=2)
av_field = Entry(win, bg="white", width=20, borderwidth=2)

# Place in window using grid
video_label.grid(row=0)
audio_label.grid(row=0,column=2)
av_label.grid(row=0,column=3)

video_field.grid(row=1)
audio_field.grid(row=1,column=2)
av_field.grid(row=1,column=3)

# Create Button for random 
av_button = Button(win, text="Choose", command=lambda:set_text(video_field ,"name")).grid(row=1,column=4)

# Calls the window object
win.mainloop()
