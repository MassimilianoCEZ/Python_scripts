#Farlo girare rispetto ad X

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


n = 100 # sono il numero di intervalli, per trovare la distanza tra un valore e l'altro fai la somma dei due
# e li dividi per n

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122,projection='3d')
x = np.linspace(np.pi/8, np.pi*4/5, n) #fa un array di valori da pi/8 a 4/5 pi (questo È theta comunque, l'angolo)
y = np.sin(x)
t = np.linspace(0, np.pi*2, n) #fa un altro array da 0 a pi/2

#fa dei cerchi, con il outer (prodotto diadico) e fa il prodotto raggio * sin o cos (ricorda il cerchio trigonometrico)
x_3d = np.outer(y, np.cos(t))
y_3d = np.outer(y, np.sin(t))
z_3d = np.zeros_like(x_3d) #prende una matrice e annulla tutti i valori, hai una matrice mxn = all'input ma con soli 0

for i in range(len(x)): #fa un ciclo della lunghezza degli elementi dell'array, se l'array (monodimensionali
    # se usi len (lenght) ) va da 3 a 9, sono 7 elementi quindi 7 iterazioni da i = (1,2,3,4,5,6,7)
    z_3d[i:i+1,:] = np.full_like(z_3d[0,:], x[i]) #il fulllike rende tutti i valori dell'array uguali al secondo argomento
    #il : significa che seleziona tutti gli elementi. zn[0,:] è utilizzato come array di riferimento. quella parte
    # seleziona tutti gli elementi della prima riga di zn  

ax1.plot(x, y)
ax2.plot_surface(x_3d, z_3d, y_3d)
plt.show()
