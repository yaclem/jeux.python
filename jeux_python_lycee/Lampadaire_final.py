# Créé par Elève, le 03/02/2022 en Python 3.7
from tkinter import *


def Cliquer(nb):
    global compteur


    prog=""
    if L[nb]>10:
        prog="alpha"
    else:
        prog="beta"


    quotient=nb//8
    reste=nb%8

    for i in range (64):
        quotient2=i//8
        reste2=i%8

        dif1 = quotient2-quotient
        dif2 = reste2-reste

        if dif1==0 or dif2==0 or dif1==dif2 or dif1==dif2*(-1):
            change_bouton(i,prog)


    change_etat_bouton(prog,nb)
    compt.config(text=compteur)

    if compteur>=8:
        victoire()


def change_bouton(i,prog):
    if prog=="beta":
        L[i]=L[i]+1
        Tbbouton[i].config(bg="yellow", state="disabled")

    else:
        L[i]=L[i]-1
        if L[i]==0:
            Tbbouton[i].config(bg="sea green", state="normal")


def change_etat_bouton(prog,nb):
    global compteur

    if prog=="alpha":
        L[nb]=L[nb]-20      #état désactivé
        Tbbouton[nb].config(bg="sea green",state="normal")
        compteur=compteur-1


    else:
        L[nb]=L[nb]+20      #état activé
        Tbbouton[nb].config(bg="orange",state="normal")
        compteur=compteur+1




def victoire():
    global list_label
    vict=Label(fen1, text="Bravo c'est gagné !",font=("Arial",19,"bold"), fg="sandy brown", width=21,heigh=11,bg="sea green")
    vict.place(x=90,y=115)
    list_label.append(vict)



def Rejouer():
    global compteur,list_label
    compteur=0
    compt.config(text=compteur)
    for i in range (64):
        Tbbouton[i].config(bg="sea green", state="normal")
        L[i]=0

    nb=len(list_label)      #jsp pk ça +1
    for i in range(nb):
        list_label[i].destroy()



def Quitter():
    fen1.destroy()


#==========================Main================================

fen1= Tk()
fen1.title("Problème des huit dames")
fen1.geometry("700x500")
fen1.config(bg='peach puff')

L=[0 for i in range(64)]            #etat des boutons

compteur=0
Tbbouton=[]        #liste avec les boutons
list_label=[]

#place les boutons
for i in range (64):
    Tbbouton.append(Button(fen1,text="",width=4,heigh=2,bg="sea green",command= lambda x=i : Cliquer(x) ))
    Tbbouton[i].place(x=90+40*(i%8),y=117+40*(i//8))



#label titre
titre=Label(fen1,text="Problème des huit dames",font=("Stencil",23,"bold"), fg="DarkOrange4",width=22,heigh=3, bg='peach puff')
titre.place(x=130,y=-10)

#label compteur
compt=Label(fen1,text=compteur, font=("Stencil",45,"bold"),fg="orange3", bg='peach puff')
compt.place(x=540,y=150)


#place les boutons spéciaux
b_rejouer=(Button(fen1,text="Rejouer",font=("Arial",11,"bold"), fg="DarkOrange4",width=8,heigh=3,bg="sienna1",command= Rejouer  ))         #bouton rejouer
b_rejouer.place(x=470,y=290)

b_quitter=(Button(fen1,text="Quitter",font=("Arial",11,"bold"), fg="DarkOrange4",width=8,heigh=3,bg="sienna1",command= Quitter ))          #bouton quitter
b_quitter.place(x=570,y=290)

b_cheat=(Button(fen1,width=2,heigh=1,relief='flat',bg='peach puff',command= victoire ))          #bouton victoire
b_cheat.place(x=570,y=400)



#droit d'auteur
droit=Label(fen1,text="©clem_compagnie",font=("Century",8,"bold"), fg="DarkOrange4",width=14,heigh=4,bg='peach puff')
droit.place(x=580,y=450)


fen1.mainloop()

