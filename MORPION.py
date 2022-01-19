# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:31:51 2020

@author: pc
"""


"""

print("__|__|__", "__|__|__", "  |  |  ", sep='\n')
"""

import numpy as np
state=np.full((3,3)," ")
print(type(state))

print(Terminal(state))
def Terminal(state):
    if(str(" ") not in state ):
        return True
    elif(Utility(state)!=0):
       return True
    return False

def Utility(state):
    res=0
    for i in range(len(state)):
        if("X" not in state[i,:] and " " not in state[i,:]):
            res=-1
        if("O" not in state[i,:] and " " not in state[i,:]):
            res=1
        if("X" not in state[:,i] and " " not in state[:,i]):
            res=-1
        if("O" not in state[:,i] and " " not in state[:,i]):
            res=1
    
    if([ state[i][i] for i in range(len(state)) ]==["O","O","O"]):
        res= -1 
    elif([ row[-i-1] for i,row in enumerate(state) ]==["O","O","O"]):
        res=-1
    elif([ state[i][i] for i in range(len(state)) ]==["X","X","X"]):
        res= 1    
    elif([ row[-i-1] for i,row in enumerate(state) ]==["X","X","X"]):
        res=1
    return res

def Verdict(valeur):
    if(valeur==-1):
        return "Le joueur humain a gagné "
    elif(valeur==0):
        return "Match null"
    else:
        return "L'IA a gagné"
        
def Action(state):   #renvoie la liste des cases vides
    liste=[]
    for i in range(len(state)):
        for j in range(len(state)):
            if(state[i,j]==" "):
                liste.append([i,j])
    return liste

def Result(state,a):        #a est l'indice de la liste 
    if(len(Action(state))==0):
        return ""
    i,j=Action(state)[a]
    state[i,j]="X"
    return state

def Prediction(state,a):
    if(len(Action(state))==0):
        return ""
    i,j=Action(state)[a]
    state[i,j]="O"
    return state
    
  
def Max_Value(state):
    if (Terminal(state)):
        return Utility(state)
    v=-1000
    for a in range(len(Action(state))):
        v=max(v,Min_Value(Result(state,a)))
    return v
    
def Min_Value(state):
    if (Terminal(state)):
        return Utility(state)
    v=1000
    for a in range(len(Action(state))):
        v=min(v,Max_Value(Prediction(state,a)))
    return v

def Min_Max_Decision(state):
    return Min_Value(Result(state,0))


def Jeu(state):
    valeur=0
    while (not Terminal(state) ):
        state=ai_input(state)
        
        if( Terminal(state)):
            valeur=Utility(state)
            print(Verdict(valeur))
            break

        #i,j=ai_input(state)
        #print(i,j,sep=" ")
        #state[i][j]="X"
        printState(state)
        state=Joueur_Humain(state)
        
       
        #state=Result(state,0) 
        printState(state)
    valeur=Utility(state)
    print(Verdict(valeur))
    return state

state=np.full((3,3)," ")
print(Jeu(state))

def printState(state):
    print(state[0,0] + '|' + state[0,1] + '|' + state[0,2])
    print('-+-+-')
    print(state[1,0] + '|' + state[1,1] + '|' + state[1,2])
    print('-+-+-')
    print(state[2,0] + '|' + state[2,1] + '|' + state[2,2])



def Joueur_Humain(state):
    choix = input("A vous de jouer ! Saisissez une position : \n")
    if (choix == "1") :
        i,j=[0,0]
    elif (choix == "2"):
        i,j=[0,1]
    elif (choix == "3"):
        i,j=[0,2]
    elif (choix == "4"):
        i,j=[1,0]
    elif (choix == "5"):
        i,j=[1,1]
    elif (choix == "6"):
        i,j=[1,2]
    elif (choix == "7"):
        i,j=[2,0]
    elif (choix == "8"):
        i,j=[2,1]
    elif (choix == "9"):
        i,j=[2,2]
    if(state[int(i),int(j)]==" "):
        state[int(i),int(j)]="O"
    else:
        print("case déjà prise")
        exit(0)
    return state


import copy


def ai_input(state):
    moves=[]
    fake_grid = copy.deepcopy(state)
    for row in range(len(fake_grid)):
        for col in range(len(fake_grid[row])):
            for a in range(len(Action(state))-1,0,-1):
                return Result(fake_grid,a)
           

def Min_Max_Decision(fake_grid,depth,is_max):
    if Utility(fake_grid) != 0 or depth == 0:
        return Utility(fake_grid)
    
    if is_max :
        max_value = 0
        for row in range(len(fake_grid)):
            for col in range(len(fake_grid[row])):
                if fake_grid[row][col] == " ":
                    new_grid = copy.deepcopy(fake_grid)
                    new_grid[row][col]="X"
                    value = Min_Max_Decision(new_grid,depth-1,False)*depth
                    max_value = max(max_value,value)
        return max_value
    else:
        min_value = 0
        for row in range(len(fake_grid)):
            for col in range(len(fake_grid[row])):
                if fake_grid[row][col] == " ":
                    new_grid = copy.deepcopy(fake_grid)
                    new_grid[row][col] = "O"
                    value = Min_Max_Decision(new_grid,depth-1,True)*depth
                    min_value = min(min_value,value)
        return min_value
print( ai_input(state))
print(state)

"""def minimax(game, depth, maximizingplayer):

    score, choice = GetScore(game)
    if depth == 0 or score == WIN or score == LOSE:
        return score, game

    if maximizingplayer:
        best = LOSE
        best_child = None
        games = GeneratePossibleMoves(game, 'O')
        for child in games:
            v, move = minimax(child, depth-1, False)
            if v > best-1:
                best_child = child
                best = v
        return best, best_child
    else:
        best = WIN
        best_child = None
        games = GeneratePossibleMoves(game, 'X')
        for child in games:
            v, move = minimax(child, depth-1, True)
            if v <= best:
                best_child = child
                best = v
        return best, best_child
