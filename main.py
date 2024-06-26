import tkinter
import pacman
import ennemis
from map import *
#import map #Nathan doit mettre

window=tkinter.Tk()
canvas=tkinter.Canvas(window,width=992,height=1200,background="black")
image=tkinter.PhotoImage(file="assets/images/case/case_mur.png")
image2=tkinter.PhotoImage(file="assets/images/case/case_pieces.png")

canvas.pack(side="top")

Map=MapGenerator()
map=Map.generate_map()
x=0
y=0
nb_piece=0
liste_objet = [[0 for i in range(31)] for i in range(31)]
for i in range(len(map)):
    for j in range(28):
        if map[i][j]=="#":
            canvas.create_image(64+j*32,32+i*32,image=image)
        if map[i][j]=="p":
            x=64+j*32
            y=32+i*32
        if map[i][j]=="O":
            nb_piece+=1
            liste_objet[i][j]=canvas.create_image(64+j*32,32+i*32,image=image2)
        if map[i][j]=="U":
            map[i][j]="."


fantome_bleu=ennemis.Fantome(window,canvas,map,liste_objet,480,512,nb_piece,"bleu")
fantome_rouge=ennemis.Fantome(window,canvas,map,liste_objet,544,512,nb_piece,"rouge")

j1=pacman.Joueur(window,canvas,map,liste_objet,x,y,nb_piece,[fantome_bleu, fantome_rouge])
j1.update_image()

canvas.focus_set()

window.mainloop()