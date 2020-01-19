#! /usr/bin/python3
import sys,random,tkinter


#initialisation de la grille avec des nombres aléatoires
grille=[[0]*4 for i in range(4)]            #génere une grille 4*4 avec des 0 partout (4 '0' pour i de 0 a 3)
for i in range(4):
    for j in range(4):
        grille[i][j]=random.randint(0,3)
        print(grille[i][j],end='')
    print("")    

print("<--------------------->")
def DejaPres(x,y,grille):                   #fonction qui vérifie si une cellule a un valeur déja présente en horizontale et verticale (=sudoku)
    for i in range(len(grille[0])):
        if(i!=x and grille[i][y]==grille[x][y]):
            grille[x][y]='\0'
            return 1
    for j in range(len(grille[0])):
        if(j!=y and grille[x][j]==grille[x][y]):
            grille[x][y]='\0'
            return 1
    return 0        
    
for i in range(4):
    for j in range(4):
        DejaPres(i,j,grille)
        print(grille[i][j],end='')
    print("")    