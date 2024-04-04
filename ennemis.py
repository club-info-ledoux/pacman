import tkinter
import fantome


class Fantome():
    def __init__(self,window,canvas,map,liste_objet,x,y,nb_piece,couleur):
        self.direction=1
        self.cst_move = ((0,-32),(32,0),(0,32),(-32,0))
        self.x=x
        self.y=y
        self.ind = -1
        self.nb_piece=nb_piece
        self.img = tkinter.PhotoImage(file="fantome_" + couleur + ".gif")
        self.canvas = canvas
        self.image = self.canvas.create_image(self.x,self.y,image=self.img)
        self.map=map
        self.window=window
        self.liste_objet=liste_objet
        self.couleur = couleur
        self.update()

        if fantome.MANUEL:
            canvas.bind("<d>", self.modifier_direction)
            canvas.bind("<z>", self.modifier_direction)
            canvas.bind("<s>", self.modifier_direction)
            canvas.bind("<q>", self.modifier_direction)



    def update(self):
        self.deplacement()
        self.modifier_direction(None)
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

    def modifier_direction(self, event):
        # direction = event.char
        if fantome.MANUEL and event != None: 
            direction = event.char
        elif not fantome.MANUEL and event == None:
            direction = fantome.play(self.map, self.couleur)
        else:
            return
        

        if direction == "d":
            self.direction = 1
            self.canvas.itemconfigure(self.image, image=self.img)
        elif direction == "z":
            self.direction = 0
            self.canvas.itemconfigure(self.image, image=self.img)
        elif direction == "q":
            self.direction = 3
            self.canvas.itemconfigure(self.image, image=self.img)
        elif direction == "s":
            self.canvas.itemconfigure(self.image, image=self.img)
            self.direction = 2








