import numpy as np
from matplotlib import pyplot as plt


# Funciones Universales

# The value of pi
np.pi
# Create the numpy array in radians
a = np.array([0, np.pi/2 , np.pi])
b = np.sin(a)
plt.plot(a, b)
plt.show() #mostrar


# Linspace devuelve números espaciados
## Make a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)

y = np.sin(x)
plt.plot(x, y)
plt.show() #mostrar


