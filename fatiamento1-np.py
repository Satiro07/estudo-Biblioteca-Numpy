

import numpy as np
array = np.random.randint(1, 21, size=(5,5))
print(array)
cont = 0
for i in array:
    i[cont] = 99
    cont += 1
print(array)