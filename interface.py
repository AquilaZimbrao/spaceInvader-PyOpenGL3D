from __init__ import *
import pygame
from pygame.mixer import Sound
root = Tk()

def startgame():
    root.destroy()
    main()

class App:
    def __init__(self,master):

        photo = PhotoImage(file='start.png')
        self.w = w = Label(master, image=photo)

        width = photo.width()
        height = photo.height()

        master.geometry("%dx%d+0+0" % (width, height))
        w.photo = photo
        w.pack()

        self.hello_b = Button(master,text="Start",command=startgame, height=2,width=6,fg= "white",bg = "black")
        self.hello_b.config(font=("Courier", 20))
        self.hello_b.place(x=630, y=550)

def inicio():
    app = App(root)
    root.mainloop()

inicio()