import numpy as np

a = np.zeros((2, 2))
b = np.ones((2, 2))
c = np.concatenate((a, b), axis=0)
d = np.concatenate((a, b), axis=1)
# print(a)

# print(b)

print(c)

print(d)