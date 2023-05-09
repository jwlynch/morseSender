from morse import MorsePlayer
from tkinter import *
from random import shuffle
import os
# os.system('clear')

mp = MorsePlayer()

root = Tk()
root.title('mcSoundOutput')
root.geometry('600x400')

mcLabel = Label(root, text="Enter string to shuffle")
mcLabel.pack()

mcTextbox = Entry(root, width=50)
mcTextbox.pack()

def play_textbox():
    s = mcTextbox.get()
    k = list(s)
    shuffle(k)
    a = ''.join(k)    
    mp.play_string(a)

mcButton = Button(root, text='Submit', command=play_textbox)
mcButton.pack()

root.mainloop()




