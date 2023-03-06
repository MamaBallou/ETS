import math
import numpy as np
import matplotlib.pyplot as plt

# Définition de la fonction f(x,y)
def f(x, y):
    return x * y * np.exp(-1 * (x + y))

# Points A et B
A = (1, 1, math.exp(-2))
B = (1, 1, 0)

# Coordonnées x, y et z pour la fonction f(x,y)
x = y = np.arange(0.0, 2.0, 0.05)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Affichage de la fonction f(x,y) en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Change transparence map
ax.plot_surface(X, Y, Z, alpha=0.5)

# Affichage des points A et B
ax.scatter(A[0], A[1], A[2], c='r', marker='o')
# Add big annotation
ax.text(A[0], A[1], A[2], 'A', size=20, zorder=1, color='k')
ax.scatter(B[0], B[1], B[2], c='r', marker='o')

# Affichage du segment entre A et B
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], c='r')

# Paramètres de l'affichage
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# Change fig size
fig.set_size_inches(10, 10)
plt.show()