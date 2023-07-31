import tkinter
from tkinter import *

names = ["Emerald", "Mila", "Ricky"]

def set_text(label, text):
    label.delete(0, END)
    label.insert(0, text)
    return

# setup size of window
window = Tk()
window.title("Auto Name Selector")
window.geometry("600x600")

# setup Labels
# video = Label(window, 
#                  text="Video").place(x = 10,
#                                              y = 25)
# audio = Label(window, 
#                  text='Audio').place(x = 10,
#                                              y = 50)
# av_Accomodador = Label(window, 
#                           text='AV Acomodador').place(x = 10,
#                                                       y = 75)
# mic1 = tk.Label(window, text='Mic 1').
# mic2 = tk.Label(window, text='Mic 2').
# plat = tk.Label(window, text='Platform')
# door = tk.Label(window, text='Puerta')
# acco1 = tk.Label(window, text='Acomodador A')
# acco2 = tk.Label(window, text='Acomodador B')

# Setup Fields
# video_field = Entry(window,
#                        width=20).place(x = 200,
#                                        y = 25)
# audio_field = Entry(window,
#                        width=20).place(x = 200,
#                                        y = 50)
# avAcco = Entry(window,
#                        width=20).place(x = 200,
#                                        y = 75)
v = Entry(window, width=30).place(x=10,y=20)

# Create Button for random (delete and insert only work when you pack())
video_Button = Button(window,
                         text="Randomize", width=6, command=lambda:set_text("Sergio Ruiz")).place(x = 400,
                                                 y = 75)


# Calls the window object
window.mainloop()