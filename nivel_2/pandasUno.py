import pandas as pd

# df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
# df['a']==1
# print(df)


# 1. almacena ruta
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# 2. se lee el csv y se guarda en OBJETO df
df = pd.read_csv(csv_path)

# lectura 5 primeros con encabezado
print(df.head())

# Acceso a la columna Longitud
x = df[['Length']]

# hace lo mismo pero no imprime encabezado solo los datos 
x1 = df['Length']
x1
#print(x1)

#Get the column as a dataframe Obtenga la columna como un marco de datos
# Access to multiple columns

y = df[['Artist','Length','Genre']]
#print(y)

# Access the value on the first row and the first column

# print(df.iloc[1,0]) #acdc 2 element
# print(df.iloc[0, 3])
print(df.iloc[0,2])