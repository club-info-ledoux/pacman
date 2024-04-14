import tkinter
import joueur


class Joueur():
    def __init__(self,window,canvas,map,liste_objet,x,y,nb_piece,fantomes):
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
        self.fantomes=fantomes
        self.update()

        if joueur.MANUEL:
            canvas.bind("<d>", self.modifier_direction)
            canvas.bind("<z>", self.modifier_direction)
            canvas.bind("<s>", self.modifier_direction)
            canvas.bind("<q>", self.modifier_direction)





    def update(self):
        self.deplacement()
        self.modifier_direction(None)

        for i in self.fantomes:
            x, y = i.update()
            self.map[(y-32)//32][(x-64)//32]="f"

        self.window.after(150, self.update)

    def deplacement(self):
        # self.map[self.x][self.y] = "."
        x = self.x+ self.cst_move[self.direction][0]
        y = self.y+ self.cst_move[self.direction][1]
        if self.verif_collision(x,y)==False:
            self.map[(self.y-32)//32][(self.x-64)//32]="."
            self.x,self.y=x,y
            self.afficher(self.direction, self.x, self.y)
        else:
            pass
    def verif_collision(self,x,y):
        
        if self.map[(y-32)//32][(x-64)//32]=="f":
            print("miam, t'as perdu")

        if self.map[(y-32)//32][(x-64)//32]=="O":
            self.canvas.delete(self.liste_objet[(y-32)//32][(x-64)//32])
            self.map[(y-32)//32][(x-64)//32]="."
            self.nb_piece-=1
        if self.map[(y-32)//32][(x-64)//32]=="#":
            return True
        else:
            self.map[(y-32)//32][(x-64)//32]="p"
            return False



    def afficher(self, direction, x, y):
        self.canvas.coords(self.image, x, y)

    def modifier_direction(self, event):
        # direction = event.char
        if joueur.MANUEL and event != None: 
            direction = event.char
        elif not joueur.MANUEL and event == None:
            direction = joueur.play(self.map)
        else:
            return
        
        if direction == "d":
            self.direction = 1
            self.gif= tkinter.PhotoImage(file="pacman_droite.gif")
            self.canvas.itemconfigure(self.image, image=self.gif)
        elif direction == "z":
            self.direction = 0
            self.gif= tkinter.PhotoImage(file="pacman_haut.gif")
            self.canvas.itemconfigure(self.image, image=self.gif)
        elif direction == "q":
            self.direction = 3
            self.gif= tkinter.PhotoImage(file="pacman_gauche.gif")
            self.canvas.itemconfigure(self.image, image=self.gif)
        elif direction == "s":
            self.gif= tkinter.PhotoImage(file="pacman_bas.gif")
            self.canvas.itemconfigure(self.image, image=self.gif)
            self.direction = 2

    #animation du titre
    def update_image(self,delay=150):
        self.ind += 1
        if self.ind == 4: self.ind = 0
        self.gif.configure(format="gif -index " + str(self.ind))
        self.window.after(delay, self.update_image)







