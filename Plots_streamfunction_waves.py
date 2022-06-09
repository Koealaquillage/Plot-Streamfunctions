#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:46:15 2021

@author: koenig.g
Ici on fait une stream function aussi mais pour les vagues et on dessine 
la trajectoire
"""

#*******On importe nos bibliothèques*******************#
import numpy as np
import matplotlib.pyplot as plt

#******On définit notre fonction pour rendre le courant****#
def fonction_courant(A,k,w,x,z,t):
    """On rend la fonction courant aux points x,z,t  """

    return (A/k)*np.outer(np.exp(k*z),np.cos(k*x-w*t))

def U_vel(A,k,w,x,z,t):
    """On rend la vitesse U"""
    
    return A*np.outer(np.exp(k*z),np.cos(k*x-w*t))

def W_vel(A,k,w,x,z,t):
    """On rend la vitesse W"""
    
    return A*np.outer(np.exp(k*z),np.sin(k*x-w*t))

def update_xz(x,z,A,k,w,t,delta_t) :
    """ On fait une petite mise à jour de la trajectoire"""
    u_traj = U_vel(A,k,w,x,z,t)
    w_traj = W_vel(A,k,w,x,z,t)
    
    return x+delta_t*u_traj,z+delta_t*w_traj
#*****Et on définit nos variables**********************#
x = np.linspace(0.,5,100)
z = np.linspace(0.,-2.,100)
t_ = np.linspace(0,10,333)
delta_t = 0.03
# Un espace vide pour la fonction courant et les vitesses
psi = np.zeros(shape=(100,100)) # Il doit avoir la taille de x*z

U = np.zeros(shape=(100,100))
V = np.zeros(shape=(100,100))
# Et une valeur pour A
A = 0.3
k = 2.
w= 2.

# Et finalement, on rajoute un petit x,z pour voir les trajectoires
x_traj,z_traj = [[2.],[2.],[2.],[2.],[2.]],[[-0.2],[-0.5],[-0.75],[-1.],[-1.5]]
# Pour le graphique on définit une valeur vide
fig,ax = plt.subplots()
traj = [0]*5 # Je crée 5 emplacements mémoire pour les trajectoires
# D'abord je calcule psi
psi = fonction_courant(A,k,w,x,z,t_[0])

# Et ensuite je le plotte
line = ax.contour(x,z,psi,c='orange')
# Et puis je calcule U et V
U = U_vel(A,k,w,x,z,t_[0])
W = W_vel(A,k,w,x,z,t_[0])
# Et maintenant si je fais un quiver dedans
quiv =  ax.quiver(x[::5],z[::5],U[::5,::5],W[::5,::5],angles='xy',
          width=0.005,scale=100.)

# Enfin je plotte ma petite trajectoire, ou plutôt 5 trajectoires
for i in range(5):
    
    traj[i], = ax.plot(x_traj[i],z_traj[i])

plt.pause(0.1)
# Maintenant j'anime ça dans le temps
for t in t_[1:]:
    # Je recalcule psi et U et V
    psi = fonction_courant(A,k,w,x,z,t)
    U = U_vel(A,k,w,x,z,t)
    W = W_vel(A,k,w,x,z,t)
    
    # Et je mets à jour le graphique
    [tp.remove() for tp in line.collections[:]]# D'abord je l'efface
    line = ax.contour(x,z,psi,c='orange') # Et puis je le refais
    
    # Et là pareil pour le quiver
    quiv.set_UVC(U[::5,::5],W[::5,::5])
    
    # Et là c'est la boucle for de l'enfer
    for i in range(5):
        # Et là je recalcule ma trajectoire et je la met à jour
        x_,z_ = update_xz(x_traj[i][-1],z_traj[i][-1],A,k,w,t,delta_t)
        # Et je mets à jour
        x_traj[i].append(x_)
        z_traj[i].append(z_)
        # Et le dessin 
        traj[i].set_xdata(x_traj[i])
        traj[i].set_ydata(z_traj[i])
    # Et là je fais une petite pause
    plt.pause(0.1)