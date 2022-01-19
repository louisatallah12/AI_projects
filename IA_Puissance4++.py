# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:48:15 2020

@author: pc
"""
#importation des librairies nécessaires

import math
import random
from copy import deepcopy
import http.client
import time
import numpy as np

CRED = '\33[31m'
CEND = '\033[0m'
CBLUE   = '\33[34m'


def printGrille():
    for i in range(len(grille)):
        print("|",end=' ')
        for j in range(len(grille)):
            if(grille[i][j]==joueurDistant):
                print(CBLUE+'0'+CEND,end=' ')
            elif grille[i][j]==joueurLocal:
                print(CRED+'0'+CEND,end=' ')
            else:
                print(" ",end=' ')
            print("|",end=' ')
        print()
    print("|",end=' ')
    for i in range(len(grille)):
        print("_",end=" ")
        print("|",end=' ')
    print()
    print("|",end=' ')
    for i in range(len(grille)):
        print(i%10,end=" ")
        print("|",end=' ')
    print()
   
# methode qui detecte si la case est libre pour la colonne "jeu"
def colonneLibre (jeu):
    ligne = 0
    for j in range(len(grille)-1,-1,-1):
        if grille[j][jeu] == " " :
            ligne = j   #si la case est libre 
            break
    if(grille[ligne][jeu] == " "):
        return True   #return true si la case est bien libre
    else:
        return False 

# Action() liste les colonnes avec encore des cases libres restantes
def Action () :
    liste = []
    for i in range(len(grille)):
        if (colonneLibre(i)) :
            liste.append(i)
    liste.sort()
    return liste


def remplirGrille (grille , jeu , joueur):
    #on verifie tout d'abord si le move est valide
    if not(colonneLibre(jeu)):
        #affiche un message d'erreur si invalide
        print("Cette colonne est pleine!")
        return grille
    #si l'emplacement est valide, on parcourt les lignes de la colonne donnée pour placer le jeton 
    for i in range(len(grille)-1,-1,-1):
        if(grille[i][jeu]==" "): 
            grille[i][jeu]=joueur
            break
    return grille

# Utility() vérifie si il y a 4 jetons alignés et renvoie le caractere specifique  
def Utility (grille):
    #Vérification Verticale
    for i in range(len(grille)):
        for j in range(len(grille)-3):
            if ((grille[j][i] != " ") and (grille[j+1][i] != " ") and (grille[j+2][i] != " ") and (grille[j+3][i] != " ")
                and (grille[j][i] == grille[j+1][i]) and (grille[j+1][i] == grille[j+2][i]) and (grille[j+2][i] == grille[j+3][i]) ) :
                return grille[j][i]
   
    #Vérification Horizotale
    for i in range(len(grille)):
        for j in range(len(grille)-3):
            if ( (grille[i][j] != " ") and (grille[i][j+1] != " ") and (grille[i][j+2] != " ") and (grille[i][j+3] != " ")
                and (grille[i][j] == grille[i][j+1]) and (grille[i][j+1] == grille[i][j+2]) and (grille[i][j+2] == grille[i][j+3])) :
                return grille[i][j]

    #Vérifications Diagonales
    for i in list(reversed(range(3,len(grille)-3))):
        for j in range(len(grille)):
            if ((grille[i][j] != " ") and (grille[i-1][j+1] != " ") and (grille[i-2][j+2] != " ") and (grille[i-3][j+3] != " ")
                and (grille[i][j] == grille[i-1][j+1]) and (grille[i-1][j+1] == grille[i-2][j+2]) and (grille[i-2][j+2] == grille[i-3][j+3]) ) :
                return grille[i][j]
   
    for i in range(len(grille)-3):
        for j in range(len(grille)-3):
            if ((grille[i][j] != " ") and (grille[i+1][j+1] != " ") and (grille[i+2][j+2] != " ") and (grille[i+3][j+3] != " ")
                and (grille[i][j] == grille[i+1][j+1]) and (grille[i+1][j+1] == grille[i+2][j+2]) and (grille[i+2][j+2] == grille[i+3][j+3]) ) :
                return grille[i][j]

    return 0

# ici valeur est le signe retourné par Utility   
def Verdict(valeur):
    if(valeur == joueurLocal):
        print( "VOUS AVEZ GAGNE !!!!!")
        return True
    elif(valeur == joueurDistant):
        print( "L'IA a gagné :(")
        return True
    else:
        return False



def matchNul ():
    for i in range(len(grille)):
        if grille[0][i] == " " :
            return False
    print("Match nul!")
    return True


def calculateScore (scoreIA , actions):
    #returns score according to the number of the consecutive pieces of the AI
    moveScore = 4 - actions
    if scoreIA == 0 :
        return 0
    elif scoreIA == 1 :
        return 1 * moveScore
    elif scoreIA == 2 :
        return 10 * moveScore
    elif scoreIA == 3 :
        return 10 * moveScore
    else :
        return 1000

def evaluategrille (grille):
    #scoreIA indicates how many AI consecutive pieces
    scoreIA = 1
    score = 0
    #cellVide indicates how many empty cells consecutive pieces
    cellVide = 0
    k = 0
    actions = 0
    #iterates over the grille to determine the listeActions of AI pieces to get how many consecutive pieces
    for i in list(reversed(range(len(grille)))):
        for j in range(len(grille)):
            #continue of it is not an AI piece
            if (grille[i][j] == " ") or (grille[i][j] == joueurLocal):
                continue
            #when j <=3 evaluate how many horizontal consecutives by determining the right side of the j jeu
            if j <= 3 :
                for k in range(1,len(grille)-3):
                    if grille[i][j+k] == joueurDistant :
                        scoreIA += 1
                    elif grille[i][j+k] == joueurLocal :
                        scoreIA = 0
                        cellVide = 0
                        break
                    else :
                        cellVide += 1

                actions = 0
                if cellVide > 0 :
                    for c in range(1,len(grille)-3):
                        jeu = j + c
                        for m in range(i,len(grille)):
                            if grille[m][jeu] == " " :
                                actions += 1
                            else :
                                break
                #calculate the score of the consecutives by calling calculateScore method
                if actions != 0 :
                    score += calculateScore (scoreIA,actions)
                scoreIA = 1
                cellVide = 0
           
            if i >= 3 :
                for k in range(1,4):
                    if grille[i-k][j] == joueurDistant :
                        scoreIA += 1
                    elif grille[i-k][j] == joueurLocal :
                        scoreIA = 0
                        break
                actions = 0
                if scoreIA > 0 :
                    jeu = j
                    for m in range(i-k+1,i):
                        if grille[m][jeu] == " " :
                            actions += 1
                        else :
                            break
                if actions != 0 :
                    score += calculateScore (scoreIA,actions)
                scoreIA = 1
                cellVide = 0
            #when j >=3 evaluate how many horizontal consecutives by determining the left side of the j jeu
            if j >= 3 :
                for k in range(1,4):
                    if grille[i][j-k] == joueurDistant :
                        scoreIA += 1
                    elif grille[i][j-k] == joueurLocal :
                        scoreIA = 0
                        cellVide = 0
                        break
                    else :
                        cellVide += 1
                actions = 0
                if cellVide > 0 :
                    for c in range(1,4):
                        jeu = j-c
                        for m in range(i,len(grille)):
                            if grille[m][jeu] == " ":
                                actions += 1
                            else :
                                break
                if actions != 0 :
                    score += calculateScore (scoreIA,actions)
                scoreIA = 1
                cellVide = 0
            #when j <=3  and i>=3 evaluate how many diagonal(positive slope)consecutives
            if (j <= 3) and (i >= 3):
                for k in range(1,4):
                    if grille[i-k][j+k] == joueurDistant :
                        scoreIA += 1
                    elif grille[i-k][j+k] == joueurLocal :
                        scoreIA = 0
                        cellVide = 0
                        break
                    else :
                        cellVide += 1
                actions = 0
                if cellVide > 0 :
                    for c in range(1,len(grille)-3):
                        jeu = j+c
                        row = i-c
                        for m in range(row,len(grille)):
                            if grille[m][jeu] == " " :
                                actions += 1
                            elif grille[m][jeu] == joueurDistant :
                                pass
                            else :
                                break
                    if actions != 0 :
                        score += calculateScore(scoreIA,actions)
                    scoreIA = 1
                    cellVide = 0
            #when j >=3  and i>=3 evaluate how many diagonal(negative slope)consecutives
            if (j >= 3) and (i >= 3):
                for k in range(1,4):
                    if grille[i-k][j-k] == joueurDistant :
                        scoreIA += 1
                    elif grille[i-k][j-k] == joueurLocal :
                        scoreIA = 0
                        cellVide = 0
                        break
                    else :
                        cellVide += 1
                actions = 0
                if cellVide > 0 :
                    for c in range(1,4):
                        jeu = j-c
                        row = i-c
                        for m in range(row,len(grille)):
                            if grille[m][jeu] == " " :
                                actions += 1
                            elif grille[m][jeu] == joueurDistant :
                                pass
                            else :
                                break
                    if actions != 0 :
                        score += calculateScore (scoreIA,actions)
                    scoreIA = 1
                    cellVide = 0
    return score

def Joueur_IA():
    jeu , score = Min_Max_Decision(grille,0,True)
    return jeu

def Min_Max_Decision(grille , profondeur , me , limite = 5 , alpha = -math.inf , beta = math.inf ):
    # Get remains empty listeActions in the grille.
    listeActions = Action()
    # The game is about to end (me win , him win ,both lose(completed grille)):
        # 1-Me win -> score = inf & no jeu to play
        # 2-Him win -> score = -inf & no jeu to play
        # 3-Completed grille -> score = 0 & no jeu to play
    game_end = (True if ((Utility(grille) != 0) or (len(listeActions )== 0)) else False )
    if game_end :
        if Utility(grille) == joueurDistant :
            return (None, math.inf)
        elif Utility(grille) == joueurLocal :
            return (None, -math.inf)
        else:
            return (None, 0)
    # profondeur = limiteed of profondeur (stop condition) -> score = current score & no jeu to play
    elif profondeur == limite :
        # we need to redefine the evaluation function
        return (None, evaluategrille(grille))
    # My Turn to play
    elif me:
        initial_score = -math.inf
        # using random choice we choose a random element from a list
        jeu = random.choice(listeActions)
        # loop in all Action (jeus)
        for action in listeActions:
            # make a copy from the current state
            grille_copy = deepcopy(grille)
            # what if i played here ? did i win ?
            # so to find out lets cal the score for this game
            # if score > initial_score -> update initial_score & let's play this game
            grille_copy = remplirGrille(grille_copy , action , joueurDistant)
            jeu , new_score = Min_Max_Decision(grille_copy, profondeur+1, False , limite ,  alpha , beta )
            #undoMove(grille,jeu)
            if new_score > initial_score:
                initial_score = new_score
                jeu = action
                alpha = max(alpha, initial_score)
                # Stop condition for the alpha_beta algorithm
                if alpha >= beta:
                    break
        return jeu, initial_score
    # His Tuen to play
    elif not(me):
        initial_score = math.inf
        # using random choice we get a random element from a list that him could choose  
        jeu = random.choice(listeActions)
        # loop in all Action (jeus)
        for action in listeActions:
            # make a copy from the current state
            grille_copy = deepcopy(grille)
            # what if he played here ? did he win ?
            # so to find out lets cal the score for this game
            # if score < initial_score -> update initial_score & let's play this game (he will loose)
            grille_copy = remplirGrille(grille_copy , action , joueurLocal)
            new_score = Min_Max_Decision(grille_copy, profondeur+1, True , limite ,  alpha, beta)[1]
            if new_score < initial_score:
                initial_score = new_score
                jeu = action
                beta = min(beta, initial_score)
                # Stop condition for the alpha_beta algorithm
                if alpha >= beta:
                    break
        return jeu, initial_score
 

grilleDim=12
grille = [[" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
             [" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
             [" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
             [" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
             [" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
[" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
[" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
[" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
[" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
[" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "],
             [" ", " ", " ", " ", " ", " ", " "," "," "," "," "," "]]

# bien préviser si vous commencer le jeu ou c'est l'adversaire qui commence
joueurLocalquiCommence=True

# cette fonction est à remplacer une qui saisie le jeu de l'adversaire à votre IA
def appliqueJeuAdv(jeu):
    print("jeu de l'adversaire est ", jeu)
   
def monjeu():
	#checks if valid move
	jeu = int(input("Veuillez saisir la colonne de votre jeu entre 0 et "+ str(grilleDim-1) +" : "))
	   while (jeu < 0 or jeu > 11 or colonneLibre(jeu)==False):
        jeu = int(input("Erreur! Colonne non valide ! \nVeuillez saisir la colonne de votre jeu entre 0 et "+ str(grilleDim-1) +" : "))
    #place the move in the grille
    remplirGrille(grille , jeu , joueurLocal)
	


if(joueurLocalquiCommence):
    joueurLocal=2
    joueurDistant=1
else:
    joueurLocal=1
    joueurDistant=2
   

###############################################################

###############################################
tour=0


if(joueurLocalquiCommence):
    jeu=monJeu()
     
    remplirGrille(grille,random.choice(range(12)),joueurDistant)
       
    printGrille()
   
	
	   
    while (True) :
        #check it there is a draw
        if matchNul() :
            break
        #let the joueur enter his moves
        monJeu()
        printGrille()
        gameResult = Utility(grille)
        #Vérification victoire ou défaite
        if Verdict(gameResult):
            break
        else :
            remplirGrille(grille,Joueur_IA(),joueurDistant)

        printGrille()
        gameResult = Utility(grille)

        if Verdict(gameResult):
            break
 
    tour+=1
