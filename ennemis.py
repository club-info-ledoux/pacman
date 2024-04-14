import tkinter
import fantome


class Fantome():
    def __init__(self,window,canvas,map,liste_objet,x,y,nb_piece,couleur):
        print("fantome créé")
        self.direction=1
        self.cst_move = ((0,-32),(32,0),(0,32),(-32,0))
        self.x=x
        self.y=y
        self.ind = -1
        self.nb_piece=nb_piece
        self.img = tkinter.PhotoImage(file="assets/images/fantomes/fantome_" + couleur + ".png")
        self.canvas = canvas
        self.image = self.canvas.create_image(self.x,self.y,image=self.img)
        self.map=map
        self.window=window
        self.liste_objet=liste_objet
        self.couleur = couleur
        self.update()

        if fantome.MANUEL:
            canvas.bind("<d>", self.entree_direction)
            canvas.bind("<z>", self.entree_direction)
            canvas.bind("<s>", self.entree_direction)
            canvas.bind("<q>", self.entree_direction)



    def update(self):
        self.deplacement()
        self.entree_direction(None)
        return (self.x, self.y)

    def deplacement(self):
        # self.map[self.x][self.y] = "."
        x = self.x+ self.cst_move[self.direction][0]
        y = self.y+ self.cst_move[self.direction][1]
        if self.verif_collision(x,y)==False:
            self.x,self.y=x,y
            self.afficher(self.direction, self.x, self.y)
        else:
            pass

        # self.map[self.x][self.y] = "p"
    
    def verif_collision(self,x,y):
        if self.map[(y-32)//32][(x-64)//32]=="p":
            print("miam, t'as perdu")

        try:
            return self.map[(y-32)//32][(x-64)//32]=="#"
        except:
            return False



    def afficher(self, direction, x, y):
        self.canvas.coords(self.image, x, y)

    def entree_direction(self,event):
        if fantome.MANUEL and event != None: 
            self.last_input = event.char
        elif not fantome.MANUEL and event == None:
            self.last_input = fantome.play(self.map, self.couleur)
        else:
            return
        
        self.direction_waiting = True
        self.modifier_direction()


    def modifier_direction(self):
        if self.direction_waiting:
            if self.last_input == "z" and self.verif_collision(self.x+ self.cst_move[0][0], self.y+ self.cst_move[0][1]) != "#" and self.direction != 2:
                self.direction = 0
                self.direction_waiting = False

            elif self.last_input == "q" and self.verif_collision(self.x+ self.cst_move[3][0], self.y+ self.cst_move[3][1]) != "#" and self.direction != 1:
                self.direction = 3
                self.direction_waiting = False

            elif self.last_input == "s" and self.verif_collision(self.x+ self.cst_move[2][0], self.y+ self.cst_move[2][1]) != "#" and self.direction != 0:
                self.direction = 2
                self.direction_waiting = False

            elif self.last_input == "d" and self.verif_collision(self.x+ self.cst_move[1][0], self.y+ self.cst_move[1][1]) != "#" and self.direction != 3:
                self.direction = 1
                self.direction_waiting = False

            else:
                self.window.after(100, self.modifier_direction)





