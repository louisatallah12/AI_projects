# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:58:44 2020

@author: pc
"""
import operator

fichier=open(r"C:\Users\pc\Desktop\ESILV A3\S6\DataScience & IA\data (1).csv",'r')
liste=[]
for lines in fichier:
    line=lines.split(';')
    liste.append(line)
for lst in liste:
	lst[0]=float(lst[0])
	lst[1]=float(lst[1])
	lst[2]=float(lst[2])
	lst[3]=float(lst[3])
# A ce niveau là la comppilation affiche une erreur, il ne faut pas en tenir compte
         

print(liste)
print(len(liste))

liste_sans_nom=[]	#liste des coordonnées des fleurs sans noms
liste_nom=[]		#liste des coordonnées des fleurs avec noms
for i in range(len(liste)):
	if(len(liste[i])==4):
		liste_sans_nom.append(liste[i])
	elif(len(liste[i])==5):
		liste_nom.append(liste[i])
print(liste_nom)
print(liste_sans_nom)

# Calcul la distance entre 2 fleurs
def calcul(liste1,liste2):	
	return ((liste1[0]-liste2[0])**2+(liste1[1]-liste2[1])**2+(liste1[2]-liste2[2])**2+(liste1[3]-liste2[3])**2)**0.5


#Ajout des données dans un dictionnaire avec pour clé la dsitance et en valeur le nom de la fleur
resultats=dict()
for i in range(len(liste_nom)):
	resultats[calcul(liste_sans_nom[-1],liste_nom[i])]=liste_nom[i][4]
#tri du dico en fonction de la distance
resultats=dict(sorted(resultats.items(),key=operator.itemgetter(0)))
print(resultats)

#juste pour réinitialiser le dico lors des tests
#resultats.clear()

#liste contenant les clés triées soit les distances en ordre croissant (pour le test)
les_cles=[]
for cle in resultats.keys():
	les_cles.append(cle)
	
def Selection(k,res,cl):	#paramètre : k, res -> dico contenant nom des fleurs et distance, cl liste des distances qui sont clés de res 
	s=0
	ve=0
	vi=0		#les compteurs
	for i in range(k):
		fleur=res.get(cl[i])	#accès de la valeur par la clé
		if(fleur=='Iris-setosa\n'):
			s=s+1
		elif(fleur=='Iris-virginica\n'):
			vi=vi+1
		elif(fleur=='Iris-versicolor\n'):
			ve=ve+1
		else:
			print("aucune fleur")
	compteurs=[s,ve,vi]
	#print(compteurs)
	if(max(compteurs)==s):
		print("setosa")
	elif(max(compteurs)==ve):
		print("versicolor")
	elif(max(compteurs)==vi):
		print("virginica")


def main(c):
	for k in range(len(liste_sans_nom)):
		resultats=dict()
		
		for i in range(len(liste_nom)):
			resultats[calcul(liste_sans_nom[k],liste_nom[i])]=liste_nom[i][4]
		
		resultats=dict(sorted(resultats.items(),key=operator.itemgetter(0)))
		#print(resultats)
		les_cles=[]
		for cle in resultats.keys():
			les_cles.append(cle)
		#print(les_cles)
		Selection(c,resultats,les_cles)
		
print(main(10))