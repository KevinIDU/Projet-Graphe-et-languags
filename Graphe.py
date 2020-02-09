# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:54:06 2020

@author: Kévin
"""

from Noeud import noeud

class Graphe(noeud):
    
    def __init__(self, nodes=[]):
        self.nodes = nodes 

    def setNodes(self):
        pass











"""LIGNE 2"""

n20= noeud('PISCINE-PATINOIRE')
n21= noeud('Arcadium')
n22= noeud('Parc_des_Sports')
n23= noeud('Place_des_Romains')
n24= noeud('Courier')

n25= noeud('GARE')
n26= noeud('Bonlieu')
n27= noeud('Préfecture_Pâquier')
n28= noeud('Impérial')
n29= noeud('Pommaries')
n210= noeud('VIGNIÈRES')
n211= noeud('CAMPUS')

"""LIGNE 1 """

n10=noeud('LYCÉE_DE_POISY + POISY_COLLÈGE')
n11=noeud('Vernod')
n12=noeud('Meythet_Le_Rabelais')
n13=noeud('Chorus')
n14=noeud('Mandallaz')
n15=noeud('GARE')
n16=noeud('France_Barattes')
n17=noeud('C.E.S._Barattes')
n18=noeud('VIGNIÈRES')
n19=noeud('Ponchy')
n110=noeud('PARC_DES_GLAISINS')

""""""""""""""""""""""""""""""""""""""""""""""""

n20.setSucesseur(n21)
n21.setPredecesseur(n20)
n21.setSucesseur(n22)
n22.setPredecesseur(n21)
n22.setSucesseur(n23)
n23.setPredecesseur(n22)
n23.setSucesseur(n24)
n24.setPredecesseur(n23)
n24.setSucesseur(n25)
n25.setPredecesseur(n14)
n25.setPredecesseur(n24)
n25.setSucesseur(n16)
n25.setSucesseur(n26)
n26.setPredecesseur(n25)
n26.setSucesseur(n27)
n27.setPredecesseur(n26)
n27.setSucesseur(n28)
n28.setPredecesseur(n27)
n28.setSucesseur(n29)
n29.setPredecesseur(n28)
n29.setSucesseur(n210)
n210.setPredecesseur(n17)
n210.setPredecesseur(n29)
n210.setSucesseur(n19)
n210.setSucesseur(n211)
n211.setPredecesseur(n210)





n10.setSucesseur(n11)
n11.setPredecesseur(n10)
n11.setSucesseur(n12)
n12.setPredecesseur(n11)
n12.setSucesseur(n13)
n13.setPredecesseur(n12)
n13.setSucesseur(n14)
n14.setPredecesseur(n13)
n14.setSucesseur(n15)
n15.setPredecesseur(n14)
n15.setPredecesseur(n24)
n15.setSucesseur(n16)
n15.setSucesseur(n26)
n16.setPredecesseur(n15)
n16.setSucesseur(n17)
n17.setPredecesseur(n16)
n17.setSucesseur(n18)
n18.setPredecesseur(n17)
n18.setPredecesseur(n29)
n18.setSucesseur(n19)
n18.setSucesseur(n211)
n19.setPredecesseur(n18)
n19.setSucesseur(n110)
n110.setPredecesseur(n19)

print(n15.getPredecesseur())