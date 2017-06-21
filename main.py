
from libs import *
import Enemys
import sys

n = nave()
e = list()

for a in range(8):
    for b in range(4):
        e.append(enemy(Enemys.Aliens[randint(0,2)],a*5,b*6))
tiros = []

class Vitoria:
    def __init__(self, master):
        photo = PhotoImage(file='youwin.png')
        self.w = w = Label(master, image=photo)

        width = photo.width()
        height = photo.height()

        master.geometry("%dx%d+0+0" % (width, height))
        w.photo = photo
        w.pack()

        self.exit = Button(master, text="Fechar", command=sys.exit, height=1, width=3, fg= "white",bg = "black")
        self.exit.config(font=("Courier", 10))
        self.exit.place(x=130, y=180)

def v():
    root = Tk()
    app = Vitoria(root)
    root.mainloop()

def myReshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70, float(w)/h+0.2, 0.1, 60)
    glMatrixMode(GL_MODELVIEW)
    glutPostRedisplay()

def myKeyboard(tecla,x,y):
    if(tecla == GLUT_KEY_RIGHT):
        n.move('r')
    if(tecla == GLUT_KEY_LEFT):
        n.move('l')
    if(tecla == GLUT_KEY_UP):
        tiros.append(n.tiro(n))

def mytimetiro(time):

    for t in tiros:
        t.pos[1] += 0.5
        if(t.pos[1] > 60):
            tiros.remove(t)


    glutPostRedisplay()
    glutTimerFunc(2,mytimetiro,0)

def mytimeEnemy(time):
    for a in e:
        a.y -= 0.05
        if(a.face < -1):
            close()

    glutPostRedisplay()
    glutTimerFunc(3,mytimeEnemy,0)

def myDisplay():
    glClearColor(0.2, 0.2, 0.2, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


    glLoadIdentity()
    gluLookAt(30.5,-6,15,
              30.5,9,0,
              0, 1, 0)

    n.draw_nave()
    n.draw_tiro(tiros)


    r = colisao(n,tiros,e)
    if(r != -1 and r != "Game Over"):
        e.remove(r[0])
        tiros.remove(r[1])
    elif(r == "Game Over"):
        print(r)
        close()
    if(len(e) == 0):
        v()

    for a in e:
        a.draw_enemy()

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(1400, 800)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Space Invader")
    glEnable(GL_DEPTH_TEST)

    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    glutIdleFunc(myDisplay)
    glutSpecialFunc(myKeyboard)
    glutTimerFunc(2,mytimetiro,0)
    glutTimerFunc(2,mytimeEnemy,0)
    glutMainLoop()
