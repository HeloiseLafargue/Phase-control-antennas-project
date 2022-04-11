## Diagramme de rayonnement pour 1,3,5,7 émetteurs (expérience)

import numpy as np
import matplotlib.pyplot as plt


thetarad = np.radians([-80,-70,-60,-50,-40,-35, -30, -25, -20,-15,-10,-5,0,5,10,15,20,25,30,35,40,50,60,70,80])


veff_1 = np.array([0.9, 0.8, 0.85, 1, 1.4, 1.35, 1.3, 1.4, 1.5, 1.7, 1.9, 2.1, 2.2, 2, 1.7, 1.6, 1.5, 1.4, 1.3, 1.25, 1.2, 1.2, 1.3, 1, 0.85])
veff_3 = np.array([1.75, 1.7, 1.8, 2.3, 2.6, 2.45, 2.4, 2.4, 2.5, 2.6, 2.8, 2.9, 2.95, 2.75, 2.6, 1.1, 1.8, 1.75, 1.7, 1.35, 1, 0.8, 1, 1.3, 1.15])
veff_5 = np.array([2.5, 1.9, 1.4, 0.7, 1.1, 1.4, 2, 2.3, 2.7, 2.9, 3.2, 3.7, 4.2, 4.5, 4.4, 4.1, 3.7, 3.2, 2.5, 2.1, 1.8, 1.7, 2, 1, 0.7])
veff_7 = np.array([3, 2.4, 1.7, 0.8, 2.6, 2.65, 2.7, 3, 3.3, 3.7, 4.2, 4.7, 5.2, 4.5, 3.7, 3.35, 3, 2.55, 2.2, 2, 1.7, 2.1, 2, 1.8, 1.4])

intensite_1 = veff_1**2 /2
intensite_3 = veff_3**2 /2
intensite_5 = veff_5**2 /2
intensite_7 = veff_7**2 /2

ax = plt.subplot(111,projection='polar')
ax.plot(thetarad, intensite_1, 'r-', label='1 émetteur', linewidth=1)       # x, y, couleur (- relié), taille
ax.plot(thetarad, intensite_3, 'g-', label='3 émetteurs', linewidth=1)
ax.plot(thetarad, intensite_5, 'm-', label='5 émetteurs', linewidth=1)
ax.plot(thetarad, intensite_7, 'b-', label='7 émetteurs', linewidth=1)

ax.legend(loc="lower right", title="Légende", frameon=False)

ax.plot()

ax.set_title("Intensité (theta)", va='bottom')
ax.set_theta_zero_location("N")

plt.show()
