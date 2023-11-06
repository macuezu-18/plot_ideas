## python3 time_plots_FNO.py

import matplotlib.pyplot as plt

## TIEMPOS
## DZ
originales=[0.93,3.39,12,55.78,245.56,362.96]
acelerados=[0.5,2.26,8.56,25.92,34.16,87.27]
acelerados_97=[0.53,2.53,9.36,28.27,41.38,105.02]

## TZ
originales_TZ=[10.79,45.05,132.35,400.95,1457.92,2000]
acelerados_TZ=[8.68,22.27,124.1,173.25,253.02,517.56]
acelerados_97_TZ=[9.86,24.24,124.51,216.54,297.91,609.39]

carbonos = [4,6,8,10,12,14]

x_new = [1,2,3,4,5,6]

carbonos_or =[]
carbonos_ac =[]
carbonos_ac2 =[]

for x in x_new:
    new = x-0.4
    new2 = x+0.2
    new3 = x-0.1
    carbonos_or.append(new)
    carbonos_ac.append(new2)
    carbonos_ac2.append(new3)

fig = plt.figure(figsize=(7,6))
ax1 = fig.add_subplot(111)

## Deltas E en eV de la doble excitada --> Con los 3 sigmas
ax1.bar(carbonos_or,originales_TZ,color='blue', width=0.3,
        label='Full-RASPT2 ANO-L-VTZP',edgecolor='k',alpha=0.5,hatch="x")
ax1.bar(carbonos_ac2,acelerados_97_TZ, width=0.3, color ='purple',
        label='FNO-RASPT2 ANO-L-VTZP ($\zeta = 0.97$)',edgecolor='k',
        alpha=0.5,hatch="x")
ax1.bar(carbonos_ac,acelerados_TZ, width=0.3, color ='red',
        label='FNO-RASPT2 ANO-L-VTZP ($\zeta = 0.95$)',edgecolor='k',
        alpha=0.5,hatch="x")

ax1.bar(carbonos_or,originales,color='blue', width=0.3,
        label='Full-RASPT2 ANO-L-VDZP',edgecolor='k')
ax1.bar(carbonos_ac2,acelerados_97, width=0.3, color ='purple',
        label='FNO-RASPT2 ANO-L-VDZP($\zeta = 0.97$)',edgecolor='k')
ax1.bar(carbonos_ac,acelerados, width=0.3, color ='red',
        label='FNO-RASPT2 ANO-L-VDZP ($\zeta = 0.95$)',edgecolor='k')

ax1.yaxis.set_tick_params(labelsize=14,width=2.5)
ax1.xaxis.set_tick_params(labelsize=14,width=2.5)



for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(3)
    ax1.spines[axis].set_color("black")
    ax1.spines[axis].set_zorder(0)

ax1.set_xlabel('# Carbon atoms', fontsize = 16)
ax1.set_ylabel("Time (s)", fontsize = 16)
plt.xticks([1,2,3,4,5,6],['4','6','8','10','12','14'],rotation=0)


######################################################################
## INSET con zoom a buta y hexa
x1, x2, y1, y2 = 0.4, 3.4, 0, 5  # subregion of the original image
axins = ax1.inset_axes(
    [0.2, 0.4, 0.35, 0.2],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.bar(carbonos_or, originales_TZ, color='blue', width=0.3,edgecolor='k',
          alpha=0.5,hatch="x")
axins.bar(carbonos_ac, acelerados_TZ, width=0.3, color='red',edgecolor='k',
          alpha=0.5,hatch="x")
axins.bar(carbonos_ac2, acelerados_97_TZ, width=0.3, color='purple',
          edgecolor='k',alpha=0.5,hatch="x")

axins.bar(carbonos_or, originales, color='blue', width=0.3,edgecolor='k')
axins.bar(carbonos_ac, acelerados, width=0.3, color='red',edgecolor='k')
axins.bar(carbonos_ac2, acelerados_97, width=0.3, color='purple',edgecolor='k')

axins.set_xticks([1,2])  # Establecer los ticks manualmente
axins.set_yticks([0,2.5,5])  # Establecer los ticks manualmente
x_ticks_labels = ['4', '6']
y_ticks_labels = ['0', '2.5', '5']
#y_ticks_labels = ['0', '10', '20','30','40','50']
axins.set_xticklabels(x_ticks_labels)
axins.set_yticklabels(y_ticks_labels)

ax1.indicate_inset_zoom(axins, edgecolor="black")

## INSET con zoom a buta y hexa
x1, x2, y1, y2 = 0.4, 3.4, 5, 140  # subregion of the original image
axins2 = ax1.inset_axes(
    [0.2, 0.62, 0.35, 0.2],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins2.bar(carbonos_or, originales_TZ, color='blue', width=0.3,edgecolor='k',
           alpha=0.5,hatch="x")
axins2.bar(carbonos_ac, acelerados_TZ, width=0.3, color='red',edgecolor='k',
           alpha=0.5,hatch="x")
axins2.bar(carbonos_ac2, acelerados_97_TZ, width=0.3, color='purple',
           edgecolor='k',alpha=0.5,hatch="x")

axins2.bar(carbonos_or, originales, color='blue', width=0.3,edgecolor='k')
axins2.bar(carbonos_ac, acelerados, width=0.3, color='red',edgecolor='k')
axins2.bar(carbonos_ac2, acelerados_97, width=0.3, color='purple',
           edgecolor='k')

axins2.set_xticks([1,2])  # Establecer los ticks manualmente
axins2.set_yticks([40,80,120])  # Establecer los ticks manualmente
x_ticks_labels2 = ['4', '6']
y_ticks_labels2 = ['40','80','120']
#y_ticks_labels = ['0', '10', '20','30','40','50']
axins2.set_xticklabels(x_ticks_labels2)
axins2.set_yticklabels(y_ticks_labels2)

axins2.spines['bottom'].set_visible(False)
axins.spines['top'].set_visible(False)
axins2.tick_params(axis='x',which='both',bottom=False,top=False,
                   labelbottom=False)
#ax1.indicate_inset_zoom(axins2, edgecolor="black")


d = .02  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=axins2.transAxes, color='k', clip_on=False)
axins2.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
axins2.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=axins.transAxes)  # switch to the bottom axes
axins.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
axins.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal


######################################################################

#ax1.text(6., 350, '(a)',fontsize=25)
#ax1.text(0.2, 1900, '(b)',fontsize=25)

plt.legend(loc='best',ncol=2,fontsize='small')
#plt.show()
plt.savefig('TIEMPOS_Stag.png',transparent=True)
#plt.savefig('TIEMPOS_TZ.png',transparent=True)

