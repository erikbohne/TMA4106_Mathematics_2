import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * (np.pi - x)

def S(x, t, N):
    s = 0
    for k in range(1, N + 1, 2):
        bn = 8 / (np.pi * k**3)
        euler_factor = np.exp(-k**2 * t)
        s += bn * euler_factor * np.sin(k * x)
    return s

# Plot for different values of t
x = np.linspace(0, np.pi, 1000)
y = f(x)

plt.plot(x, y, label = 'f(x) = x(pi - x)')
plt.plot(x, S(x, 0.1, 3), label = 't = 0.1')
plt.plot(x, S(x, 0.5, 3), label = 't = 0.5')
plt.plot(x, S(x, 1, 3), label = 't = 1')
plt.legend()
plt.savefig('5.png')
