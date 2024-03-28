import tkinter
import json


class Joueur():
    def __init__(self,window,canvas,map,liste_objet,x,y,nb_piece):
        self.direction=1
        self.cst_move = ((0,-32),(32,0),(0,32),(-32,0))
        self.x=x
        self.y=y
        self.ind = -1
        self.nb_piece=nb_piece
        self.gif = tkinter.PhotoImage(file="pacman_droite.gif")
        self.canvas = canvas
        self.image = self.canvas.create_image(self.x,self.y,image=self.gif, tag="photo")
        self.map=map
        self.window=window
        self.liste_objet=liste_objet
        self.update()



    def update(self):
        self.deplacement()
        self.window.after(150, self.update)

    def deplacement(self):
        x = self.x+ self.cst_move[self.direction][0]
        y = self.y+ self.cst_move[self.direction][1]
        if self.verif_collision(x,y)==False:
            self.x,self.y=x,y
            self.afficher(self.direction, self.x, self.y)
        else:
            pass
    def verif_collision(self,x,y):
        if self.map[(y-32)//32][(x-64)//32]=="O":
            self.canvas.delete(self.liste_objet[(y-32)//32][(x-64)//32])
            self.map[(y-32)//32][(x-64)//32]="U"
            self.nb_piece-=1


        try:

            return self.map[(y-32)//32][(x-64)//32]=="#"
        except:
            return False



    def afficher(self, direction, x, y):
        self.canvas.coords(self.image, x, y)

    def modifier_direction(self,event):
        if event.char == "d":
            self.direction = 1
            self.gif= tkinter.PhotoImage(file="pacman_droite.gif")
            self.canvas.itemconfigure(self.image, image=self.gif)
        elif event.char == "z":
            self.direction = 0
            self.gif= tkinter.PhotoImage(file="pacman_haut.gif")
            self.canvas.itemconfigure(self.image, image=self.gif)
        elif event.char == "q":
            self.direction = 3
            self.gif= tkinter.PhotoImage(file="pacman_gauche.gif")
            self.canvas.itemconfigure(self.image, image=self.gif)
        elif event.char == "s":
            self.gif= tkinter.PhotoImage(file="pacman_bas.gif")
            self.canvas.itemconfigure(self.image, image=self.gif)
            self.direction = 2

    def display_gif(self):
        self.ind += 1
        if self.ind == 4:
            self.ind = 0
        self.gif.configure(format="gif index- " + str(self.ind))
        window.after(100, self.display_gif)


    #animation du titre
    def update_image(self,delay=200):
        self.ind += 1
        if self.ind == 4: self.ind = 0
        self.gif.configure(format="gif -index " + str(self.ind))
        self.window.after(delay, self.update_image)







