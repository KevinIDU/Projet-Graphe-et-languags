# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:41:05 2020

@author: Kévin
"""

import data2py as data



class Lignes ():
    def __init__(self, numero, arret=[]):
        self.numero = numero
        self.arret = arret 
        
        
    def getArret(self):
        name = data.regular_path.split(" N ")
        for a in name:
            self.arret.append(a) 
        return self.arret
    
    def getNumero(self):
        return self.numero
    

    
    
#a=Lignes(1)
#nom = a.getArret()
#print (nom)