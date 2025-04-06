# filtrar números maiores que 10

import numpy as np

array = np.array([2, 4, 6, 8, 10, 12, 14, 16])
array_filtrado = np.array([i for i in array if i > 10]) # usando compreensão de lista

print(f'Array original: {array}')
print(f'Array filtrado: {array_filtrado}')