import numpy as np
import matplotlib.pyplot as plt

N = 1000
T = 20
h = T/N
t = np.linspace(0, T, N)
x = np.zeros((2, N))  # Combined state vector for x1 and x2
alpha1 = 2
alpha2 = 1

A = np.array([[-alpha1, alpha1], [alpha2, -alpha2*2]])

eigvals, eigvecs = np.linalg.eig(A)

# Initial conditions
x[:, 0] = [88, 4]  # [x1(0), x2(0)]

# Calculate the coefficients based on the initial conditions
# This involves solving c = V^-1 * x(0) where V is the matrix of eigenvectors
c = np.linalg.inv(eigvecs) @ x[:, 0]

for i in range(1, N):
    x[:, i] = c[0] * eigvecs[:, 0] * np.exp(eigvals[0] * t[i]) + c[1] * eigvecs[:, 1] * np.exp(eigvals[1] * t[i])

plt.plot(t, x[0, :], label='x1')
plt.plot(t, x[1, :], label='x2')
plt.legend()
plt.show()
