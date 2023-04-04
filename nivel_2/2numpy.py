import numpy as np
a=[1,2,3,4,5]

#Cambiar la lista a matriz 
x = np.array(a)
print(type(x)) # muestra tipo nunpy array
# Encuentre la forma de la matriz: muestra cuantos elementos hay en la dimension 0
print(x.shape)

# Tipo de datos en la matriz: aca muestra int 32
print(x.dtype)

# media o promedio 3
x.mean()