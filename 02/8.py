import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return x

def An(n):
    if n == 0:
        return np.pi**2 / 2
    else:
        return 2 * (np.pi*n*np.sin(np.pi*n) + np.cos(np.pi*n) - 1) / (n**2 * np.pi)
    
def S(x, t, N):
    s = 0
    for k in range(1, N + 1, 2):
        an = An(k)
        euler_factor = np.exp(-k**2 * t)
        s += an * euler_factor * np.cos(k * x)
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

plt.show()