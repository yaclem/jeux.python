# Créé par Elève, le 18/10/2021 en Python 3.7
from random import randint

class Personnage:                       #init
    def __init__ (self,nom,vie):
        self.nom=nom
        self.vie=vie

    def combat(self,other):
        t=0
        while other.vie>0 and self.vie>0:
            t=t+1
            if t%2==1:
                print(self.nom,"avec",self.vie,"de vie, se prépare à attaquer contre",other.nom,"avec",other.vie,"vie, round",t)
                other.vie=degat(other.nom,other.vie)
            else:
                print(other.nom,"avec",other.vie,"de vie, se prépare à attaquer contre",self.nom,"avec",self.vie,"vie, round",t)
                self.vie=degat(self.nom,self.vie)
            print("-"*50)

#--------------affiche------------------------------------------------------------------------------

        if other.vie<=0:
            affiche_score(self.nom,other.nom,t)
        else:
            affiche_score(other.nom,self.nom,t)



def affiche_score(nom1,nom2,tour):                           #score
    print(nom2,"est mis K.O en",tour,"tours par",nom1)
    print(nom1,"sort vainqueur de ce duel")


def degat(nom,vie):                      #calcule dégât attaque
    crit=randint(1,10)
    if crit==1:
        degat=80
        print("Coup critique!!!")
    else:
        degat=randint(10,40)

    vie=vie-degat
    print(nom,"se prend un",degat,"de dégât en pleine tête")
    return vie



joueur1=Personnage("Tiplouf",100)
joueur2=Personnage("Pika-Pika",100)
Personnage.combat(joueur1,joueur2)

