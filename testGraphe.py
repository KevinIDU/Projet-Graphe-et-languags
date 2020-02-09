# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:10:16 2020

@author: Kévin
"""
import networkx as nx
import data2py as data
import Arret as arret

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
        G.add_edge(name1[i], name1[i+1])
      
        for i in range(len(name2)-1):
            G.add_edge(name2[i], name2[i+1])



      
      
#==============================================================
      #conversion de time en seconde et vise versa 
#==============================================================
      
def Horraire_Seconde(time):
    h_splited = time.split(":")
    heures = int(h_splited[0])*60        
    minutes = int(h_splited[1])
    temps = heures + minutes
    return temps


def Horraire_minute(time):
    heure = time // 60
    minute = time % 60
    return (heure,minute)

#==============================================================
       
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
        

Creategraphe()
conversionHorairesgo()


   
#for nodes in G.nodes : 
#   if nodes == "GARE" : 
#        print(G.adj[nodes])

#
#depart = input ("Ou etes vous ? ")
#arrive = input ("Ou voulez vous aller ?" )
#heure = input("L'heure svp") #format h:min
#time = Horraire_Seconde(heure)
#
##
#print(name1[0], name2[11]) #name[0] = poissy , name[21] = campus
#print (nx.shortest_path(G, name1[8], name2[10]))
