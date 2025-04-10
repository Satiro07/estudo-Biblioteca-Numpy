# adicionar uma constante a cada elemento na diagonal, somar matriz
import numpy as np

array = np.identity(5)
print(array)
print()
cont = 0
for i in array:
    i[cont] += 7
    cont += 1
print(array)
print()
soma = np.sum(array)
print(soma)