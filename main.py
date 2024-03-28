from tkinter import *
import ctypes
import random

user32 = ctypes.windll.user32
screensize ={ "x":int(user32.GetSystemMetrics(0)), "y":int(user32.GetSystemMetrics(1))}

window=Tk()
window.attributes('-fullscreen', True)
window.title("Snake")

frame=Frame(window,width=screensize["x"],height=screensize["y"],background="white")
frame=Frame(window,width=screensize["x"],height=screensize["y"],background="Black")
frame.place(x=0,y=0)

def afficher_menu():
    for widget in frame.winfo_children(): widget.destroy()
    map_rezet()
    Play_bouton=Button(frame,borderwidth=0,image=image_play,bg="black",command=lambda:(play(frame)))
    Play_bouton.place(x=int(screensize["x"]*0.5)-125,y=int(screensize["y"]*0.5))

canvas=0

def map_rezet():
    global map_liste
    map_liste=[[0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],


           ]



#----------------image-------------------
image_play=PhotoImage(file="play.png")
#terrain----------------------------------
image_pair=PhotoImage(file="case_pair.png")
image_impair=PhotoImage(file="case_impair.png")

image_apple=PhotoImage(file="apple.png")

#serpent-------------------------------------------------------------
image_serpent_body_bottomleft=PhotoImage(file="body_bottomleft.png")
image_serpent_body_bottomright=PhotoImage(file="body_bottomright.png")

image_serpent_body_horizontal=PhotoImage(file="body_horizontal.png")
image_serpent_body_topleft=PhotoImage(file="body_topleft.png")
image_serpent_body_topright=PhotoImage(file="body_topright.png")
image_serpent_body_vertical=PhotoImage(file="body_vertical.png")

image_serpent_head_down=PhotoImage(file="head_down.png")
image_serpent_head_left=PhotoImage(file="head_left.png")
image_serpent_head_right=PhotoImage(file="head_right.png")
image_serpent_head_up=PhotoImage(file="head_up.png")

image_serpent_tail_down=PhotoImage(file="tail_down.png")
image_serpent_tail_left=PhotoImage(file="tail_left.png")
image_serpent_tail_right=PhotoImage(file="tail_right.png")
image_serpent_tail_up=PhotoImage(file="tail_up.png")



def play(frame): #supprime les éléments de la frame , créé un canvas , affiche la map, créer une pomme et un serpent
    global canvas
    for widget in frame.winfo_children(): widget.destroy()


    canvas=Canvas(frame,width=screensize["x"],height=screensize["y"],background="black")
    canvas.place(x=-2,y=-2)
    print(canvas)
    afficher_map(canvas)
    apple_generate(canvas)
    canvas.focus_set()
    canvas.bind("<d>", modifier_direction)
    canvas.bind("<z>", modifier_direction)
    canvas.bind("<s>", modifier_direction)
    canvas.bind("<q>", modifier_direction)
    snake(canvas)



def afficher_map(canvas):

    for y in range(10):
        for x in range(10):
            if (x+y)%2==0:
                canvas.create_image((screensize["x"]//2)-200+x*40,(screensize["y"]//2)-200+y*40,image=image_pair)
            else:
                canvas.create_image((screensize["x"]//2)-200+x*40,(screensize["y"]//2)-200+y*40,image=image_impair)
def apple_generate(canvas):
    x=0
    y=0
    on_serpent=True
    while on_serpent==True:
        x=random.randint(0,9)
        y=random.randint(0,9)
        a=0
        for dictionaire in snake_liste:

            if dictionaire["x"]==x and dictionaire["y"]==y:
                a+=1
        if a==0:
            on_serpent=False

    map_liste[y][x]=2
    canvas.create_image((screensize["x"]//2)-200+x*40,(screensize["y"]//2)-200+y*40,image=image_apple,tags="apple")

#var du serpent
ancienne_direction=1
direction=1
etat="en_jeux"
snake_liste=[{"x":0,"y":0},{"x":1,"y":0},{"x":2,"y":0}]
def snake(canvas):
    global direction,snake_liste
    snake_liste=[{"x":0,"y":0},{"x":1,"y":0},{"x":2,"y":0}]

    #mise dans la map
    map_liste[0][0]=1
    map_liste[0][1]=1
    map_liste[0][2]=1

    #creation image avec tkinter
    snake_liste[-1]["objet"]=canvas.create_image((screensize["x"]//2)-200+snake_liste[-1]["x"]*40,(screensize["y"]//2)-200+snake_liste[-1]["y"]*40,image=image_serpent_head_right,tags="head")
    snake_liste[1]["objet"]=canvas.create_image((screensize["x"]//2)-200+snake_liste[1]["x"]*40,(screensize["y"]//2)-200+snake_liste[1]["y"]*40,image=image_serpent_body_horizontal)
    snake_liste[0]["objet"]=canvas.create_image((screensize["x"]//2)-200+snake_liste[0]["x"]*40,(screensize["y"]//2)-200+snake_liste[0]["y"]*40,image=image_serpent_tail_left)

    boucle_snake()


def deplacement():#modifie la position du srpent et change les images
    global etat,direction,snake_liste,canvas,ancienne_direction
    const=((0,-1),(1,0),(0,1),(-1,0))
    x=snake_liste[-1]["x"]+const[direction][0]
    y=snake_liste[-1]["y"]+const[direction][1]

    try:
        if map_liste[y][x]==2:
                canvas.delete("apple")
                apple_generate(canvas)

        else:
            canvas.delete(snake_liste[0]["objet"])
            map_liste[snake_liste[0]["y"]][snake_liste[0]["x"]]=0
            del(snake_liste[0])
    except:
        etat="fin"
        return afficher_menu()




    compteur=0

    for dictionaire in snake_liste:
        if dictionaire["x"]==x and dictionaire["y"]==y:
            compteur+=1

    if compteur>=1 or x<0 or y<0 or x>10 or y>10 :
        etat="fin"
        return afficher_menu()

    else:
        if direction==2:
            objet=canvas.create_image((screensize["x"]//2)-200+x*40,(screensize["y"]//2)-200+y*40,image=image_serpent_head_down)
        if direction==3:
            objet=canvas.create_image((screensize["x"]//2)-200+x*40,(screensize["y"]//2)-200+y*40,image=image_serpent_head_left)
        if direction==0:
            objet=canvas.create_image((screensize["x"]//2)-200+x*40,(screensize["y"]//2)-200+y*40,image=image_serpent_head_up)
        if direction==1:
            objet=canvas.create_image((screensize["x"]//2)-200+x*40,(screensize["y"]//2)-200+y*40,image=image_serpent_head_right)
        map_liste[y][x]=1
        snake_liste.append({"x":x,"y":y,"objet":objet})



    if ancienne_direction==0 and direction==0:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_vertical)
    elif ancienne_direction==0 and direction==1:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_bottomright)
    elif ancienne_direction==0 and direction==3:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_bottomleft)
    elif ancienne_direction==1 and direction==0:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_topleft)
    elif ancienne_direction==1 and direction==1:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_horizontal)
    elif ancienne_direction==1 and direction==2:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_bottomleft)
    elif ancienne_direction==2 and direction==1:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_topright)
    elif ancienne_direction==2 and direction==2:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_vertical)
    elif ancienne_direction==2 and direction==3:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_topleft)
    elif ancienne_direction==2 and direction==0:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_topleft)
    elif ancienne_direction==3 and direction==0:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_topright)
    elif ancienne_direction==3 and direction==2:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_bottomright)
    elif ancienne_direction==3 and direction==3:canvas.itemconfigure(snake_liste[len(snake_liste)-2]["objet"], image=image_serpent_body_horizontal)


    difx,dify=snake_liste[0]["x"]-snake_liste[1]["x"],snake_liste[0]["y"]-snake_liste[1]["y"]
    if difx==-1 and dify==0:canvas.itemconfigure(snake_liste[0]["objet"], image=image_serpent_tail_left)
    if difx==1 and dify==0:canvas.itemconfigure(snake_liste[0]["objet"], image=image_serpent_tail_right)
    if difx==0 and dify==-1:canvas.itemconfigure(snake_liste[0]["objet"], image=image_serpent_tail_up)
    if difx==0 and dify==1:canvas.itemconfigure(snake_liste[0]["objet"], image=image_serpent_tail_down)

    ancienne_direction=direction


def boucle_snake():

    deplacement()

    if etat=="en_jeux":
        window.after(200,boucle_snake)






def modifier_direction(event):
    global direction,ancienne_direction
    if event.char == "d":
        direction = 1

    elif event.char == "z":
        direction = 0

    elif event.char == "q":
        direction = 3

    elif event.char == "s":
        direction = 2







afficher_menu()
window.mainloop()
