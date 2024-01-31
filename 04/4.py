import numpy as np
import matplotlib.pyplot as plt

# Definerer tidsdomenet
t = np.linspace(0, 4 * np.pi, 1000)  # 2 perioder for enkelthets skyld

def sawtooth_wave(N, t):
    sum = np.zeros_like(t)
    for n in range(1, N + 1):
        sum += ((-1) ** (n + 1)) * np.sin(n * t) / n
    return 2 / N * sum

def square_wave(N, t):
    sum = 0.5  # Startverdien for summen (likestrømskomponenten)
    for n in range(1, N + 1):
        sum += np.sin((2 * n - 1) * t) / (2 * n - 1)
    return sum * (4 / np.pi)

# Plotting for sagtannbølger for forskjellige verdier av N
plt.figure(figsize=(14, 8))
for N in [1, 3, 5, 10, 50]:
    plt.plot(t, sawtooth_wave(N, t), label=f'Sagtann N={N}')

plt.title('Sagtannbølger for forskjellige N')
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('sagtann.png')

# Plotting for firkantbølger for forskjellige verdier av N
plt.figure(figsize=(14, 8))
for N in [1, 3, 5, 10, 50]:
    plt.plot(t, square_wave(N, t), '--', label=f'Firkant N={N}')

plt.title('Firkantbølger for forskjellige N')
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('firkant.png')
