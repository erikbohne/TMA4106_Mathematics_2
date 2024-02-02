import numpy as np
import matplotlib.pyplot as plt

# Parametere
N = 5  # Antall termer i Fourier-rekken

# Trekantbølgefunksjon
def triangle_wave(t):
    return np.pi - np.abs(t % (2 * np.pi) - np.pi)

# Beregning av Fourier-koeffisienter
def a_n(n):
    if n == 0:
        return np.pi**2 / 2  # Resultatet av integralet for a_0
    else:
        # Uttrykket for a_n etter å ha løst integralet, under bruk av symmetri og Fourier-analyse
        return ((-1)**n - 1) / (n**2) * 2

# Fourier-rekke for trekantbølgen
def fourier_series(t, N):
    f_t = np.zeros_like(t)
    for n in range(N + 1):
        f_t += a_n(n) * np.cos(n * t)
    return f_t / np.pi  # Normaliserer med perioden

# Tidsvektor
t = np.linspace(-5 * np.pi, 5 * np.pi, 1000)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, triangle_wave(t), label='Trekantbølge')
plt.plot(t, fourier_series(t, N), label=f'Fourier-rekke N={N}')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Trekantbølge og Fourier-rekke')
plt.legend()
plt.grid(True)
plt.savefig('trekantbølge.png')
