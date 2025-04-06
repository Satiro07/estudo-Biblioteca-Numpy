# acessar elementos específicos (fatiamento)

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(f'Array: {array}')

pos = 5
print(f'Número na posição {pos}: {array[5]}')

inicio = 10
fim = 15
print(f'Elementos da {inicio}° posição até {fim}° posição: {array[inicio:fim]}')

array[-1] = 99
print(array)