import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Definer variabler og grid
x = np.linspace(-np.pi, np.pi, 100)  # x fra -pi til pi
t = np.linspace(0, 5, 100)  # t fra 0 til 5 sekunder
x, t = np.meshgrid(x, t)

c = 1  # Bølgehastighet
alpha = 0.5  # Dempingsrate
u = np.sin(x) * np.exp(-alpha * t) * np.cos(c * t)  # Dempet bølgefunksjon

# Opprett plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Overflateplot
surf = ax.plot_surface(x, t, u, cmap=cm.coolwarm)

# Merking av aksene
ax.set_xlabel('X Axis')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Damped Wave Function u(x, t)')

# Lagre figur
plt.savefig('damped_wave.png', dpi=300)
