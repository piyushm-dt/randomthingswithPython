import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

win = Tk()
win.title('WikiX')
win.geometry('300x100')

# the searching function.
def searchX():
    search = entry.get()
    answer = wikipedia.summary(search)
    showinfo("Summary ",answer)

# define the indication on and position of the label, button and search box.    

label = Label(win,text="Wiki Search: ")
label.grid(row=0,column=0)

entry = Entry(win)
entry.grid(row=2,column=2)

button = Button(win,text="Spit",command=searchX)
button.grid(row=1,column=1,padx=10)

win.mainloop()
