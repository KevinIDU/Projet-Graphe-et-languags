# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:39:47 2020

@author: Kévin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:04:11 2020

@author: Kévin
"""

from ligne import Lignes
import data2py as data

class Arret(Lignes):
    
    def __init__ (self, direction, nom, numLigne=[], horaires=[]):
    
        self.horaires = horaires
        self.direction = direction
        self.nom = nom
        self.numLigne = numLigne

    
    def getDirection(self):
        return self.direction
    
    def getNom(self):
        return self.nom
    
    def getLigne(self, ligne1:Lignes):
      liste= ligne1.getArret()
      for nomArret in liste:
          if nomArret == self.nom:
              self.numLigne = ligne1.numero
              return self.numLigne
            
             
    def getHoraireAller(self):
        self.horaires = data.regular_date_go[self]
        return self.horaires
            
    def getHoraireRetour(self, ligne:Lignes):
        nom = ligne.getArret()
        for name in nom:
            if self.getNom() == name:
                self.horaires = data.regular_date_back[name]
        return self.horaires
            
   

        
        
        
    
#arret = Arret('direct', 'Vernod')
#lig=Lignes(1) 
#a=arret.Horraire_Seconde(lig)
##a_splited = a[0].split(":")
##heures= a_splited[0]
##miniutes = a_splited[1]
#print(a)
#print(Horraire_Seconde("10:52"))