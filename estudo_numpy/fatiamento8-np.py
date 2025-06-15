import numpy as np
print('Matriz original')
array = np.arange(1, 101).reshape(10,10)
print(array)
print()
print('Zona superior esquerda')
superior_esquerdo = array[:5,:5]
print(superior_esquerdo)
print()
print('Zona superior direita')
superior_direito = array[:-5,-5:]
print(superior_direito)
print()
print('Zona inferior esquerda')
inferior_esquerdo = array[-5:,:5]
print(inferior_esquerdo)
print()
print('Zona inferior direita')
inferior_direito = array[-5:,-5:]
print(inferior_direito)