import numpy as np 
import matplotlib.pyplot as plt

B = np.array([[1, 1], [1, 1], [-1, 1]])
A = np.array([[0, 1, 1], [1, 0, 1]])
Z = np.dot(A,B)
print(np.sin(Z))

# Usamos el atributo numpy T para calcular la matriz transpuesta
C = np.array([[1,1],[2,2],[3,3]])
C.T
