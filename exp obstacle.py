import numpy as np
import matplotlib.pyplot as plt


thetarad1 = np.radians([-80,-70,-60,-50,-40,-30,-20,-15,-10,-5,0,5,10,15,20,30,40,50,60,70,80])
thetarad2 = np.radians([-70,-60,-50,-40,-30,-20,-10,0,10,20,25,30,35,40,45,50,55,60,65,70])

veff_1 = np.array([3.26,2.7,2.18,3.3,2.6,4,5,5.2,5.5,5.8,5.9,5.8,5.4,4.9,3.2,2.4,1.75,2.55,3.4,3,3.1])
veff_2 = np.array([3.1,3.1,3.35,3.3,3.25,3,3.15,2.6,4,4.9,5.2,5.5,5.8,5.9,5.8,5.4,4.9,3.2,3.6,3.2])


intensite_1 = veff_1**2 /2
intensite_2 = veff_2**2 /2




ax = plt.subplot(111,projection='polar')
ax.plot(thetarad1, intensite_1, 'r-', label='obstacle en face', linewidth=1)       # x, y, couleur (- relié), taille
ax.plot(thetarad2, intensite_2, 'g-', label='obstacle à 40 degrés', linewidth=1)



ax.legend(loc="lower right", title="Légende", frameon=False)


ax.plot()

ax.set_title("Intensité (theta)", va='bottom')
ax.set_theta_zero_location("N")

plt.show()



#
#Calcul theta max
#

max1 = np.max(intensite_1)
max2 = np.max(intensite_2)

i,j = thetarad1[ np.where(intensite_1 == max1) ], thetarad2[ np.where( intensite_2 == max2) ]