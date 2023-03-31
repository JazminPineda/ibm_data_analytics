# Todos los meses actualizan el archivo eliminando a los miembros que no están activos. 
# Se le ha asignado la tarea de automatizar esto con sus habilidades de Python.

# Dado el archivo currentMem, elimine cada miembro con un 'no' en su columna Activo.
# Realice un seguimiento de cada uno de los miembros eliminados y agréguelos al archivo exMem.
# Asegúrese de que se conserve el formato de los archivos originales
#(Sugerencia: haga esto leyendo/escribiendo líneas completas y asegurándose de que el encabezado permanezca)

#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)