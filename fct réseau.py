"""
Trace la fonction réseau pour N émetteurs
"""

import numpy as np
import matplotlib.pyplot as plt


N1 = 10
N2 = 5

theta = np.linspace(-np.pi + 1, np.pi - 1, 100)

f1 = np.sin(N1 * theta)/ np.sin(theta)
f2 = np.sin(N2 * theta)/ np.sin(theta)

plt.plot(theta, f1, label="10 émetteurs")
plt.plot(theta, f2, label="5 émetteurs")

plt.title("Fonction réseau sin(Nx)/sin(x)")
plt.legend()
plt.show()

