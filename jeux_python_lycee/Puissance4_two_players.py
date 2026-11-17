# Créé par Elève, le 21/02/2022 en Python 3.7
from tkinter import *
from PIL import Image, ImageTk
from random import *

'''
Programme Puissance 4, avec partie contre ia et partie multi
Problèmes à résoudre:
    -donne 4 points lorsque le puissance 4 est à l'horizontale
    -réalise des puissances 4 en comptant les bords de chaque côté (ex: 12,20,28,36)
Eventuelles améliorations:
    -ia moyen et difficile
    -mettre la ligne de pions vicotieux en surlignage

'''

def Cliquer(nb):
    global Tb_rond, list_haut, List_état, couleur,jouer

    if jouer=="actif":
#=======================mode multi=====================================
        if mode4=="actif":
            hauteur=list_haut[nb]      #calcule la hauteur inversé
            if hauteur >= 0:
                coord = hauteur*7+nb        #calcule position

                if couleur==1:  #joueur1
                    Tb_rond.append(Grille.create_oval(40*(nb+1),40*(hauteur+1),40*(nb+2),40*(hauteur+2), fill="red3"))       #place les ronds

                    List_état[coord]=1                  #change l'état
                    list_haut[nb]=list_haut[nb]-1       #modifie la hauteur
                    verif_victoire(coord,couleur)       #test jetons
                    couleur=2                           #change de joueur
                else:
                    Tb_rond.append(Grille.create_oval(40*(nb+1),40*(hauteur+1),40*(nb+2),40*(hauteur+2), fill="goldenrod1"))

                    List_état[coord]=2
                    list_haut[nb]=list_haut[nb]-1
                    verif_victoire(coord,couleur)
                    couleur=1


#=======================mode ia=====================================
        else:
            hauteur=list_haut[nb]
            if hauteur >= 0:
                if couleur==1:
                    coord = hauteur*7+nb

                    Tb_rond.append(Grille.create_oval(40*(nb+1),40*(hauteur+1),40*(nb+2),40*(hauteur+2), fill="red3"))

                    List_état[coord]=1
                    list_haut[nb]=list_haut[nb]-1
                    verif_victoire(coord,couleur)
                    couleur=2

                    #==========tour de l'ia============
                    if mode1=="actif":
                        nb2=ia_facile()
                    elif mode2=="actif":
                        nb2=ia_moyen()
                    elif mode3=="actif":
                        nb2=ia_difficile()

                    print("nombre choisi = ",nb2)

                    hauteur2=list_haut[nb2]
                    coord2 = hauteur2*7+nb2
                    print ("coordonnée de 0-41 =",coord2)

                    Tb_rond.append(Grille.create_oval(40*(nb2+1),40*(hauteur2+1),40*(nb2+2),40*(hauteur2+2), fill="goldenrod1"))

                    List_état[coord2]=2
                    list_haut[nb2]=list_haut[nb2]-1
                    verif_victoire(coord2,couleur)
                    couleur=1



def ia_facile():        #ia choisissant aléatoirement un emplacement
    global list_haut

    list_possib_ia=[i for i in range(7)]
    erreur=[]

    for i in range(len(list_haut)):
        if list_haut[i] < 0:
            erreur.append(i)
    print("liste erreur =",erreur)

    if erreur!=[]:
        for i in range(len(erreur)):
            del list_possib_ia[erreur[i]]

    print("liste possible nb =",list_possib_ia)
    al=randint(0,len(list_possib_ia)-1)
    nb=list_possib_ia[al]

    return nb


def ia_moyen():
    global List_état

    for i in range(3,39,7):
        test_empla(i,couleur)

    for i in range(14,28,1):
        pass




def ia_difficile():
    pass


def verif_victoire(coord,couleur):      #test les jetons adjacents (3 avants, 3 après)
    global List_état,nb

    for i in range(-4,5,1):     #horizontal
        test = coord + i
        test_empla (test,couleur)
    nb=0

    for i in range(-28,29,7):     #vertical
        test = coord + i
        test_empla (test,couleur)
    nb=0

    for i in range(-32,33,8):     #diagonal /
        test = coord + i
        test_empla (test,couleur)
    nb=0

    for i in range(-24,25,6):     #diagonal \
        test = coord + i
        test_empla (test,couleur)
    nb=0


def test_empla (test,couleur):     #compte le nb de jetons successivement alignés
    global nb,liste_vict

    if nb==4 :
        print(liste_vict)
        victoire(couleur)
    elif test > 41 or test < 0:
        nb=0
        liste_vict=[]
    else:
        if List_état[test]==couleur:
            nb+=1
            liste_vict.append(test)
        else:
            nb=0


def victoire(coul):     #affiche panneau victoire
    global résultat, jouer, vict_joueur, vict_joueur1, vict_joueur2, Joueur1, Joueur2


    if coul == 1:
        résultat.config(text=(Joueur1,"victorieux"),font=("Century",15,"bold"), fg="red")
        label_img2.config(image = photo2)

        vict_joueur[0]=vict_joueur[0]+1
        vict_joueur1.config(text=(Joueur1,"=",vict_joueur[0]))

    else :
        résultat.config(text=(Joueur2,"victorieux"),font=("Century",15,"bold"), fg="goldenrod1")
        label_img3.config(image = photo3)

        vict_joueur[1]=vict_joueur[1]+1
        vict_joueur2.config(text=(Joueur2,"=",vict_joueur[1]))

    jouer="nul"


def victoire_cheat():       #test victoire
    global résultat,jouer,label_img

    résultat.config(text="Clément gagne bien sûr",font=("Century",15,"bold"), fg="blue")
    label_img1.config(image = photo1)
    jouer="nul"


def Rejouer():      #fonction restart
    global List_état, list_haut, Tbbouton, Tb_rond, couleur,résultat,jouer

    while Tb_rond!=[]:
        Grille.delete(Tb_rond.pop())

    List_état=[0 for i in range(42)]    #liste état grille
    list_haut=[5 for i in range(8)]     #liste état hauteur colonne
    Tbbouton=[]     #liste bouton
    Tb_rond=[]      #liste rond
    couleur=1
    nb=0
    liste_vict=[]
    jouer="actif"

    résultat.config(text="")
    label_img1.config(image = "")
    label_img2.config(image = "")
    label_img3.config(image = "")


def Quitter():      #fonction leave
    fen1.destroy()


def difficult (x):      #choisi le mode de jeu et ferme les fenetres
    global diff,mode1,mode2,mode3,mode4
    txtacceuil.place_forget()
    txtdiff.place_forget()
    difficult1.place_forget()
    difficult2.place_forget()
    difficult3.place_forget()
    multi.place_forget()

    if x==1:
        mode1="actif"

    elif x==2:
        mode2="actif"

    elif x==3:
        mode3="actif"

    elif x==10:
        mode4="actif"

#====================Main===============================

fen1= Tk()
fen1.title("Puissance 4")
fen1.geometry("700x500")
fen1.config(bg='skyblue')

#création label titre
titre=Label(fen1,text="Puissance 4",font=("Stencil",25,"bold"), fg="blue3",width=10,heigh=3,bg='skyblue')
titre.place(x=184,y=-20)


#valeur
List_état=[0 for i in range(42)]    #liste état grille
list_haut=[5 for i in range(7)]     #liste état hauteur colonne

Tbbouton=[]     #liste boutons
Tb_rond=[]      #liste ronds
couleur=1       #joueur1

nb=0                #variable test (long/haut/diag1/diag2)
jouer="actif"       #variable de lancement du  jeu

liste_vict=[]       #emplacement pions puissance 4
vict_joueur=[0,0]       #nb de victoire par joueur


Joueur1="Joueur1"       #nom joueur
Joueur2="Joueur2"


#création grille
Grille=Canvas(fen1,width=400,height=500)
Grille.place(x =100,y=100)
Grille.config(bg='skyblue',highlightbackground='skyblue')

for i in range (8): #vertical
    Grille.create_line(40+i*40,38,40+i*40,283,width=7, fill="royal blue")

for i in range(7):  #horizontal
    Grille.create_line(38,40+i*40,323,40+i*40,width=7, fill="royal blue")


#création boutons
for i in range (7):
    Tbbouton.append(Button(fen1,text="",width=4,heigh=2,bg="DodgerBlue2",command= lambda x=i : Cliquer(x) ))        #bouton à cliquer
    Tbbouton[i].place(x=140+40*(i%8),y=80+40*(i//8))

b_rejouer=(Button(fen1,text="Rejouer",font=("Arial",11,"bold"), fg="royal blue",width=8,heigh=3,bg="paleturquoise",command= Rejouer  ))         #bouton rejouer
b_rejouer.place(x=470,y=290)

b_quitter=(Button(fen1,text="Quitter",font=("Arial",11,"bold"), fg="royal blue",width=8,heigh=3,bg="paleturquoise",command= Quitter ))          #bouton quitter
b_quitter.place(x=570,y=290)

b_cheat=(Button(fen1,width=2,heigh=1,relief='flat',bg='skyblue',command= victoire_cheat ))          #bouton victoire
b_cheat.place(x=570,y=400)


#création label résultat
résultat=Label(fen1,width=20,heigh=6,text="",bg='skyblue')
résultat.place(x=425,y=40)


#placer images victoire
load1 = Image.open("images/troll_face.png")
load1.thumbnail((110,110))   #largeur/hauteur
photo1 = ImageTk.PhotoImage(load1)

load2 = Image.open("images/magicarpe.png")
load2.thumbnail((120,120))
photo2 = ImageTk.PhotoImage(load2)

load3 = Image.open("images/pikachu.png")
load3.thumbnail((130,130))
photo3 = ImageTk.PhotoImage(load3)


#label image victoire
label_img1 = Label(fen1, bg='skyblue')
label_img1.place(x=500 , y=160)

label_img2 = Label(fen1, bg='skyblue')
label_img2.place(x=520 , y=140)

label_img3 = Label(fen1, bg='skyblue')
label_img3.place(x=515 , y=142)


#compteur victoire
vict_joueur1=Label(fen1,text=(Joueur1,"=",vict_joueur[0]),font=("Century",12,"bold"), fg="goldenrod1",width=12,heigh=3,bg='red3')
vict_joueur1.place(x=130,y=410)

vict_joueur2=Label(fen1,text=(Joueur2,"=",vict_joueur[1]),font=("Century",12,"bold"), fg="red3",width=12,heigh=3,bg='goldenrod1')
vict_joueur2.place(x=290,y=410)



#droit d'auteur
droit=Label(fen1,text="clem_compagnie",font=("Century",8,"bold"), fg="darkblue",width=14,heigh=4,bg='skyblue')
droit.place(x=580,y=450)


#fenêtre début difficultés
txtacceuil=Label(fen1,font=("Arial",15,"bold"),width=60,heigh=33,bg='white', text="Bienvenue dans le Puissance 4, \n Le but du jeu ? c'est juste d'aligner 4 jetons  \n \n Vous pourrez ainsi choisir oÃ¹ placer vos pions pour gagner \n Attention à que votre adversaire ne fasse pas de mÃªme... ")
txtacceuil.place(x=0,y=-250)


difficult1=Button(fen1, text="Facile", fg="black", bg="green",font=("Arial",25,"bold"),command= lambda x=1 : difficult(x))
difficult2=Button(fen1, text="Normal", fg="black", bg="orange",font=("Arial",25,"bold"),command= lambda x=2 : difficult(x))
difficult3=Button(fen1, text="Difficile", fg="black", bg="red",font=("Arial",25,"bold"),command= lambda x=3 : difficult(x))
multi=Button(fen1, text="Multijoueur", fg="black", bg="skyblue3",font=("Arial",25,"bold"),command= lambda x=10: difficult(x))

difficult1.place(x=120,y=300)
difficult2.place(x=270,y=300)
difficult3.place(x=440,y=300)
multi.place(x=240,y=390)


txtdiff=Label(fen1,text="Choisissez maintenant le niveau de difficulte : ", fg=("blue"),font=("Arial",15,"bold"))
txtdiff.place(x=130,y=250)

#type de mode de jeu
mode1="down"        #ia facile
mode2="down"        #ia moyenne
mode3="down"        #ia dure
mode4="down"        # multi



fen1.mainloop()
