def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
            members.pop(0)
                
            inactive = [member for member in members if ('no' in member)]
            '''
            The above is the same as 

            for member in members:
            if 'no' in member:
                inactive.append(member)
            '''
            #go to the beginning of the write file
            writeFile.seek(0) #vuelve al principio del archivo del miembros activos
            writeFile.write(header) # sobreeescbie el encabezado
            for member in members: # recorre la misma lista 
                if (member in inactive):
                    appendFile.write(member) # separa los inactivos, si esta en la lista lo escribe
                else:
                    writeFile.write(member)  # rescribe los activos
            writeFile.truncate()
                
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)