import tkinter
import joueur


class Joueur():
    def __init__(self,window,canvas,map,liste_objet,x,y,nb_piece,fantomes):
        print("joueur créé")
        self.direction=0
        self.last_input = "d"
        self.direction_waiting = False
        self.cst_move = ((0,-32),(32,0),(0,32),(-32,0))
        self.x=x
        self.y=y
        self.ind = -1
        self.nb_piece=nb_piece
        self.gif = tkinter.PhotoImage(file="assets/images/pacman/pacman_droite.gif")
        self.canvas = canvas
        self.image = self.canvas.create_image(self.x,self.y,image=self.gif, tag="photo")
        self.map=map
        self.window=window
        self.liste_objet=liste_objet
        self.fantomes=fantomes
        self.update()
        joueur.init(map)

        if joueur.MANUEL:
            canvas.bind("<d>", self.entree_direction)
            canvas.bind("<z>", self.entree_direction)
            canvas.bind("<s>", self.entree_direction)
            canvas.bind("<q>", self.entree_direction)





    def update(self):
        self.deplacement()
        self.entree_direction(None)

        for i in self.fantomes:
            x, y = i.update()
            self.map[(y-32)//32][(x-64)//32]="f"

        self.window.after(150, self.update)

    def deplacement(self):
        x = self.x+ self.cst_move[self.direction][0]
        y = self.y+ self.cst_move[self.direction][1]
        collision = self.verif_collision(x,y)
        if collision !="#":
            if collision == "p1":
                self.x = (self.map[15].index("p2") + 2)*32
            elif collision == "p2":
                self.x = (self.map[15].index("p1") + 2)*32
            else:
                self.map[(self.y-32)//32][(self.x-64)//32] = "."
                self.x,self.y=x,y
                self.afficher(self.direction, self.x, self.y)
        else:
            pass
        
        self.map[(self.y-32)//32][(self.x-64)//32] = "p"
        

    def verif_collision(self,x,y):
        
        if self.map[(y-32)//32][(x-64)//32]=="f":
            print("miam, t'as perdu")

        if self.map[(y-32)//32][(x-64)//32]=="O":
            self.canvas.delete(self.liste_objet[(y-32)//32][(x-64)//32])
            self.map[(y-32)//32][(x-64)//32]="."
            self.nb_piece-=1

        return self.map[(y-32)//32][(x-64)//32]



    def afficher(self, direction, x, y):
        self.canvas.coords(self.image, x, y)

    def entree_direction(self,event):
        if joueur.MANUEL and event != None: 
            self.last_input = event.char
        elif not joueur.MANUEL and event == None:
            self.last_input = joueur.play(self.map)
        else:
            return
        
        self.direction_waiting = True
        self.modifier_direction()


    def modifier_direction(self):
        if self.direction_waiting:
            if self.last_input == "z" and self.verif_collision(self.x+ self.cst_move[0][0], self.y+ self.cst_move[0][1]) != "#" and self.direction != 2:
                self.direction = 0
                self.gif= tkinter.PhotoImage(file="assets/images/pacman/pacman_haut.gif")
                self.canvas.itemconfigure(self.image, image=self.gif)
                self.direction_waiting = False

            elif self.last_input == "q" and self.verif_collision(self.x+ self.cst_move[3][0], self.y+ self.cst_move[3][1]) != "#" and self.direction != 1:
                self.direction = 3
                self.gif= tkinter.PhotoImage(file="assets/images/pacman/pacman_gauche.gif")
                self.canvas.itemconfigure(self.image, image=self.gif)
                self.direction_waiting = False

            elif self.last_input == "s" and self.verif_collision(self.x+ self.cst_move[2][0], self.y+ self.cst_move[2][1]) != "#" and self.direction != 0:
                self.direction = 2
                self.gif= tkinter.PhotoImage(file="assets/images/pacman/pacman_bas.gif")
                self.canvas.itemconfigure(self.image, image=self.gif)
                self.direction_waiting = False

            elif self.last_input == "d" and self.verif_collision(self.x+ self.cst_move[1][0], self.y+ self.cst_move[1][1]) != "#" and self.direction != 3:
                self.direction = 1
                self.gif= tkinter.PhotoImage(file="assets/images/pacman/pacman_droite.gif")
                self.canvas.itemconfigure(self.image, image=self.gif)
                self.direction_waiting = False

            else:
                self.window.after(100, self.modifier_direction)

    #animation du titre
    def update_image(self,delay=200):
        self.ind += 1
        if self.ind == 4: self.ind = 0
        self.gif.configure(format="gif -index " + str(self.ind))
        self.window.after(delay, self.update_image)







