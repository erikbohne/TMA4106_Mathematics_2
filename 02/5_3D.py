import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definerer S(x, t, N) for Fourier-serien
def S(x, t, N):
    s = 0
    for k in range(1, N + 1, 2):
        bn = 8 / (np.pi * k**3)
        euler_factor = np.exp(-k**2 * t)
        s += bn * euler_factor * np.sin(k * x)
    return s

# Genererer data for 3D-plot
x = np.linspace(0, np.pi, 1000)
t = np.linspace(0, np.pi, 1000)  # t-akse fra 0 til pi sekunder
X, T = np.meshgrid(x, t)
Y = S(X, T, 10)  # Bruker N=10 for en mer detaljert sum

# Plotter i 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, Y, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('t (tid)')
ax.set_zlabel('S(x, t, 10)')

plt.savefig('5_3D.png')
