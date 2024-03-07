import tkinter
class Joueur():
    def __init__(self,canvas):
        self.direction=1
        self.cst_move = ((0,-32),(32,0),(0,32),(-32,0))
        self.x=0
        self.y=0
        self.canvas=canvas
        self.image=self.canvas.create_rectangle(0,0,32,32,fill="Yellow")
        self.update()

    def update(self):
        self.deplacement()
        window.after(50, self.update)

    def deplacement(self):
        self.x += self.cst_move[self.direction][0]
        self.y += self.cst_move[self.direction][1]
        self.afficher(self.direction, self.x, self.y)

    def afficher(self, direction, x, y):
        self.canvas.coords(self.image, x, y, x+32, y+32)
    def modifier_direction(self,event):
        if event.char == "d":
            self.direction = 1
        elif event.char == "z":
            self.direction = 0
        elif event.char == "q":
            self.direction = 3
        elif event.char == "s":
            self.direction = 2


window=tkinter.Tk()
canvas=tkinter.Canvas(window,width=800,height=500,background="red")


canvas.pack()
j1=Joueur(canvas)

canvas.focus_set()
canvas.bind("<d>", j1.modifier_direction)
canvas.bind("<z>", j1.modifier_direction)
canvas.bind("<s>", j1.modifier_direction)
canvas.bind("<q>", j1.modifier_direction)

window.mainloop()