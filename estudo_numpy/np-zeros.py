# substituir elementos da diagonal (canto superior esquerdo ao inferior direito)
import numpy as np
array = np.zeros((3, 3))
print(f'Matriz inicial: \n{array}')
cont = 0
num = 1
for i in range(0, len(array)):
    array[cont][i] = num
    cont += 1
    num += 1
print(f'Array modificada: \n{array}')