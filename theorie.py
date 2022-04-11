"""
trace le diagramme de rayonnement d'un réseau d'antennes
theta : angle polaire
Y20 : intensité ou éclairement
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv


def Y20(t):
    """ Calcul des valeurs de Y20 """
    N = 7
    n_air = 1
    lambda0 = 0.12
    d = lambda0 /4
    psi = np.pi*n_air*d/lambda0*np.sin(t)
    phi = 30*np.pi/180

    return ( np.cos(t)*(np.sin(N*(psi + phi/2))/(np.sin(psi + phi/2))) )**2

step = 1e-3
theta = np.arange(-180, 180, step)
Y20values = np.abs(Y20(theta))


ax = plt.subplot(111, projection="polar")
ax.plot(theta, Y20values)


ax.set_theta_zero_location("N")

plt.show()