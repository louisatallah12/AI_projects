# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:16:23 2020

@author: pc
"""

import numpy as np
import time
def ErrorModel(m,b,data):
    """
    f:x|--> mx+b
    data = {(x,y)}
    """
    n = len(data)
    return (1/n) *sum((((m*data[i][0]+b) - data[i][1])**2 for i in range(n)))


def getData():
    """
    Fonction permettant de récupérer les données provenant du fichier csv
    """
    data = []
    #On récupère les données dans le fichier
    with open('C:/Users/pc/Desktop/ESILV A3/S6/DataScience & IA/TD 6/IA_tp6_data.csv') as f:
        for row in f:
            row = row.replace("\n","") #on enlève les sauts de ligne
            row = row.split(',') #On sépare les valeurs
            row = [float(item) for item in row] #On converti les valeurs en flotant (car elles sont au départ ou forme de chaine de carractères)
            data.append(row)
    return data

#Définition du dataset
dataset = getData()


def MSE(m,b,données):
    erreur=0
    for point in données:
        if point!=['']:
            erreur+=(m*float(point[0])+b-float(point[1]))**2
    return erreur/len(données)

#Methode brute force

def BruteForce(données):
    minimal=10000
    mmin=-49.9
    bmin=-9.9
    compteur=0
    debut=time.time()
    for m in range(-499,501):
        for b in range(-99,101):
            candidat=MSE(m/10,b/10,données)
            print(compteur)
            compteur+=1
            if candidat<minimal:
                minimal=candidat
                mmin=m/10
                bmin=b/10
    fin=time.time()-debut
    print(fin)
    return mmin,bmin

print(BruteForce(dataset))

