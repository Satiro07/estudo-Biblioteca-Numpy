# substituir os 3 primeiros valores da diagonal

import numpy as np
array = np.random.randint(1, 21, size=(5,5))
print('Array original')
print()
print(array)
print()
cont = 0
for i in array:
    i[cont] = 99
    if cont == 2:
        break
    cont += 1
print('Array modificada')
print()
print(array)