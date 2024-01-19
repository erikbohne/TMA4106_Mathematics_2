import numpy as np
import matplotlib.pyplot as plt

def S(x, N):
    s = np.zeros_like(x)
    for n in range(1, N+1):
        s += (2 * (-1)**(n+1) / n) * np.sin(n * x)
    return s

# Plotting
x = np.linspace(-np.pi, np.pi, 5000)
plt.plot(x, S(x, 5), label="N=5")
plt.plot(x, S(x, 25), label="N=25")
plt.plot(x, S(x, 5000), label="N=5000")
plt.xlabel('x')
plt.ylabel('S(x)')
plt.title('Fourier-rekke for Sagtannfunksjonen')
plt.legend()
plt.show()
