# elementos igualmente espaçados, soma so array, e produto do array
import numpy as np

array = np.linspace(0, 100, 10)
soma = np.sum(array)
produto = 1
for i in array:
    produto *= i
print(array)
print(f'Soma do array: {soma}')
print(f'Produto do array: {produto}')
