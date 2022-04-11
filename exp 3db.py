"""
Tracer du diagramme de rayonnement
theta est l'angle polaire
Y20values : valeurs expérimentales de l'amplitude
"""
import numpy as np
import matplotlib.pyplot as plt

#
# Valeurs pour 7 émetteurs
#
theta=np.radians([-80,-70,-60,-50,-40,-35, -30, -25, -20,-15,-10,-5,0,5,10,15,20,25,30,35,40,50,60,70,80])
Y20values=[3, 2.4, 1.7, 0.8, 2.6, 2.65, 2.7, 3, 3.3, 3.7, 4.2, 4.7, 5.2, 4.5, 3.7, 3.35, 3, 2.55, 2.2, 2, 1.7, 2.1, 2, 1.8, 1.4]
Y20values_2 = [p**2 /2 for p in Y20values]


#
# Ouverture à 3 dB
#
Y20_max = np.max(Y20values_2)
i = np.where( Y20values_2 >= Y20_max/2 )
theta_3db_min = np.min( theta[i] )
theta_3db_max = np.max( theta[i] )
theta_3dB = ( theta_3db_max - theta_3db_min )*180/np.pi


#
# tracer du diagramme en puissance et de l'ouverture à 3 db
#

theta_3db_arc = np.linspace(theta_3db_min, theta_3db_max, 50)
ax = plt.subplot(111, projection="polar")
ax.plot(theta, Y20values_2)
ax.plot(theta_3db_arc, [Y20_max/2] * len(theta_3db_arc), "r")

ax.annotate(r"$\theta_{3dB} = $" + str(theta_3dB) + "°", xy=(theta_3db_min - 5 * np.pi / 180, Y20_max/2), ha="left", va="top",color="r",fontsize=12)

ax.plot(2 * [theta_3db_min], [0, Y20_max], "r", 2 * [theta_3db_max], [0, Y20_max], "r")
ax.set_theta_zero_location("N")

plt.show()

