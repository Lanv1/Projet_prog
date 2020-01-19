#! /usr/bin/python3
import sys,random
from tkinter import *
import tkinter.font as tkFont


grille=[[0]*4 for i in range(4)] #grille de 4*4 initialisée a 0
fenetre=Tk()
myFont=tkFont.Font(size=20)
# fenetre.geometry("800x500")


# Affichage de la grille
for i in range(4):
    for j in range(4):
        grille[i][j]=Entry(fenetre,width=5,font=myFont,justify=CENTER)
        grille[i][j].grid(column=i,row=j)
        grille[i][j].insert(0,i+j)

win=0

fenetre.mainloop()