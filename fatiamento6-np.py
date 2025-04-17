import numpy as np
print('Matriz original')
array = np.random.randint(1, 101, size=(4,5))
print(array)
print()
print('Matriz modificada')
matriz = array[:,-1:]
matriz1 = array[:,:-1]

matriz_modificada = np.concatenate((matriz, matriz1),axis=1)
print(matriz_modificada)