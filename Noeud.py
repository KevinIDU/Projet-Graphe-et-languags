# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:48:20 2020

@author: Kévin
"""

#G1= dict()
#G1['LYCÉE_DE_POISY + POISY_COLLÈGE'] = [' ', 'Vernord']
#G1['Vernod'] = ['LYCÉE_DE_POISY + POISY_COLLÈGE','Meythet_Le_Rabelais']
#G1['Meythet_Le_Rabelais'] = ['Vernod','Chorus']
#G1['Chorus'] = ['Meythet_Le_Rabelais','Mandallaz']
#G1['Mandallaz'] = ['Chorus','GARE']
#G1['GARE'] = ['Mandallaz','France_Barattes']
#G1['France_Barattes'] = ['GARE','C.E.S._Barattes']
#G1['C.E.S._Barattes'] = ['France_Barattes','VIGNIÈRES']
#G1['VIGNIÈRES'] = ['C.E.S._Barattes','Ponchy']
#G1['Ponchy'] = ['VIGNIÈRES','PARC_DES_GLAISINS']
#G1['PARC_DES_GLAISINS'] = ['Ponchy', ' ']
#
#G2 = dict()
#G2['PISCINE-PATINOIRE'] = [' ','Arcadium']
#G2['Arcadium'] = ['PISCINE-PATINOIRE','Parc_des_Sports']
#G2['Parc_des_Sports'] = ['Arcadium','Place_des_Romains']
#G2['Place_des_Romains'] = ['Parc_des_Sports','Courier']
#G2['Courier'] = ['Place_des_Romains','GARE']
#G2['GARE'] = ['Courier','Bonlieu']
#G2['Bonlieu'] = ['GARE','Préfecture_Pâquier']
#G2['Préfecture_Pâquier'] = ['Bonlieu','Impérial']
#G2['Impérial'] = ['Préfecture_Pâquier','Pommaries']
#G2['Pommaries'] = ['Impérial','VIGNIÈRES']
#G2['VIGNIÈRES'] = ['Pommaries', 'CAMPUS']
#G2['CAMPUS'] = ['VIGNIÈRES', ' ' ]




class noeud():
    
    def __init__ (self, nom, predecesseur=[], sucesseur=[], ligne=[]):
        self.nom = nom
        self.ligne = ligne
        

    def setSucesseur(self, succ):
         self.sucesseur = succ
    
    def setPredecesseur(self, pred):
         self.predecesseur = pred
    
    def getNom(self):
        return self.nom
    
    def getLigne(self):
        return self.ligne
    
    def __str__(self):
        return self.nom
    
    def getSucesseur(self):
        return self.sucesseur.getNom()
    
    def getPredecesseur(self):
        return self.predecesseur.getNom()
    

#node=noeud('Vernord')    
#node1=noeud('GARE')
#node2=noeud('Meythet')
#
#node1.setPredecesseur(node)
#node1.setSucesseur(node2)


    
    
    
    
    
    
    
    
    
    
    
    
    