# gerar 20 números aleatorios de 1 a 100, encontrar maior, minímo ,soma e a media
import numpy as np 
array = np.random.randint(1, 100, size=(1,20))
maior = np.max(array)
menor = np.min(array)
print(array)