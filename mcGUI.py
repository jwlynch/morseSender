from morse import MorsePlayer
from tkinter import *
import os
# os.system('clear')

mp = MorsePlayer()

root = Tk()
root.title('mcSoundOutput')
root.geometry('600x400')

mcLabel = Label(root, text="Enter text to xmit in caps 50 chars max:")
mcLabel.pack()

mcTextbox = Entry(root, width=50)
mcTextbox.pack()

def play_textbox():
    text = mcTextbox.get()
    text = text.upper()
    mp.play_string(text)

mcButton = Button(root, text='Submit', command=play_textbox)
mcButton.pack()

root.mainloop()




