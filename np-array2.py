# multiplicar array por um número

import numpy as np

lista = [3, 6, 9, 12]
array_antes = np.array(lista)
array_depois = np.array(lista) * 2
print(f'Array antes: {array_antes}')
print(f'Array depois: {array_depois}')
