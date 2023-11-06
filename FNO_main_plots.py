import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import scipy.optimize
#import matplotlib.patches as mpatches
#from array import array
#from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
#import matplotlib.image as image

## Primero leo los archivos
deltas = pd.read_csv('1422.dat',header=None,engine='python', delim_whitespace=True,dtype=float)

deleted = pd.read_csv('DELETED',header=None,engine='python', delim_whitespace=True,dtype=float)

## SIGMA 0.1
deltaE1_s1 = deltas[0]
deltaE2_s1 = deltas[1]
deleted_s1 = deleted[0]

## SIGMA 0.01
deltaE1_s2 = deltas[2]
deltaE2_s2 = deltas[3]
deleted_s2 = deleted[1]

## SIGMA 0.0
deltaE1_s3 = deltas[4]
deltaE2_s3 = deltas[5]
deleted_s3 = deleted[2]

correlacion = [80,90,95,97,99]

fig = plt.figure(figsize=(7,6))
ax1 = fig.add_subplot(111)

## Deltas E en eV de la doble excitada --> Con los 3 sigmas
ax1.plot(correlacion,deltaE2_s3, "|", label = "$n_N\\rightarrow \pi^{*} (\sigma=0.0)$", linewidth = 2, markersize=10, color = "blue")
ax1.plot(correlacion,deltaE2_s1, "_", label = "$n_N\\rightarrow \pi^{*} (\sigma=0.1)$", linewidth = 2, markersize=10, color = "blue")
ax1.plot(correlacion,deltaE2_s2, "x", label = "$n_N\\rightarrow \pi^{*} (\sigma=0.01)$", linewidth = 2, markersize=10, color = "blue")

## Deltas E en eV de la HL --> Con los 3 sigmas
ax1.plot(correlacion,deltaE1_s3, "|", label = "$\pi \\rightarrow \pi^{*} (\sigma=0.0)$", linewidth = 2, markersize=10, color = "red")
ax1.plot(correlacion,deltaE1_s1, "_", label = "$\pi \\rightarrow \pi^{*} (\sigma=0.1)$", linewidth = 2, markersize=10, color = "red")
ax1.plot(correlacion,deltaE1_s2, "x", label = "$\pi \\rightarrow \pi^{*} (\sigma=0.01)$", linewidth = 2, markersize=10, color = "red")

## Energía CASPT2
ax1.axhline(y=3.96,color='red',linestyle='--',linewidth=2)

ax1.axhline(y=4.92,color='blue',linestyle='--',linewidth=2)


## Energía RASPT2
x = np.arange(70.0, 120.2, 0.01)
ax1.fill_between(x, 5.55, 5.65,color='blue',linewidth=0,alpha=0.15)
ax1.fill_between(x, 4.59, 4.69,color='red',linewidth=0,alpha=0.15)

ax1.legend(loc='lower left',fontsize='small',ncol=2)

## Esto no sé qué es (creo que es el número de orbitales secundarios), pero a mi no me hace falta. El % yo lo cálculo directamente con el otro script
#sec = 69

## Aquí pone el segundo eje para representar los deleted orbitals
ax2=ax1.twinx()

ax2.plot(correlacion,deleted_s3,"|",color='Green',linewidth=1,markersize=10)
ax2.plot(correlacion,deleted_s1,"_",color='Green',linewidth=1,markersize=10)
ax2.plot(correlacion,deleted_s2,"x",color='Green',linewidth=1,markersize=10)

#ax2.plot(data2[0],data2[2],"--s",color='Blue',linewidth=1,alpha=0.3)

#ax2.plot(data_LiF_symm_CASPT2[0],data_LiF_symm_CASPT2[3],"o",color='darkgrey',linewidth=3)
ax2.set_ylabel("% Deleted Orbitals",color='Green',fontsize=16)

ax2.yaxis.set_tick_params(labelsize=14,width=2.5)
ax2.set_ylim(0,100)

ax1.yaxis.set_tick_params(labelsize=14,width=2.5)
ax1.xaxis.set_tick_params(labelsize=14,width=2.5)


#ax1.axhline(y=1.0,color='grey',linestyle='-',alpha=0.8)


for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(3)
    ax1.spines[axis].set_color("black")
    ax1.spines[axis].set_zorder(0)

ax1.set_xlabel('$\zeta$', fontsize = 16)
ax1.set_ylabel("$\Delta E$ (eV)", fontsize = 16)

#adding images for 2-enol-Ura

#file = "/home/juliana/FNO_paper/CADENAS/IMAGENES/buta_new.png"
#buta = image.imread(file)

#imagebox = OffsetImage(buta, zoom = 0.03)
#ab = AnnotationBbox(imagebox, (90, 6.5), frameon = False)#,zorder=-1)
#ax1.add_artist(ab)


plt.xlim(78,102)
#plt.show()
plt.savefig('Nucleoside_1422_DZ.png',transparent=True)

