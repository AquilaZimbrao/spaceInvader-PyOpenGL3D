from Tkinter import *

import pygame
from pygame.mixer import Sound
from libs import *
from interface import *

class cube():
    def __init__(self, t=None):
        self.x = 0
        self.y = 0
        self.z = 0
        if (t == None):
            self.tam = 1
        else:
            self.tam = t

    def get_pos(self):
        return [self.x, self.y, self.z]

class circ():
    def __init__(self):
        self.tam = 0.5
        self.pos = [0, 0, 0]

class nave():
    def __init__(self):
        self.x = 0
        self.cubes = []
        for a in range(4):
            self.cubes.append(cube())

    def draw_nave(self):
        self.cubes[0].x = 29.5 + self.x
        self.cubes[0].y = 0.5

        self.cubes[1].x = 30.5 + self.x
        self.cubes[1].y = 0.5

        self.cubes[2].x = 31.5 + self.x
        self.cubes[2].y = 0.5

        self.cubes[3].x = 30.5 + self.x
        self.cubes[3].y = 1.5

        for c in self.cubes:
            glColor3f(1, 1, 1)
            glPushMatrix()
            glColor3f(1, 1, 1)
            glTranslatef(c.x, c.y, c.z)
            glutSolidCube(c.tam)

            glPopMatrix()

            glPushMatrix()

            glColor3f(0, 0, 0)
            glTranslatef(c.x, c.y, c.z)
            glutWireCube(c.tam)

            glPopMatrix()

    def move(self, direcao):
        if (direcao == 'r'):
            if (self.cubes[2].x <= 49):
                self.x += 0.8
        if (direcao == 'l'):
            if (self.cubes[0].x > 11):
                self.x -= 0.8

    def tiro(self, nave):
        pygame.mixer.init(44100, -16, 2, 2048)
        audio = Sound('shoot.wav')
        audio.play()
        tiro = circ()
        tiro.pos = [nave.cubes[3].x, nave.cubes[3].y + 1.5, 0]

        return tiro

    def draw_tiro(self, tiros):

        for t in tiros:
            glColor3f(0, 1, 0)
            glPushMatrix()
            glColor3f(1, 0, 0)
            glTranslatef(t.pos[0], t.pos[1], t.pos[2])
            glutSolidSphere(GLdouble(0.25), GLint(10), GLint(10))

            glPopMatrix()

            glPushMatrix()

            glColor3f(0, 0, 0)
            glTranslatef(t.pos[0], t.pos[1], t.pos[2])
            glutWireSphere(GLdouble(0.25), GLint(10), GLint(10))

            glPopMatrix()

class enemy():
    def __init__(self, e, x, y):
        self.x = x
        self.y = y
        self.face = 2000
        self.leaft = 2000
        self.rigth = -2000

        self.matrix = e
        self.cubes = []
        for a in range(8):
            c = list()
            for b in range(11):
                if (self.matrix[a][b] != 0):
                    c.append(cube(0.3))
                else:
                    c.append(0)
            self.cubes.append(c)

    def draw_enemy(self):
        for nl, l in enumerate(self.matrix):
            for nc, c in enumerate(l):
                if (self.matrix[nl][nc] != 0):

                    glPushMatrix()
                    if (self.matrix[nl][nc] == 1):
                        glColor3f(1, 1, 1)
                    else:
                        glColor3f(0, 0, 0)

                    self.cubes[nl][nc].x = 10 + self.x + (self.cubes[nl][nc].tam * nc)
                    self.cubes[nl][nc].y = 60 + self.y + (self.cubes[nl][nc].tam * nl)
                    self.cubes[nl][nc].z = 0

                    glTranslatef(self.cubes[nl][nc].x, self.cubes[nl][nc].y, self.cubes[nl][nc].z)
                    glutSolidCube(self.cubes[nl][nc].tam)
                    self.face = min(self.face, self.cubes[nl][nc].y)
                    self.leaft = min(self.leaft, self.cubes[nl][nc].x)
                    self.rigth = max(self.rigth, self.cubes[nl][nc].x)

                    glColor3f(0, 0, 0)
                    glutWireCube(self.cubes[nl][nc].tam)

                    glPopMatrix()

def colisao(nave, listTiros, listEnemys):
    for e in listEnemys:
        for t in listTiros:
            if (t.pos[0]  >= e.leaft - 0.3
                and t.pos[0] <= e.rigth + 0.3
                and t.pos[1] + t.tam >= e.face - 0.3):
                pygame.mixer.init(44100, -16, 2, 2048)
                audio2 = Sound('invaderkilled.wav')
                audio2.play()
                return [e, t]

        for c in nave.cubes:
            if (c.x - 0.5 > e.leaft - 0.3
                and c.x + 0.5 < e.rigth + 0.3
                and c.y + 0.5 >= e.face):
                return "Game Over"
    return -1

class Fim:
    def __init__(self,master):

        photo = PhotoImage(file='gameover.png')
        self.w = w = Label(master, image=photo)

        width = photo.width()
        height = photo.height()

        master.geometry("%dx%d+0+0" % (width, height))
        w.photo = photo
        w.pack()

        self.exit = Button(master, text="Fechar", command=sys.exit, height=1, width=3, fg="red", bg="white")
        self.exit.config(font=("Courier", 10))
        self.exit.place(x=120, y=400)

def close():
    root = Tk()
    app = Fim(root)
    root.mainloop()

