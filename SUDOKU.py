# -*- coding: utf-8 -*-
"""

@author: pc

ARISS nael
ATALLAH Louis

Projet : resolution de sudoku à multiples difficultées
"""
import numpy as np
def GenererPlateau(L,c):  # methode pour générer un sudoku de taille L avec c cases révélées
    k=0
    matrice=np.zeros(shape=(L,L))
    while k < c:
    
        i=np.random.randint(0,len(matrice))
        j=np.random.randint(0,len(matrice))
        r=np.random.randint(1,9)
        if(r not in matrice[i,:] and r not in matrice[:,j] and matrice[i,j]==0): #si les conditions sont satisfaites alors on ajoute la valeur dans la matrice
            matrice[i,j]=r
            k=k+1
    print(matrice)
    return matrice

mat=GenererPlateau(9,17)

from ortools.sat.python import cp_model

model = cp_model.CpModel()


taille = 3          # taille des petits carrés du plateau
ligne = taille**2
line = range(ligne)
case = range(taille)

plateau = {
    (i, j): model.NewIntVar(1, ligne, 'plateau %i %i' % (i, j))
    for i in line
    for j in line
}

plateau = {}
for i in line:
    for j in line:
        plateau[i, j] = model.NewIntVar(1, ligne, 'plateau %i %i' % (i, j))
        
for i in line:
    model.AddAllDifferent([plateau[(i, j)] for j in line])
    
for j in line:
    model.AddAllDifferent([plateau[(i, j)] for i in line])
    
for i in case:
    for j in case:
        one_case = [
            plateau[(i * taille + di,
                    j * taille + dj)]
            for di in case
            for dj in case
        ]
        model.AddAllDifferent(one_case)
        

            
solver = cp_model.CpSolver()

cond = solver.Solve(model)
if cond == cp_model.FEASIBLE:
    for i in line:
        print([int(solver.Value(plateau[(i, j)])) for j in line]) #le sudoku est résolu ligne par ligne et colonne par colonne
        
        
