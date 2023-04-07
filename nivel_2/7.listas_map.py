import numpy as np
from functools import reduce

#Considera las listas [1, 2, 3, 4, 5] y [1, 0, 1, 0, 1]. 

def igualador(x,y):
    return x == y

def method_equal(l1, l2):
    equal = map(lambda x, y:x == y,  l1, l2)
    map(igualador,  l1, l2)
    result = reduce(lambda x, y: x and y, equal)
    return result and len(l1) == len(l2)

list1 =np.array([1, 2, 3, 4, 5])
list2 =np.array([1, 0, 1, 0, 1])

# prueba = method_equal(list1, list1)
# print(prueba)
print(list(map(igualador,  list1, list2)))


# validacion de cada elementoto 2
for i in range(len(list1)):
    print(igualador(list1[i], list2[i]), "validarion 2")

# cracion en una linea si son iguales 

print([list1[i] == list2[i] for i in range(len(list1))], "validarion 3")

# Metodo reforzado para multiplicar listas
def method_multiplicar(l1, l2):
    list3= [] 
    multiplicar = map(lambda x, y:x * y,  l1, l2)
    return list(multiplicar)
multi = method_multiplicar(list1, list2)
print(multi, "validarion 4")

list3= np.multiply(list1, list2)
print(list3)