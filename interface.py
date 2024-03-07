
from tkinter import *

# def fenetre
fenetre = Tk()
fenetre.geometry("1200x650")
fenetre.title("Pac-man")

#def canvas
menu = Canvas(fenetre, width=1200, height=650, bg="yellow", highlightthickness=0)
menu.pack()
partie = Canvas(fenetre, width=1200, height=650, bg="purple", highlightthickness=0)

#importation images
img_bouton_nouvelle_partie = PhotoImage(file="images/b_new_game.png")
img_labyrinthe = PhotoImage(file = "images/labyrinthe.png")

#def fonctions
def nouvelle_partie(event):
    menu.pack_forget()
    partie.pack()

#boutons
bouton_nouvelle_partie = menu.create_image(600, 300, image=img_bouton_nouvelle_partie)
menu.tag_bind(bouton_nouvelle_partie, '<1>', nouvelle_partie)




fenetre.mainloop()