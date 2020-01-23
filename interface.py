#! /usr/bin/python3
import sys,random
from tkinter import *
import tkinter.font as tkFont


grille=[[0]*4 for i in range(4)] #grille de 4*4 initialisée a 0, sera composée d'entry
grilleLi=[[0]*4 for i in range(4)] #copie de la grille, c'est une liste avec les valeurs de la grille
fenetre=Tk()
myFont=tkFont.Font(size=20)
# fenetre.geometry("800x500")

def DejaPres(x,y,grille,Entry):                   #fonction qui vérifie si une cellule a un valeur déja présente en horizontale et verticale (=sudoku)
    for i in range(4):
        if(i!=x and grille[i][y]==Entry.get()):
            Entry.configure({"background":"red","fg":"white"})
            return 1
    for j in range(4):
        if(j!=y and grille[x][j]==Entry.get()):
            Entry.configure({"background":"red","fg":"white"})
            return 1
    return 0        
    

# Affichage de la grille
for i in range(4):
    for j in range(4):
        grille[i][j]=Entry(fenetre,width=5,font=myFont,justify=CENTER)  # grille est la liste des entry(champs)
        grille[i][j].grid(column=i,row=j)                               # interface de la grille
        grille[i][j].insert(1,random.randint(0,3))                      # test en complétant la grille en entier avec des entiers random entre 0 et 3
        grilleLi[i][j]=grille[i][j].get()
        DejaPres(i,j,grilleLi,grille[i][j])

print(grilleLi)
win=0

fenetre.mainloop()