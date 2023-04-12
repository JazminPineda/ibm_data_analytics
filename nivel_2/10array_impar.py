import numpy as np



#print([list1[i] == list2[i] for i in range(len(list1))], "validarion 3")

# Metodo reforzado para multiplicar listas

# def impar(x):
#     if x % 2 == 1:
#         return x
     
def method_evaluar(l1, l2):
    l3 = np.concatenate((l1, l2), axis=0)
    print(l3)
    evalua = map(lambda x, y : (x, y) % 2 == 1,  l3)
    impares = [numero for numero in l3 if numero % 2 == 1]
    pares = [numero for numero in l3 if numero % 2 == 0] # resto
    print(impares, pares)

arr1 = np.array([1, 2, 3, 4, 5]) 
arr2 = np.array([6, 7, 8, 9, 10]) 

method_evaluar(arr1, arr2)

