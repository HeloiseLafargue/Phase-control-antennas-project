## Diagramme de rayonnement pour 7 émetteurs avec déphasage (expérience)

import numpy as np
import matplotlib.pyplot as plt


thetarad = np.radians([-80,-75,-70,-65,-60,-55,-50,-45,-40,-35, -30, -25, -20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80])


veff_50 = np.array([3.1, 2.9, 2.7, 3.1, 3.4, 4.2, 5.15, 6, 6.6, 6.9, 6.9, 6.45, 5.9, 5.2, 4.7, 4.2, 4.05, 3.9, 4.1, 3.75, 3.6, 3.4, 2.9, 3, 3.1, 3.25, 2.95, 3.75, 4.2, 5.05, 5.5, 4.9, 5.5])


veff_30 = np.array( [4, 3.85, 3.7, 3.4, 3, 2.5, 1.9, 2.4, 3.2, 4.8, 5.9, 6.3, 6.7, 6.6, 6.2, 5.8, 5.4, 5.1, 4.8, 4.45, 4.1, 3.7, 3.3, 3.05, 2.8, 2.4, 2, 2.35, 2.9, 3.1, 3.3, 3.2, 3.1 ])


intensite_50 = veff_50*veff_50 / 2
intensite_30 = veff_30*veff_30 / 2

ax = plt.subplot(111,projection='polar')

ax.plot(thetarad, intensite_50, 'b-', label='7 émetteurs, déphasage de 50 degrés', linewidth=1)
ax.plot(thetarad, intensite_30, 'r-', label='7 émetteurs, déphasage de 30 degrés', linewidth=1)

ax.legend(loc="lower right", title="Légende", frameon=False)

ax.plot()

ax.set_title("Intensité (theta)", va='bottom')
ax.set_theta_zero_location("N")

plt.show()