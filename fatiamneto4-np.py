
import numpy as np

matriz = np.arange(1, 37).reshape(6,6)
print(matriz)
array = matriz[::2,::2] # apenas linhas e colunas ímpares
print(array)