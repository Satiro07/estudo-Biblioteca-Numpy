# criar duas matrizes e somar as matrizes
import numpy as np
matriz1 = np.random.randint(1, 50, size=(3, 3))
print(matriz1)
print()
matriz2 = np.random.randint(1, 50, size=(3, 3))
print(matriz2)
soma_m = np.sum(matriz1,matriz2)
print()
print(f'Soma entre as matrizes 1 e 2: {soma_m}')