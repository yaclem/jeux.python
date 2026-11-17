#Programme principal Jeu MASTERMIND par DUBREUIL Clement et DE ROTALIER Julien

from random import randint
from tkinter import *

# FONCTIONS
def Liste_Solution (Sol, Col): # fonction permettant afficher les boutons
    for i in range (5):
        Sol.append(Col[randint(0,5)])
    return Sol

print(Liste_Solution)


def Couleur_jouee(nbx):     # fonction permettant afficher les boutons pour selectioner la case et placer le pion de la couleur choisie
    global Tour_de_jeu, Couleur_pion, Etape_jeu, Coup_joue

    if Coup_joue<6 and Tour_de_jeu<11:


        for i in range (5):
            if Joueur[i]=="":                                           # creation et placement des boutons permettant de placer la couleur choisie
                Couleur_pion=Couleur[nbx]
                Bcase[i].config(text=str(i),bg=Couleur_pion)
                Bcase[i].place(x=26+i*40,y=528-40*(Tour_de_jeu-1))
        print("couleur choisie",Couleur_pion)

    else:
        Lab_err.config(text="La ligne est complete. Valider ou Annuler le dernier coup",fg='red',font="bold")


    Etape_jeu=2


def Couleur_placee(nbx):  # fonction placant le pion sur la case choisie
    global Tour_de_jeu, Couleur_pion, Etape_jeu, Coup_joue
    print(Tour_de_jeu)

    if Coup_joue<6 and Tour_de_jeu<11:
        Grille.create_oval(5 + nbx * 40, 408 - Tour_de_jeu * 40, 45 + nbx * 40, 448 - Tour_de_jeu * 40, fill=Couleur_pion)
        print("Case",nbx,"choisie")
        for i in range (5):
            Bcase[i].place_forget()
        Coup_joue=Coup_joue+1

        Joueur[nbx]=Couleur_pion



    else:
        Lab_err.config(text="La ligne est complete. Valider ou Annuler le dernier coup",fg='red',font="bold")

    Etape_jeu=1


def Annuler():
     global Tour_de_jeu,Etape_jeu,Ligne,Coup_joue


def Valider():
     global Tour_de_jeu,Blancs_Solution,Coup_joue,Couleur_pion

     print("joueur",Joueur)

     if Coup_joue<6 :
        Lab_err.config(text="La ligne est imcomplete. Completer la ligne avant de valider",fg='red',font="bold")
     else:
        Coup_joue=1
        nb_noirs=0     # initialise le nombre de pions de la bonne couleur et bien place
        nb_blancs=0    # initialise le nombre de pions de la bonne couleur et mal place

        for i in range (0,5):
            Solution2[i]=Solution[i]

        for i in range (0,5):
            if Joueur[i]==Solution2[i]:
                nb_noirs=nb_noirs+1
                Joueur[i]="x"
                Solution2[i]="y"
            else:
                nb_noirs=nb_noirs+0


        for i in range (0,5):
            for indice in range (0,5):
                if Joueur[i]==Solution2[indice]:
                    nb_blancs=nb_blancs+1
                    Joueur[i]="x"
                    Solution2[i]="y"
                else:
                    nb_blancs=nb_blancs+0



        if Tour_de_jeu==10 or  nb_noirs==5: # la partie est termine

            for j in range(6):               # Les boutons couleurs  sont effaces
                Bcouleur[j].place_forget()

            Annul.place_forget()
            Valid.place_forget()

            if nb_noirs==5:    # s'il y a 5 pions noirs le joueur a gagne
                print("Gagne !")
            else:
                #  Affichage des resultats de la ligne valide:


                Lab_err.config(text="Perdu ! Vous n'avez pas reussi a trouver la solution en 10 essais.",fg='red',font="bold")

            for j in range(6):                # Les boutons couleurs  sont effaces
                Bcouleur[j].place_forget()

            Annul.place_forget()
            Valid.place_forget()

        else:               #  Affichage des resultats de la ligne valide:

            Labresult[2*(Tour_de_jeu-1)].config(text=str(nb_noirs),bg='black',fg='white')
            Labresult[2*(Tour_de_jeu-1)+1].config(text=str(nb_blancs),bg='white',fg='black')

            print("il y a", nb_noirs, "de noir et", nb_blancs, "de blanc")
            print("Allez tente encore une fois")

        Tour_de_jeu=Tour_de_jeu+1       # Tour de jeu suivant

        for i in range(0,5):
            Joueur[i]=""         # la solution proposee par le joueur est reinitialisee pour le prochain tour de jeu



def Rejouer(nbx):      # permet la reinitialisation de l'ensemble des variables et de la grille a jouer
    global Tour_de_jeu, Coup_joue
    Etape_jeu=1
    Coup_joue=1
    print("Reinitialiser !")



#PROGRAMME PRINCIPAL

# declaration de la fenetre
fen1= Tk()
fen1.title("Jeu MASTER MIND ")
fen1.geometry("610x600")

# Creation d'un Canvas pour dessiner la grille de jeu
Grille=Canvas(fen1,width=510,height=600)
Grille.place(x =20,y=150)

#Lignes verticales  de la grille
for i in range (9):
    Grille.create_line(5+i*40,8,5+i*40,408,width=2)

#Lignes horizontales de la grille
for i in range (11):
    Grille.create_line(5,8+i*40,205,8+i*40,width=2)
    Grille.create_line(245,8+i*40,325,8+i*40,width=2)

# Variables
Tour_de_jeu=1     # La variable tour de jeu compte le nombre de tour de jeu elle permet d'arreter la partie si il n'y a aucun gagnant au bout de 10 tours.
Couleur=["red","yellow","green","blue","purple","orange"] # liste des couleurs jouables
Solution=[]             # Liste contenant la solution à  determiner
Tab_Rond=[]             # liste contenant tous les pions affichés utilisé pour l'annulation de coup joué et la réinitialisation du jeu
Ligne=[0,0,0,0,0]       # liste utilisée pour placer les pions sur le ligne de jeu du joueur
Etape_jeu=1
Coup_joue=1
Joueur=["","","","",""]             # tableau comprenant la solution proposée apr la joueur
Blancs_Joueurs=["","","","",""]     # tableau utilise pour determiner le nb de pions blancs associe a la proposition du joueur
Blancs_Solution=[" "," "," "," "," "]    # tableau utilise pour determiner le nb de pions blancs associe a la proposition du joueur -- cette liste contiendra la solution moins les pions noirs trouve par le joueur
Bcouleur=[]         # Liste pour les boutons de selection de la couleur
Bcase=[]
Labresult=[]        # cette liste comprendra les resultats des lignes validees par le joueur (nb de pions noirs et de pions blancs par ligne validée)
Solution2=["","","","",""]

for i in range (51): #creation d'un tabeau contenant les disques de couleur représentant la ligne jouee-- utilisée pour effacer les derniers coups joués sur une ligne
     Tab_Rond.append(Grille.create_oval(5,8,5,8,fill="grey"))


Solution=Liste_Solution(Solution,Couleur)
print(Solution)     # cette ligne a pour seule object de visualiser au niveau de la console, la solution a determiner afin d'operer les tests du jeu


for i in range (6):     # creation et placement des boutons de couleur
    Bcouleur.append(Button(fen1,text="",width=4,bg=Couleur[i],command= lambda x=i : Couleur_jouee(x)))
    Bcouleur[i].place(x=360+i*40,y=488)

for i in range (5):     # creation et placement des boutons permettant de placer la couleur choisie
    Bcase.append(Button(fen1,text="",width=4,command= lambda x=i : Couleur_placee(x)))

for i in range (20):
    Labresult.append(Label(fen1,text=""))

for i in range (10):
    Labresult[2*i].place(x=275,y=528-i*40)
    Labresult[2*i+1].place(x=315,y=528-i*40)

Label0 = Label(fen1,text="Determiner les pions de couleurs choisis aleatoirement",font="bold")

Lab_err = Label(fen1,text=" ")

Rejoue=Button(fen1, text="Rejouer", fg="green", command=Rejouer)
Valid=Button(fen1, text="Valider", fg="blue", command=Valider)      # Bouton "Valider" permettant de valider la ligne jouee
Quit=Button(fen1, text="Quitter", fg="Red", command=fen1.destroy)   # Bouton "Quitter" permettant de fermer la fenetre
Annul=Button(fen1, text="Annuler", fg="pink", command=Annuler)

# positionnement des widgets Labels et du bouton Quitter
Label0.place(x=10,y=0)

Lab_err.place(x=160,y=560)

Valid.place(x=370,y=530)
Rejoue.place(x=425,y=530)
Annul.place(x=485,y=530)
Quit.place(x=545,y=530)     #Positionnement du bouton quitter
     #Positionnement du bouton Rejouer

fen1.mainloop()