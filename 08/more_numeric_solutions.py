import matplotlib.pyplot as plt
import numpy as np

N = 100
T = 20
h = T/N
t = np.linspace(0, T, N)
x = np.zeros((2, N))

alpha1 = 2
alpha2 = 1

#---------------- Explicit Euler ----------------

x[:, 0] = [88, 4]

A = np.array([[-alpha1, alpha1], [alpha2, -alpha2*2]])
I = np.eye(2)

for i in range(1, N):
    x[:, i] = (I + h*A) @ x[:, i-1]
    
plt.plot(t, x[0, :], label='x1')
plt.plot(t, x[1, :], label='x2')
plt.legend()
plt.savefig('euler_explicit.png')

#---------------- Implicit Euler ----------------

x = np.zeros((2, N))
x[:, 0] = [88, 4]

for i in range(1, N):
    x[:, i] = np.linalg.inv(I - h*A) @ x[:, i-1]
    
plt.figure()
plt.plot(t, x[0, :], label='x1')
plt.plot(t, x[1, :], label='x2')
plt.legend()
plt.savefig('euler_implicit.png')

#---------------- Trapeziodal method ----------------
x = np.zeros((2, N))
x[:, 0] = [88, 4]

for i in range(1, N):
    x[:, i] = np.linalg.inv(I - (h/2)*A) @ (I + (h/2)*A) @ x[:, i-1]
    
plt.figure()
plt.plot(t, x[0, :], label='x1')
plt.plot(t, x[1, :], label='x2')
plt.legend()
plt.savefig('trapezoidal.png')
