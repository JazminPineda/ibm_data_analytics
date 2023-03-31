def currentMem(archivo_lect):
    with open(archivo_lect, "r+") as testwritefile:
        inactivos = []
        miembros = testwritefile.readlines()       
        for miembro in miembros:
            if 'no' in miembro:
                inactivos.append(miembro)
           
    return inactivos
                # print(miembro, end="")
            
def exReg(archiv, lista):
    with open(archiv, "a+") as writefile:
        writefile.writelines(lista)
        print(writefile.readlines())
    
            # if miembro not in writefile:
               
            
          

lista_inactivos = currentMem('members.txt')
print(lista_inactivos)
exReg('inactive.txt', lista_inactivos) 

# print(miembro)#
