from morse import MorsePlayer
from tkinter import *
import os
# os.system('clear')

mp = MorsePlayer()

root = Tk()
root.title('mcSoundOutput')
root.geometry('600x400')

mcLabel = Label(root, text="Enter word to BackInto")
mcLabel.pack()

mcTextbox = Entry(root, width=50)
mcTextbox.pack()

def play_textbox():
    s = mcTextbox.get()
    l = len(s)
    a = ""
    for b in range (l+1):
        a = a + (s[l-b:] + " ") * 5
    
    mp.play_string(a)

mcButton = Button(root, text='Submit', command=play_textbox)
mcButton.pack()

root.mainloop()




