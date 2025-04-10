# gerar 20 números aleatorios de 1 a 100, encontrar maior, minímo ,soma e a media
import numpy as np 
array = np.random.randint(1, 100, size=(20))
maior = np.max(array)
menor = np.min(array)
soma = np.sum(array)
media = np.mean(array)
print(array)
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Soma: {soma}')
print(f'Média: {media}')