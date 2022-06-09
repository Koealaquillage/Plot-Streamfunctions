#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:10:36 2021

@author: koenig.g
Ici on plotte une fonction de courant et les vecteurs associés.
"""

#*******On importe nos bibliothèques*******************#
import numpy as np
import matplotlib.pyplot as plt

#******On définit notre fonction pour rendre le courant****#
def fonction_courant(A,x,C):
    """ A c'est un paramètre, x la position et 
    c un autre facteur de décalage"""

    return C/(4*A*x)
#*****Et on définit nos variables**********************#
x = np.linspace(0.2,5,100)
# On définit quelques C
C = np.linspace(-2,0,15)
# Et un truc pour noter
dx,dy = 0.01,0.01 
# Un espace vide pour y
y=[]
# Et une valeur pour A
A = -2

# Pour le graphique on définit une valeur vide
fig,ax = plt.subplots()

# On lance une boucle et on plotte
for c_ in C:
    # On calcule la ligne associée à la valeur C
    y = fonction_courant(A,x,c_)
    # Et on le plotte
    ax.plot(x,y,c='orange')
    # Et on plotte aussi la vitesse
    ax.quiver(x+dx,y+dy,2*A*(x+dx),-2*A*(y+dy),angles='xy',
              width=0.005,scale=100.)
    
    
