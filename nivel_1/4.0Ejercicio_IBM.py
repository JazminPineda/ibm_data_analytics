import urllib.request

# nombre del archivo
filename = 'Example1.txt' 

# urllib.request.urlretrieve(url, filename)

# Leer mas eficiente el archivo
# with open(filename, "r") as file:
    # FileContent = file.read()
    # print(FileContent)


# Leer cierta cantidad de caracteres

    # print(file.read(2))
    # print(file.read(1))
    # print(file.read(5))
    # print(file.read(20))

# leer una linea  4 ejercicio
# with open(filename, "r") as file:
#     print(file.readline(10)) #no lee más allá del final de la línea, solo los 10 caracteres 
#     print(file.read(33)) # Devuelve los siguientes 33 caracteres.


#Iterar a través de las líneas
# with open(filename, "r") as file:
#     i = 0
#     for line in file:
#         print("Iteration", str(i), ":", line)
#         i += 1

# Usando el metodo readlines() Lea todas las líneas y guárdelas como una lista
with open(filename, "r") as file:
    fileaslist = file.readlines()
# Cada elemento de la lista corresponde a una línea de texto:
print(fileaslist[2])