# criar duas matrizes e somar as matrizes (formando uma matriz final)
import numpy as np
matriz1 = np.random.randint(1, 50, size=(3, 3))
print(f'Matriz 1: \n{matriz1}')
print()
matriz2 = np.random.randint(1, 50, size=(3, 3))
print(f'Matriz 2: \n{matriz2}')
soma_m = matriz1 + matriz2
print()
print(f'Soma entre as matrizes 1 e 2: \n{soma_m}')