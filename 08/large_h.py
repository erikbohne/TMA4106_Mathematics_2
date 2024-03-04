import numpy as np

# Definer matrisen A
alpha1 = 2
alpha2 = 1
A = np.array([[-alpha1, alpha1], [alpha2, -alpha2*2]])

print("Egenverdiene til A:", np.linalg.eigvals(A))

# Velg ulike stegstørrelser h
for h in [0.01, 0.1, 1, 10]:
    print(f"Stegstørrelse h = {h}")

    # Definer identitetsmatrisen I
    I = np.eye(2)

    # Beregn egenverdiene for I - hA
    eigvals = np.linalg.eigvals(I - h*A)

    # Skriv ut egenverdiene etter diagonalisering
    print("    Egenverdiene etter D:", eigvals)
