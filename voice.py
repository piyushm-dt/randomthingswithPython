import tkinter as tk
from gtts import gTTS
from playsound import playsound
import random, string

# define the GUI
win = tk.Tk()
win.title("Text to Speech")
win.geometry("200x200")

# generate file names
def randomword():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(7))

# convert text to speech
def textSpeech():
    text = entry.get()
    speech = gTTS(text=text,lang="en")
    name = randomword()
    speech.save(r'C:\Users\Downloads\%s.mp3'%name)
    playsound(r'C:\Users\Downloads\%s.mp3'%name)

# position and indication of label
label = tk.Label(win,text="Enter here")
label.grid(row=0,column=0)

# position and indication of entry box.
entry = tk.Entry(win)
entry.grid(row=0,column=2)

#position and indication of button.
button = tk.Button(win,text="Press",command=textSpeech)
button.grid(row=5,column=2)

win.mainloop()
