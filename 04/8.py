import numpy as np
import matplotlib.pyplot as plt

# Parametere
A = 1  # Amplitude
T = 2 * np.pi  # Periode
N = 50  # Antall termer i partialsummen
periods = 2  # Antall perioder å plotte

# Tidsvektor over flere perioder
t = np.linspace(0, periods * T, 1000)

# Sagtannbølgefunksjon som repeterer over flere perioder
def sawtooth_wave(t, T, A):
    return 2 * A / T * (t % T - T / 2)

# Beregning av Fourier-koeffisientene b_n
def b_n(n, A):
    if n == 0:
        return 0
    else:
        return -2 * A * (-1) ** n / (n * np.pi)

# Reell Fourier-rekke for sagtannbølgen
def fourier_series(t, N, T, A):
    f_t = np.zeros_like(t)
    for n in range(1, N + 1):
        bn = b_n(n, A)
        f_t += bn * np.sin(2 * np.pi * n * t / T)
    return f_t

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, sawtooth_wave(t, T, A), label='Sagtannbølge', color='blue')
plt.plot(t, fourier_series(t, N, T, A), label='Fourier-rekke N=' + str(N), linestyle='--', color='red')
plt.xlabel('Tid (t)')
plt.ylabel('Amplitude')
plt.title('Sagtannbølge og Fourier-rekke')
plt.legend()
plt.grid(True)
plt.savefig('sagtannbølge.png')
