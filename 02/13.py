import numpy as np
import matplotlib.pyplot as plt

def S(t, N):
    s = 0
    for k in range(1, N + 1):
        if k % 2 != 0:  # Sjekker om k er et oddetall
            s += (2/(np.pi*k)) * np.sin(k * t)
        
    return s + 0.5

t = np.linspace(-np.pi, np.pi, 1000)
plt.plot(t, S(t, 1), label='N = 1')
plt.plot(t, S(t, 3), label='N = 3')
plt.plot(t, S(t, 5), label='N = 5')
plt.plot(t, S(t, 100), label='N = 100')
plt.xlabel('t')
plt.ylabel('S(t)')
plt.title('Fourier-rekke til Enhetssprangfunksjonen')
plt.legend()
plt.show()
