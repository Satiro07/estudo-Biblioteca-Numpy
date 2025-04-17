import numpy as np
print('Matriz original')
array = np.arange(1, 101).reshape(10,10)
print(array)
print()
print('Zona superior esquerda')
superior_esquerdo = array[:5,:5]
print(superior_esquerdo)