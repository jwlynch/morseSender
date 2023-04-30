from morse import MorsePlayer
from tkinter import *
import os
# os.system('clear')

mp = MorsePlayer()

root = Tk()
root.title('mcSoundOutput')
root.geometry('600x400')

# mp.play_string('CQ CQ CQ')

mcLabel = Label(root, text="Enter text to xmit in caps 50 chars max:")
mcLabel.pack()

mcTextbox = Entry(root, width=50)
mcTextbox.pack()

mcButton = Button(root, text='Submit', command=mp.play_string('CQ CQ'))
mcButton.pack()

root.mainloop()




