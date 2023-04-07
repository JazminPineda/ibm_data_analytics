import numpy as np
from matplotlib import pyplot as plt


arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3 = np.add(arr1, arr2) #forma elegante

# Enter your code here
v = arr1 + arr2

print(arr3)


# Resta / sustraccion
a = np.array([10, 20, 30])
b = np.array([5, 10, 15])
c = np.subtract(a, b)

print(c)

# multiplicacion 
x = np.array([1, 2])
y = np.array([2, 1])

z= np.multiply(x, y)
print(z)

# division 
a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
c = np.divide(a, b)
print(c)




# Añadir constantes a una matriz Numpy
arr = np.array([1, 2, 3, -1]) 
arr1 = arr + 5
print(arr1)



# array numpy dentro de [5, 4] y 6 elementos Make a numpy array within [5, 4] and 6 elements

a = [5,4,5,4,5,4]
b = np.array(a)
print(type(b))

# Lo correcto es 
# Enter your code here
c = np.linspace(5, 4, num=6)
print(c)
