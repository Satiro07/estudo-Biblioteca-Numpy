# operações em arrays multidimensionais
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array)

print(f'Soma dos elementos da primeira linha: {sum(array[0])}')
print(f'Soma dos elementos da segunda linha: {sum(array[1])}')
print(f'Soma dos elementos da terceira linha: {sum(array[2])}')

array[1][1] = 0
print(f'Trocar valor central por 0: \n{array}')