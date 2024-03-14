from tkinter import *

# def fenetre
fenetre = Tk()
fenetre.attributes('-fullscreen', True)
fenetre.title("Pac-man")

#def canvas
menu = Canvas(fenetre, bg="yellow", highlightthickness=0)
menu.pack()
partie = Canvas(fenetre, bg="purple", highlightthickness=0)

#importation images
img_bouton_nouvelle_partie = PhotoImage(file="images/b_new_game.png")

#def fonctions
def nouvelle_partie(event):
    menu.pack_forget()
    partie.pack()

#boutons
bouton_nouvelle_partie = menu.create_image(0, 0, image=img_bouton_nouvelle_partie)
menu.tag_bind(bouton_nouvelle_partie, '<1>', nouvelle_partie)




fenetre.mainloop()