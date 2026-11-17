# Créé par Clément, le 23/03/2022 en Python 3.7
from tkinter import *
from random import randint

vit_x = 13
vit_y = 0



animation_active = False
stop_animation = False



# ----------------------------------------------------------------
# Fonctions

def modification():
    global vit_x, vit_y, animation_active, stop_animation,vie1,score1

    animation_active = True
    mod_angle = 0
    liste_coord = monCanvas.coords(pacman_1)
    liste_items = monCanvas.find_overlapping(liste_coord[0],liste_coord[1],liste_coord[2],liste_coord[3])
    #print(liste_items)
    test_collision = False

    if vie1==0:
        défaite()

    if len(liste_items) > 1 :
        if liste_items[1]==2:
            pommier()
            score1+=10
            score.config(text=score1)

        else:
            for x in liste_items :
                if x != pacman_1 :
                    test_collision = True
                    break

    if test_collision == True :
        monCanvas.itemconfig(pacman_1, fill="red")
        vie1-=10
        compt.config(text=vie1)


    else:
        monCanvas.itemconfig(pacman_1, fill="yellow")

    if liste_coord[2]>500 :
        vit_x = -13

    elif liste_coord[0]<0 :
        vit_x = 13

    elif liste_coord[1]<0 :
        vit_y = 13

    elif liste_coord[3]>600 :
        vit_y = -13

    if (vit_x <0 or vit_y>0) :
        mod_angle = 180

    if vit_y == 0 :
        if (monCanvas.itemcget(pacman_1, 'start') == '15.0' or monCanvas.itemcget(pacman_1, 'start') == '195.0') :
            monCanvas.itemconfig(pacman_1, start=30+mod_angle, extent=300)

        else:
            monCanvas.itemconfig(pacman_1, start=15+mod_angle, extent=330)

    if vit_x ==0 :
        if (monCanvas.itemcget(pacman_1, 'start') == '105.0' or monCanvas.itemcget(pacman_1, 'start') == '285.0') :
            monCanvas.itemconfig(pacman_1, start=120+mod_angle, extent=300)

        else:
            monCanvas.itemconfig(pacman_1, start=105+mod_angle, extent=330)

    monCanvas.move(pacman_1,vit_x,vit_y)
    modification2()

    if stop_animation == False :
        fen_princ.after(100, modification)

    else:
        stop_animation = False
        animation_active = False



def init_couleurs():         #fonction pour réinitialisé la couleur des boutons
    but_avance.config(bg="black")
    but_recule.config(bg="black")
    but_monte.config(bg="black")
    but_descend.config(bg="black")
    but_init.config(bg="red")
    but_arret.config(bg="red")



def droite_x (event):
    init_couleurs()         #réinitialise les couleurs
    but_avance.config(bg="blue")        #change à chaque fois la couleur du bouton utilisé

    global vit_x, vit_y, stop_animation

    stop_animation = False
    vit_x = 13              # se décale de 10 à droite
    vit_y = 0

    if animation_active == False :
        modification()      #se déplace


def gauche_x (event):
    init_couleurs()
    but_recule.config(bg="blue")

    global vit_x, vit_y, stop_animation

    stop_animation = False
    vit_x = -13             # se décale de 10 à gauche
    vit_y = 0

    if animation_active == False :
        modification()


def haut_y (event):
    init_couleurs()
    but_monte.config(bg="blue")

    global vit_x, vit_y, stop_animation

    stop_animation = False
    vit_x = 0
    vit_y = -13             # se décale de 10 en haut

    if animation_active == False :
        modification()


def bas_y (event):
    init_couleurs()
    but_descend.config(bg="blue")

    global vit_x, vit_y, stop_animation

    stop_animation = False
    vit_x = 0
    vit_y = 13              # se décale de 10 en en bas

    if animation_active == False :
        modification()



def point_depart():
    init_couleurs()
    but_init.config(bg="blue")

    global vit_x, vit_y, lose, vie, l_pac, compt, vie1, score1, pacman_1

    #lose.place_forget()
    vie1=110
    compt.config(text=vie1)

    score1=0
    score.config(text=score1)

    vit_x = 0       #vitesse nul
    vit_y = 0
    arret()

    monCanvas.coords(pacman_1,50,50,150,150)
    monCanvas.itemconfig(pacman_1,fill="yellow", start=15,extent=330)

    for i in range(len(l_pac)):
        x1=50+i*150
        x2=150+i*150
        monCanvas.coords(l_pac[i],x1,350,x2,450)
        monCanvas.itemconfig(l_pac[i], start=15,extent=330)

    monCanvas.coords(pomme,300,100,320,120)



def arret():        #fonction pour stopper le jeu
    init_couleurs()
    but_arret.config(bg="blue")

    global stop_animation

    stop_animation = True


def modification2():        #déplace le pacman ia
    global vit_x2, vit_y2,l_pac, List_vit


    if animation_active == True :

        for i in range(len(l_pac)):
            direction = randint(-20,100)
            #print(direction)

            if direction > 80 :
                if direction > 95 :

                    vit_x2 = 10     #droite
                    vit_y2 = 0

                elif direction > 90 :

                    vit_x2 = -10     #gauche
                    vit_y2 = 0

                elif direction > 85 :

                    vit_x2 = 0        #bas
                    vit_y2 = 10

                else:
                    vit_x2 = 0          #haut
                    vit_y2 = -10


                List_vit[i][0]=vit_x2
                List_vit[i][1]=vit_y2

            mod_angle = 0       #remet l'angle à 0

            liste_coord = monCanvas.coords(l_pac[i])        #situe le canvas

            #liste de conditions pour les rebonds sur les bords
            if liste_coord[2]>500 :
                vit_x2 = -10
                List_vit[i][0]=vit_x2

            elif liste_coord[0]<0 :
                vit_x2 =10
                List_vit[i][0]=vit_x2

            elif liste_coord[1]<0 :
                vit_y2 = 10
                List_vit[i][1]=vit_y2

            elif liste_coord[3]>600 :
                vit_y2 = -10
                List_vit[i][1]=vit_y2

            if (List_vit[i][0] <0 or List_vit[i][1]>0) :
                mod_angle = 180


            #anime la bouche qui s'ouvre lorsque le pacman ne change pas de direction

            if List_vit[i][1] == 0 :
                if (monCanvas.itemcget(l_pac[i], 'start') == '15.0' or monCanvas.itemcget(l_pac[i], 'start') == '195.0') :  #
                    monCanvas.itemconfig(l_pac[i], start=30+mod_angle, extent=300)

                else:
                    monCanvas.itemconfig(l_pac[i], start=15+mod_angle, extent=330)

            if List_vit[i][0] ==0 :
                if (monCanvas.itemcget(l_pac[i], 'start') == '105.0' or monCanvas.itemcget(l_pac[i], 'start') == '285.0') :
                    monCanvas.itemconfig(l_pac[i], start=120+mod_angle, extent=300)

                else:
                    monCanvas.itemconfig(l_pac[i], start=105+mod_angle, extent=330)


    #print(List_vit)
    for j in range(len(l_pac)):
        dir1 = 0+j*2
        dir2 = 1+j*2

        monCanvas.move(l_pac[j],List_vit[j][0],List_vit[j][1])  #déplace le pacman ia

        #print("tour")



def défaite ():     #affiche panneau défaite
    global lose
    #lose.place(x=100,y=100)
    arret()
    point_depart()


def pommier():
    global pomme
    L=[]
    for i in range(2):
        a=randint(0,500)
        L.append(a)

    #pomme.place(x=L[0],y=L[1])
    monCanvas.coords(pomme,L[0],L[1],L[0]+20,L[1]+20)


# ----------------------------------------------------------------

# Corps du programme

# ----------------------------------------------------------------

#fenêtre
fen_princ = Tk()
fen_princ.title("Bataille des Pacmans")
fen_princ.geometry("600x600")

#canvas terrain de jeu
monCanvas = Canvas(fen_princ, width=500, height=600, bg='ivory', bd=0, highlightthickness=0)
monCanvas.grid(row=0,column=0, padx=10,pady=10)

#pacman
pacman_1 = monCanvas.create_arc(50,50,150,150,fill="yellow",start=15,extent=330)

#pomme
pomme = monCanvas.create_oval(300,100,320,120,fill="red")

l_pac=[]
nb_ia=3     #nb d'ennemii (peut varier)

for i in range(nb_ia):
    x1=50+i*150
    x2=150+i*150

    l_pac.append(monCanvas.create_arc(x1,350,x2,450,fill="orange",start=15,extent=330))


#canvas boutons
zone2 = Frame(fen_princ, bg='#999999')
zone2.grid(row=0,column=1,ipadx=5)

#boutons déplacement et fonctions utiles
but_avance = Button(zone2, text="Droite", fg="yellow", bg="black")
but_recule = Button(zone2, text="Gauche", fg="yellow", bg="black")
but_monte = Button(zone2, text="Monte", fg="yellow", bg="black")
but_descend = Button(zone2, text="Descend", fg="yellow", bg="black")

but_arret = Button(zone2, text="STOP", fg="yellow", bg="red", command=arret)
but_init = Button(zone2, text="INIT", fg="yellow", bg="red", command=point_depart)

#regroupe les boutons en pack
but_avance.pack(fill=X)
but_recule.pack(fill=X)
but_monte.pack(fill=X)
but_descend.pack(fill=X)

but_arret.pack(fill=X)
but_init.pack(fill=X)

#raccourcies claviers
fen_princ.bind('<Up>', haut_y)
fen_princ.bind('<Down>', bas_y)
fen_princ.bind('<Left>', gauche_x)
fen_princ.bind('<Right>', droite_x)

#variable vie pacman
vie1=100
compt=Label(fen_princ,text=vie1, font=("Stencil",15,"bold"),fg="red", bg='ivory')
compt.place(x=530,y=175)

#score
score1=0
score=Label(fen_princ,text=score1, font=("Stencil",15,"bold"),fg="red", bg='ivory')
score.place(x=537,y=75)

lose=Label(fen_princ, text="t'es mort !",font=("Arial",19,"bold"), fg="sandy brown", width=21,heigh=11,bg="sea green")

List_vit=[]
for i in range(len(l_pac)):
    vit_x2 = -10
    vit_y2 = 0
    List_vit.append([vit_x2,vit_y2])


lab1=Label(fen_princ,text="Score :", font=("Bodoni MT",15,"bold"),fg="red", bg='ivory')
lab2=Label(fen_princ,text="Vie :", font=("Bodoni MT",15,"bold"),fg="red", bg='ivory')
lab1.place(x=517,y=30)
lab2.place(x=528,y=130)

fen_princ.mainloop()

