import urllib.request

## descarga de archivo
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"
# nombre del archivo
filename = 'Example1.txt' 
urllib.request.urlretrieve(url, filename)


# instancia archivo 
file= open(filename, "r")
#leo el nombre desde el archivo
print(file.name)
# modo de lectura o escritura r o w
print(file.mode)
# lectura del contenido del archivo
fileContent = file.read()
print(fileContent)
# tipo del contenido 
print(type(fileContent), "tipo")

#cierro siempre archivo
file.close()