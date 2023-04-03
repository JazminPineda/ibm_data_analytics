def currentMem(archivo_lect):
    with open(archivo_lect, "r+") as testwritefile:
        inactivos = []
        miembros = testwritefile.readlines()       
        # lista comprensiva= devuelve una lista de member cuando lo recorre y esta no dentro de la linea del miembro 
        #inactive = [member for member in members if ('no' in member)]
        for miembro in miembros:
            if 'no' in miembro:
                inactivos.append(miembro)
           
    return inactivos
                # print(miembro, end="")
            
def exRegis(archiv, lista):
    with open(archiv, "a+") as writefile:
        writefile.writelines(lista)
        #print(writefile.readlines())
    
            # if miembro not in writefile:
               
def cleanFiles(memReg, archiv2):
    lista_inactivos = currentMem(memReg)
    exRegis(archiv2, lista_inactivos)            
          

memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)

# print(miembro)#
