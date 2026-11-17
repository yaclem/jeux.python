# Créé par Clément, le 02/03/2022 en Python 3.7
from tkinter import *


def pendu(mot):
    rep=mot.lower()
    long=len(rep)

    if long>6:

    Grille=Canvas(fen1,width=700,height=300)
    Grille.place(x =100,y=100)

    for i in range(1,long+1):

        Grille.create_line(60*i,200,40+60*i,200,width=5, fill="royal blue")



##def pendu(mot):
##    mot=(" ")+mot
##    mot=mot.lower()
##    fin=mot
##    réponse=(" ")+("-"*(len(mot)-1))
##    space=mot.find(" ")
##
##    while space>=0:
##        réponse=réponse[:space]+" "+réponse[space+1:]
##        mot=mot[:space]+"*"+mot[space+1:]
##        space=mot.find(" ")
##    nbvie=5
##    letutlsé=""
##    manche=1
##    lettre=""
##    while (réponse!=fin) and ((" "+lettre)!=fin) and (nbvie!=0):
##        print("Manche",manche)
##        print ("lettres utilisées :", letutlsé)
##        print(réponse)
##        lettre=input("insérez la lettre choisi")
##        while (letutlsé.find(lettre))>=0 :
##            lettre=input("veuillez choisir une lettre inutilisée")
##        j=mot.find(lettre)
##        if len(lettre)==1:
##            if j>=0:
##                réponse=réponse[:j]+lettre+réponse[j+1:]
##                print(réponse)
##                print("gagné")
##                mot=mot[:j]+"*"+mot[j+1:]
##                j=mot.find(lettre)
##                while j>=0 :
##                    mot=mot[:j]+" "+mot[j+1:]
##                    réponse=réponse[:j]+lettre+réponse[j+1:]
##                    j=mot.find(lettre)
##            elif j<0:
##                nbvie=nbvie-1
##                print("perdu vous avez",nbvie,"vies")
##            letutlsé=letutlsé+lettre+"-"
##        manche=manche+1
##        print(" ")
##    return("MISSION PASSED")


#---------------------------main---------------------

fen1= Tk()
fen1.title("Pendu")
fen1.geometry("700x500")

#création label titre
titre=Label(fen1,text="Pendu",font=("Stencil",25,"bold"), fg="black",width=10,heigh=3)
titre.place(x=230,y=-20)


mot1="Couscous"
mot2="tome"
mot3="salamandre"
print(pendu(mot3))




fen1.mainloop()






##
##print("Bonjour, tu sais jouer au pendu ? Et bien c'est ce qu'on va voir...")
##
##print("LEVEL 1")
##print(pendu("Bonjour"))
##
##print("LEVEL 2")
##print(pendu("comment ca va"))
##
##print("LEVEL 3")
##print(pendu("kiwi"))
##
##print("T'as eu que de la chance réessaye pour voir")

