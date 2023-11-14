import tkinter as tk 
from tkinter import *
# returns a list of names at random 0 - 5. Can Also exlude names from appearing
import __init__ as main

# Create an instance of tkinter frame
win = tk.Tk()

# Define geometry of the window
win.geometry("400x300")
win.title("Auto Name Selector")
win.resizable(0, 0)

# configure the grid
win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=3)

# setup Labels
# Video
video_label = Label(win, text="Video")
video_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

video_field = Entry(win)
video_field.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# Audio
audio_label = Label(win, text="Audio")
audio_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

audio_field = Entry(win)
audio_field.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# A/V Label
av_label = Label(win, text="A/V")
av_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

av_field = Entry(win)
av_field.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

# Plataforma Label
plat_label = Label(win, text="Plataforma")
plat_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

plat_field = Entry(win)
plat_field.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

# Mic1 Label
mic1_label = Label(win, text="Mic 1")
mic1_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

mic1_field = Entry(win)
mic1_field.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

# Mic2 Label
mic2_label = Label(win, text="Mic 2")
mic2_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

mic2_field = Entry(win)
mic2_field.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

# Exclude Label
ex_label = Label(win, text="Exclude")
ex_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)

ex_field = Entry(win)
ex_field.grid(column=1, row=6, rowspan=2,sticky=tk.E, padx=5, pady=5)


def get_data():
   li = list((ex_field.get()).split(","))
   return li
   


# Button setup
# Adding "lambda" keeps button from executing the function inside
select_button = Button(win, text="Select", command=lambda : create_field(1,"",get_data()))
select_button.grid(column=2, row=6, sticky=tk.E, padx=5, pady=5)


# Function to play in window
def create_field(w,d,x_names):
   name_list = main.assign_week(w,d,x_names)

   video_field.delete(0, tk.END)
   video_field.insert(0,name_list[0])

   audio_field.delete(0, tk.END)
   audio_field.insert(0,name_list[1])

   av_field.delete(0, tk.END)
   av_field.insert(0,name_list[2])

   plat_field.delete(0, tk.END)
   plat_field.insert(0,name_list[3])

   mic1_field.delete(0, tk.END)
   mic1_field.insert(0,name_list[4])

   mic2_field.delete(0, tk.END)
   mic2_field.insert(0,name_list[5])


# Calls the window object
win.mainloop()
