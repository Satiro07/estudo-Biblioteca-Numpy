import numpy as np
print('Matriz original')
array = np.arange(1, 26).reshape(5,5)
print('Matriz original')
print(array)
print()
print('Matriz com linhas invertidas')
matriz_linhas_invertidas = array[::-1]
print(matriz_linhas_invertidas)
print()
print('Matriz com colunas invertidas')
matriz_colunas_invertidas = array[:,::-1]
print(matriz_colunas_invertidas)