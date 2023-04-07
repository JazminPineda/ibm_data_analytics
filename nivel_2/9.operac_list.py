import numpy as np

list1 = np.array([1, 2, 3])
list2 = np.array([8, 9, 10])

suma = np.add(list1, list2)
resta = np.subtract(list1, list2)
multiplic = np.multiply(list1, list2)
division = np.divide(list1, list2)
producto = np.dot(list1, list2)
print("suma", suma,"resta", resta,
"multipl", multiplic, "divis", division , "punto", producto)