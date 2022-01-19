# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:58:44 2020

@author: pc
"""
import operator

fichier=open(r"C:\Users\pc\Desktop\ESILV A3\S6\DataScience & IA\preTest (1).csv",'r')
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

liste_sans_nom=[]	#liste des coordonnées des lettres sans noms
liste_nom=liste		#liste des coordonnées des lettres avec noms
fichier=open(r"C:\Users\pc\Desktop\ESILV A3\S6\DataScience & IA\finalTest (1).csv",'r')
for lines in fichier:
    line=lines.split(';')
    liste_sans_nom.append(line)
for lst in liste_sans_nom:
	lst[0]=float(lst[0])
	lst[1]=float(lst[1])
	lst[2]=float(lst[2])
	lst[3]=float(lst[3])
"""for i in range(len(liste)):
	if(liste[i][4]=='\n'):
		liste_sans_nom.append(liste[i])
	else:
		liste_nom.append(liste[i])"""
print(liste_nom)
print("\n\n\n")
print(liste_sans_nom)

# Calcul la distance entre 2 lettres
def calcul(liste1,liste2):	
	return ((liste1[0]-liste2[0])**2+(liste1[1]-liste2[1])**2+(liste1[2]-liste2[2])**2+(liste1[3]-liste2[3])**2)**0.5


#Ajout des données dans un dictionnaire avec pour clé la dsitance et en valeur le nom de la lettre
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


def Selection(k,res,cl):	#paramètre : k, res -> dico contenant nom des lettres et distance, cl liste des distances qui sont clés de res 
	a=0
	b=0
	c=0		#les compteurs
	I=0
	d=0
	e=0
	f=0
	g=0
	h=0
	j=0
	stock=""
	file=open(r"C:\Users\pc\Desktop\ESILV A3\S6\DataScience & IA\TD 5\ARISS_ATALLAH.txt",'a')
	for i in range(k):
		lettre=res.get(cl[i])	#accès de la valeur par la clé
		if(lettre=='A\n'):
			a=a+1
		elif(lettre=='B\n'):
			b=b+1
		elif(lettre=='C\n'):
			c=c+1
		elif(lettre=='D\n'):
			d=d+1
		elif(lettre=='E\n'):
			e=e+1
		elif(lettre=='F\n'):
			f=f+1
		elif(lettre=='G\n'):
			g=g+1
		elif(lettre=='H\n'):
			h=h+1
		elif(lettre=='I\n'):
			I=I+1
		elif(lettre=='J\n'):
			j=j+1
		else:
			print("aucune lettre")
	compteurs=[a,b,c,d,e,f,g,h,I,j]
	#print(compteurs)
	if(max(compteurs)==a):
		print("A")
		stock="A\n"
	elif(max(compteurs)==b):
		print("B")
		stock="B\n"
	elif(max(compteurs)==c):
		print("C")
		stock="C\n"
	elif(max(compteurs)==d):
		print("D")
		stock="D\n"
	elif(max(compteurs)==e):
		print("E")
		stock="E\n"
	elif(max(compteurs)==f):
		print("F")
		stock="F\n"
	elif(max(compteurs)==g):
		print("G")
		stock="G\n"
	elif(max(compteurs)==h):
		print("H")
		stock="H\n"
	elif(max(compteurs)==I):
		print("I")
		stock="I\n"
	elif(max(compteurs)==j):
		print("J")
		stock="J\n"
	"""for i in range(len(liste)):
		if(liste[i][4]=='\n'):
			liste[i][4]=stock
			break

			"""
	
	file.write(stock)
	file.close()
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

		
print(main(11))

# verification du pourcentage de reussite par rapport à la liste originale
#fichierO=open(r"C:\Users\pc\Desktop\ESILV A3\S6\DataScience & IA\preTest original.csv",'r')
#liste_originale=[]
#for lines in fichierO:
 #   line=lines.split(';')
  #  liste_originale.append(line)
#for lst in liste_originale:
#	lst[0]=float(lst[0])
#	lst[1]=float(lst[1])
#	lst[2]=float(lst[2])
#	lst[3]=float(lst[3])
#compteur=0
#for i in range(len(liste)):
#	if(liste[i][4]==liste_originale[i][4]):
#		compteur+=1
		
#print("Taux de correspondance : ",compteur/len(liste)*100," %, pour ",len(liste_sans_nom)," valeurs manquantes")