# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:10:16 2020

@author: Kévin
"""
import networkx as nx
import data2py as data

"""
LYCEE_DE_POISY                          PISCINE-PATINOIRE
POISY_COLLÈGE                           Arcadium 
Vernod                                  Parc_des_Sports 
Meythet_Le_Rabelais                     Place_des_Romains     
Chorus                                  Courier 
Mandallaz                               GARE 
GARE                                    Bonlieu 
France_Barattes                         Préfecture_Pâquier 
C.E.S._Barattes                         Imperial 
VIGNIERES                               Pommaries 
Ponchy                                  VIGNIERES 
PARC_DES_GLAISINS                       CAMPUS
"""


#==============================================================
      #Création du graphe
#==============================================================
      
G = nx.Graph()     
name1 = data.regular_path1.split(" N ")
name2= data.regular_path2.split(" N ")

def Creategraphe():
    for i in range(len(name1)-1):
        G.add_edge(name1[i], name1[i+1], poids = 1)
      
        for i in range(len(name2)-1):
            G.add_edge(name2[i], name2[i+1], poids = 1)



      
      
#==============================================================
      #fonction sur les horraires
#==============================================================
    
#remplace h:min en sec
def Horraire_Seconde(time):
    h_splited = time.split(":")
    heures = int(h_splited[0])*60        
    minutes = int(h_splited[1])
    temps = heures + minutes
    return temps

#remplace sec en h:min
def Horraire_minute(time):
    heure = time // 60
    minute = time % 60
    return (heure,minute)

#convertit toutes les horaires des fichiers en secondes  
def conversionHorairesgo():
    for elem in data.regular_date_go[0]:
        print(elem)
        liste=[]
        for j in data.regular_date_go[0][elem]:
            if j == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(j))
                
        print(liste, end =",")
        print("\n")
        
    for elem in data.regular_date_go[1]:    
        print(elem)
        liste=[]
        for j in data.regular_date_go[1][elem]:
            if j == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(j))
       
        print(liste, end =",")
        print("\n")
        
#trouve le prochain bus qui passe a un arret donné
def TrouveHorraire():
    heure = input("Quelle heure est-il? \n")
    ligne = input("Sur quelle ligne êtes vous ? \n")
    départ = input("A quel arrêt vous trouvez vous? \n")
    direction = input("la direction du bus ?")
    liste=[]
    hor=Horraire_Seconde(heure)
    if ligne == "1" and direction == "PARC_DES_GLAISINS"  :
        for heure in data.regular_date_go[0][départ]:
            if heure == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(heure))
        for elem in liste:
            if type(elem) != str:
                if (elem - hor > 0):
                    return Horraire_minute(elem)
#   Rajouter les conditions pour gere les we et jours ferier    
    if ligne == "1" and direction == "LYCEE_DE_POISY + POISY_COLLEGE" :
        for heure in data.regular_date_back[0][départ]:
            if heure == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(heure))
        for elem in liste:
            if type(elem) != str:
                if (elem - hor > 0):
                    return Horraire_minute(elem)
    
    if ligne == "2":
        for heure in data.regular_date_go[1][départ]:
            if heure == "-":
                liste.append(".")
            else:
                liste.append(Horraire_Seconde(heure))
        for elem in liste:
            if type(elem) != str:
                if (elem - hor > 0):
                    return Horraire_minute(elem) 
#==============================================================
      #Algo 
#==============================================================                 

#le chemin le plus rapide 
      
def shortest():
    depart = input("ou etes vous ? ")
    arrive = input ("ou allez vous ?")
    print("le chemin le plus rapide est: ", nx.shortest_path(G,depart,arrive))
    

