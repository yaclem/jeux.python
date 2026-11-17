# Créé par Elève, le 08/02/2022 en Python 3.7
from tkinter import *
from random import randint
from PIL import Image, ImageTk



class carre ():                             #fonction carré
    def __init__(self, Liste_position, L_pos_tab2):
        self.c1 = Liste_position[0]         #4 positions des 4 carrés (1 pos= [4 coordonnées])
        self.c2 = Liste_position[1]
        self.c3 = Liste_position[2]
        self.c4 = Liste_position[3]


        self.a = L_pos_tab2[0]              # indice des positions des 4 carrés dans le 2e tableau)
        self.b = L_pos_tab2[1]
        self.c = L_pos_tab2[2]
        self.d = L_pos_tab2[3]




    def destruction(self):
        global Liste_carre

        for i in range(4):
            Grille.delete(Liste_carre.pop())




    def  creation(self,Liste_position):         #  créer les carrés
        global Liste_carre
        global coul_al

        Liste_carre.append(Grille.create_rectangle(self.c1[0], self.c1[1], self.c1[2], self.c1[3], fill=coul_al))      #créer
        Liste_carre.append(Grille.create_rectangle(self.c2[0], self.c2[1], self.c2[2], self.c2[3], fill=coul_al))
        Liste_carre.append(Grille.create_rectangle(self.c3[0], self.c3[1], self.c3[2], self.c3[3], fill=coul_al))
        Liste_carre.append(Grille.create_rectangle(self.c4[0], self.c4[1], self.c4[2], self.c4[3], fill=coul_al))

        Liste_position=[self.c1, self.c2, self.c3, self.c4]     # nouvelle positions



# [gauche,haut,droite,bas]
# dimension tableau : min= [40, 40, 80, 80] , max= [8*40=320 , 14*40=560, 9*40=360, 15*40=600]

    def déplacement_bas (self):
        global Liste_etat
        global L_pos_tab2
        global destruct

        if self.c1[3] == 560 or Liste_etat[self.c+8]==1 or Liste_etat[self.d+8]==1 :        #haut_g / bas
            L_pos_tab2=[self.a, self.b, self.c, self.d]

            destruct=0

            Pose_tab2 (L_pos_tab2)

            Début()

        else:

            for i in range(1,4,2):
                self.c1[i] += 40        #change coordonnées carrés tableau 1
                self.c2[i] += 40
                self.c3[i] += 40
                self.c4[i] += 40

            self.a+=8                   #change coordonnées carrés tableau 2
            self.b+=8
            self.c+=8
            self.d+=8
            L_pos_tab2=[self.a, self.b, self.c, self.d]

            self.destruction()

            self.creation(Liste_position)



    def déplacement_gauche (self):
        global Liste_etat
        global L_pos_tab2
        global destruct

        if self.c1[0] > 40 and Liste_etat[self.a-1]==0 and Liste_etat[self.c-1]==0 :    #haut_g / gauche
            for i in range(0,3,2):
                self.c1[i] -= 40
                self.c2[i] -= 40
                self.c3[i] -= 40
                self.c4[i] -= 40

            self.a-=1                   #change coordonnées carrés tableau 2
            self.b-=1
            self.c-=1
            self.d-=1
            L_pos_tab2=[self.a, self.b, self.c, self.d]

            self.destruction()

            self.creation(Liste_position)



    def déplacement_droit (self):
        global Liste_etat
        global L_pos_tab2
        global destruct

        if self.c1[2] < 320 and Liste_etat[self.b+1]==0 and Liste_etat[self.d+1]==0 :             #haut_g / droite
            for i in range(0,3,2):
                self.c1[i] += 40
                self.c2[i] += 40
                self.c3[i] += 40
                self.c4[i] += 40

            self.a+=1                   #change coordonnées carrés tableau 2
            self.b+=1
            self.c+=1
            self.d+=1

            L_pos_tab2=[self.a, self.b, self.c, self.d]

            self.destruction()

            self.creation(Liste_position)




#=========================Definition============================


def Début ():       #lancement du jeu
    global forme_al
    global Liste_position
    global L_pos_tab2
    global coul_al


    Test_ligne()
##    nb=randint(0,6)
##    forme_al=Forme[nb]
##    print (forme_al)
    forme_al=Forme[3]

    nb2=randint(0,len(List_couleur)-1)
    coul_al=List_couleur[nb2]


    if forme_al=="carre" :
        Liste_position= [[160, 40, 200, 80],[160, 80, 200, 120],[200, 40, 240, 80],[200, 80, 240, 120]]
        L_pos_tab2=[3,4,11,12]

        carré_class = carre(Liste_position ,L_pos_tab2)
        carré_class.creation(Liste_position)





def Pose_tab2 (L_pos_tab2):        # change de 0 à 1 les positions du carré
    global Liste_etat

    for i in range(4):
        Liste_etat[L_pos_tab2[i]]=1




def Test_ligne():
    global Liste_etat

    L2_add=0
    Ligne=0

    for j in range(14):
        L2_add=0
        compt=8*j

        for i in range(8):
            nbre = i+compt
            L2_add += Liste_etat[nbre]

        if L2_add == 8:
            Ligne=1

    print(Ligne)

    L2_add=0
    Ligne=0





#==================Clique_direction=======================

def Clique_bas(event):
    global forme_al

    if forme_al=="carre" :
        carré_class = carre(Liste_position, L_pos_tab2)
        carré_class.déplacement_bas()



def Clique_gauche(event):
    global forme_al

    if forme_al=="carre" :
        carré_class = carre(Liste_position, L_pos_tab2)
        carré_class.déplacement_gauche()



def Clique_droit(event):
    global forme_al


    if forme_al=="carre" :
        carré_class = carre(Liste_position ,L_pos_tab2)
        carré_class.déplacement_droit()





#====================Bouton=================================

def Rejouer():
    global forme_al, Liste_carre, Liste_position, destruct, Liste_etat, L_pos_tab2, coul_al

    if Liste_carre!=[]:
        while Liste_carre!=[]:
            Grille.delete(Liste_carre.pop())

    forme_al=""
    coul_al=""
    Liste_carre=[]
    Liste_position=[]
    destruct=0
    Liste_etat = [0 for i in range(112)]
    L_pos_tab2=[]

    Grille.delete("rectangle")


    print ("Redémarage")



def Quitter():
    fen1.destroy()


#==========================Main================================

fen1= Tk()
fen1.title("Tetris")
fen1.geometry("700x700")

Forme=["barre","l","l_inverse","carre", "s","s_inverse", "t_inverse"]


##
##file1 = "E:\\Projet_tetris\\Nsi codage pro\\Paonhéron des grandes oeuvres\\Projet_tetris\\The_Tetris_Company_Logo.png"
##
##img = PhotoImage(file=file1)
##
##canvas=Canvas(fen1,width=400,height=500)
##canvas.create_image(250, 250, image=img)



#============================carré variable=====================================

forme_al=""         #forme tirée aléatoirement
coul_al=""
Liste_carre=[]          #liste des carrés
Liste_position=[]       #liste des coordonnées des carrés 1


Liste_etat = [0 for i in range(112)]        #tableau2

L_pos_tab2=[]       #liste positions des carrés tableau 2


#=======================Tableau 2 trié================


#=====================Couleur========================


List_couleur=["tomato","aquamarine","salmon","light goldenrod","blueviolet","chartreuse","purple"]

#====placer les grilles=====

Grille=Canvas(fen1,width=510,height=600)
Grille.place(x =80,y=30)

for i in range (10):
    Grille.create_line(i*40,40,i*40,600,width=2)

for i in range(17):
    Grille.create_line(40,i*40,360,i*40,width=2)


#====Commandes flèche directionnelles=======

fen1.bind('<Down>', Clique_bas)

fen1.bind('<Left>', Clique_gauche)

fen1.bind('<Right>', Clique_droit)



#=========Commandes Boutons==============

b_debut=(Button(fen1,text="Start",width=15,heigh=3,bg="paleturquoise",command= Début  ))
b_debut.place(x=530,y=330)

b_rejouer=(Button(fen1,text="Rejouer",width=5,heigh=2,bg="paleturquoise",command= Rejouer  ))
b_rejouer.place(x=530,y=400)

b_quitter=(Button(fen1,text="Quitter",width=5,heigh=2,bg="paleturquoise",command= Quitter ))
b_quitter.place(x=600,y=400)



fen1.mainloop()