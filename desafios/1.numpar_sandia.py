from random import randint

"""

One hot summer day Pete and his friend Billy decided to buy a watermelon. 
They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, 
and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, 
however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon 
in such a way that each of the two parts weighs even number of kilos, at the same time it is not
 obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as
possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. 
For sure, each of them should get a part of positive weight."""

#w = int(input("Escribe el peso de su watermelon: "))


def generar_impares(n=8):
    numeros  = []
    while True:
        numeros = [randint(1, 100) for _ in range(n)]
        if all(x % 2 == 1 for x in numeros):# Para todos los elementos q son impares y se recorre para cada n de la lista 
            impares = numeros
           # si cumple la condicion se guarda el contenido de números
            break
    return impares

lista_impar = generar_impares()    
type( lista_impar)
for x in lista_impar:
    Billy = x + 1
    Pete = x - 1
 
    print(f"El total que pesa el watermelon es {Billy+Pete} kg,  Billy corresponde {Billy} partes, para Pete {Pete} partes")
    

    # if peso_cad % 2 != 0:
    #     Billy = peso_cad + 1
    #     Pete = peso_cad -1
    #     print(f"Se parte el watermelon para Billy {Billy} teniendo un peso total de {Pete}")
    # else:
    #     print(f"Las mitades no son pares {peso_cad}")

