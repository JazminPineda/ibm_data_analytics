import requests
#librerias
import os 
from PIL import Image
from IPython.display import IFrame
url='https://www.ibm.com/'
r=requests.get(url)

# Respuesta obtención solicitud
r.status_code

# Encabezdos
r.request.headers
# Cuerpo de solicitud No hay nada
"request body:", r.request.body

#Encabezado de respuesta HTTP
header=r.headers
#print(r.headers)

# obtener la fecha de envío de la solicitud mediante la clave Date

#print(header['date'])

#Pede comprobar la codificación "encoding"
print(r.encoding)

# Como el tipo de contenido es texto/html, podemos usar el atributo
# texto para mostrar el HTML en el cuerpo, se trae los primeros 100 caracteres:
#print(r.text[0:100])

# traer imagenes

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
req_imagen=requests.get(url)
#Podemos mirar el encabezado de respuesta:

#
# print(req_imagen.headers)

print(req_imagen.headers['Content-Type'])