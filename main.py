import tkinter
import pacman
#import map #Nathan doit mettre

window=tkinter.Tk()
canvas=tkinter.Canvas(window,width=992,height=992,background="red")


canvas.pack()

#map=map.generer()
j1=pacman.Joueur(window,canvas)
j1.update_image()

canvas.focus_set()
canvas.bind("<d>", j1.modifier_direction)
canvas.bind("<z>", j1.modifier_direction)
canvas.bind("<s>", j1.modifier_direction)
canvas.bind("<q>", j1.modifier_direction)

window.mainloop()