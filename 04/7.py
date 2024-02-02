import numpy as np
import matplotlib.pyplot as plt

# Parametere
A = 1  # Amplitude
T = 2 * np.pi  # Periode, gjør dette for å forenkle beregningene
N = 10 # Antall termer i partialsummen

# Tidsvektor
t = np.linspace(-T, T, 1000)

# Firkantbølgefunksjon
def square_wave(t, T, A):
    return A * np.sign(np.sin(2 * np.pi * t / T))

# Beregn Fourier-koeffisienter for de odde harmonikkene
def fourier_coefficients(n, A):
    if n % 2 == 1:  # Bare for odde n
        return (4 * A) / (np.pi * n)
    else:
        return 0

# Rekonstruer firkantbølgen ved å bruke Fourier-rekken
def fourier_series(t, N, T, A):
    f_t = np.zeros_like(t)
    for n in range(1, N + 1, 2):  # Justert til å gå over oddetallene n
        c_n = fourier_coefficients(n, A)
        f_t += c_n * np.sin(2 * np.pi * n * t / T)
    return f_t

# Plot den originale firkantbølgen og Fourier-rekken
plt.figure(figsize=(10, 6))
plt.plot(t, square_wave(t, T, A), label='Firkantbølge')
plt.plot(t, fourier_series(t, N, T, A), label=f'Fourier-rekke, N={N}')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Firkantbølge og dens Fourier-rekke')
plt.legend()
plt.grid(True)
plt.savefig('firkantbølge.png')
