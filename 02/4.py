import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * (np.pi - x)

def S(x, N):
    s = 0
    for k in range(1, N + 1, 2):
        s += 8 / (np.pi * k**3) * np.sin(k * x)
    return s

# Plot f(x)
x = np.linspace(0, np.pi, 1000)
y = f(x)
plt.plot(x, y, label = 'f(x) = x(pi - x)')

# Plot partial sums
plt.plot(x, S(x, 1), label = 'N = 1', linestyle = '--')
plt.plot(x, S(x, 2), label = 'N = 2', linestyle = ':')
plt.plot(x, S(x, 3), label = 'N = 3', linestyle = '-.')
plt.legend()
plt.show()

