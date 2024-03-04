import numpy as np
import matplotlib.pyplot as plt

#gitter
n=float(1000)
T=10
h=T/n
t=np.linspace(0,10,int(n))

#lÃ¸sning
x=np.zeros((int(n),2))

#initialverdier
x[0][0]=88
x[0][1]=4

#fysiske konstanter
drikketemp = 13
alpha = np.array([1,1])

#matriser for numerisk lÃ¸sning
A = np.array([[-alpha[0],alpha[0]],[alpha[0],-alpha[0]-alpha[1]]])
ekspl_mat = np.eye(2) + h*A
impl_mat = np.linalg.inv(np.eye(2) - h*A)
trap_mat = np.linalg.inv(np.eye(2) - h*A/2)@(np.eye(2) + h*A/2) 

#eksplisitt euler = ekspl_mat
#implisitt euler  = impl_mat
#trapesmetoden    = trap_mat
for i in range(int(n-1)):

    x[i+1]=trap_mat@x[i]

#plottings
plt.plot(t,x)
plt.plot(t,np.ones(int(n))*drikketemp)
plt.suptitle('HOMEOPATISKE FORVIKLINGER', fontsize=14, fontweight='bold')
plt.savefig('homeopati')
