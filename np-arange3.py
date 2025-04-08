# maior valor, menor valor, e media array
import numpy as np

array = np.arange(20, -1, -1)
maior_numero = np.max(array)
menor_numero = np.min(array)
media = np.sum(array) / len(array)
print(array)
print(f'Maior valor: {maior_numero}, menor valor: {menor_numero}')
print(f'Média: {media}')

