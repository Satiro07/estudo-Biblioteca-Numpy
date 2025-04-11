# inverter a lista, remover os primeiros 2 nomes e os 2 ultimos
import numpy as np
lista = ['ana', 'bruno', 'carlos', 'jose', 'daniela', 'eduardo']
print('Lista original')
print()
print(lista)
print()
array = np.array(lista[::-1])
print('Lista invertida')
print()
print(array)
print()
c = len(lista)-2
cont = 0

for i in range(0, len(lista)):
    if cont <= 1:
        lista.remove(lista[c])
        cont += 1
        continue
    if cont == 2:
        for y in range(0, 2):
            lista.remove(lista[0])
        break
    
print('removendo os dois primeiros nomes e os dois ultimos')
print(lista)