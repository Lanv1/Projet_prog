#! /usr/bin/python3
import sys,random


#initialisation de la grille avec des nombres aléatoires
#Faire l'implémentation de la grille finale: les valeurs son 1 ligne, colonne sur 2. FAIT
#Implémentation dans la classe cell pour les contraintes > ou < grace a cette grille.
#
print("<--------------------->")
def AfficheG(grille,D):
    for i in range(D):
        for j in range(D):
            print(grille[i][j],end='')
        print("")
def GenRandGrille(grille,D):
    compteConst=0
    for i in range(D):              
        for j in range(D):
            if(i%2==0 and j%2==0):  #case où l'on peut mettre une valeur
                if(random.randint(0,1)):
                    grille[i][j]=random.randint(1,((D+1)/2))
                    DejaPres(i,j,grille)
            elif((i%2!=0 or j%2!=0) and compteConst<5):
                if(random.randint(0,1)):
                    grille[i][j]=">"
                    compteConst+=1


def DejaPres(x,y,grille):                   #fonction qui vérifie si une cellule a un valeur déja présente en horizontale et verticale (=sudoku)
    for i in range(0,len(grille[0]),2):
        if(i!=x and grille[i][y]==grille[x][y]):
            grille[x][y]=0
            return 1
    for j in range(0,len(grille[0]),2):
        if(j!=y and grille[x][j]==grille[x][y]):
            grille[x][y]=0
            return 1
    return 0        

def Chercher_case_vide(grille,i,j,D):
    for i in range(0,len(grille[0]),2):
        for j in range(0,len(grille[0]),2):
            if(grille[i][j]==0):
                return(i,j,True)
    return(i,j,False)
        
  
   

def Peut_etre_attr(grille,x,y,val):
    for i in range(0,len(grille[0]),2):
        if(i!=x and grille[i][y]==val):
            return 0
    for j in range(0,len(grille[0]),2):
        if(j!=y and grille[x][j]==val):
            return 0
    return 1        


def Solveur(grille,D,Dval):
    i=j=0
    if (not Chercher_case_vide(grille,i,j,D)[2]):
        return True
    i=Chercher_case_vide(grille,i,j,D)[0]
    j=Chercher_case_vide(grille,i,j,D)[1]
    TabCell[i][j]=Cell(Dval,i,j)           #tableau de cellules pour acceder aux possibilitées propres a chaque case de la grille
    TabCell[i][j].update(grille)
    if(TabCell[i][j].nbrChoix()==1):
        grille[i][j]=TabCell[i][j].ChoixUnique()
        #print("BRAVO")
        if(Solveur(grille,D,Dval)):
            return True
    for val in TabCell[i][j].ListeChoix():         #on cherche les valeurs uniquement dans les possibilités calculées avant avec la méthode
        if(Peut_etre_attr(grille,i,j,val)):
            grille[i][j]=val
            if(Solveur(grille,D,Dval)):
                return True
            grille[i][j]=0
    return False

###########################################################
class Cell:
    taille=0
    def __init__(self,diff,x,y):
        self.choix=[0 for i in range(diff)]
        k=0
        while(k<=(diff-1)):
            self.choix[k]=1
            k+=1
        self.taille=diff
        self.abs=x
        self.ord=y

    def nbrChoix(self):
        som=0
        for i in range(self.taille):
            if self.choix[i]:
                som+=1
        return som

    def update(self,grille):
        for i in range(0,self.taille,2):                    
            if(i!=self.abs and grille[i][self.ord]!=0):
                self.choix[grille[i][self.ord]-1]=0
        for j in range(0,self.taille,2):
            if(j!=self.ord and grille[self.abs][j]!=0):
                self.choix[grille[self.abs][j]-1]=0
    
    def ChoixUnique(self):
        u=0
        if(self.nbrChoix()==1):
            while(self.choix[u]==0):
                u+=1
            return u+1

    def AfficheChoix(self):
        for i,e in enumerate(self.choix):
            if (e!=0):
                print(i+1,end="")
        print("") 

    def ListeChoix(self):
        Lc=list()
        for i,e in enumerate(self.choix):
            if e==1:
                Lc.append(i+1)    #car la cellule 0 correspond a la valeur 1
        return Lc
###########################################################""   

D=(2*int(sys.argv[1])-1) #pour initialiser la grille avec les >,<
Dval=int(sys.argv[1])   #pour avoir la liste des valeurs que les cellules peuvent prendre


grille=[[0]*D for i in range(D)]            #génere une grille 4*4 avec des 0 partout (4 '0' pour i de 0 a 3)
TabCell=[[0]*D for i in range(D)]   
# TestG=[[0,6,0,0,0,0,0,1,0],[4,0,0,7,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,3,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,7,0,0],[0,0,0,0,0,0,0,8,0],[0,0,0,0,0,0,0,0,0],[5,0,0,0,0,0,0,0,0]]
# TestGC=[[]]
GenRandGrille(grille,D)
AfficheG(grille,D)
print("Résolution de la grille . . .",'\n')
# Solveur(TestG,D)
# AfficheG(TestG,D)

if(Solveur(grille,D,Dval)):
    AfficheG(grille,D)
else:
    print("Cette grille n'a pas de solution")
# #c=Cell(D,0,D-1)
# print("cellule: ",grille[0][D-1])
# c.AfficheChoix()
# c.update(grille)
# Tab=['a','b','c']
# for i,e in enumerate(Tab):
#     print(e)
 
#print("Liste des choix: ",c.ListeChoix())
for i in range(4):
    print(i)
            


