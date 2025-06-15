# contar quantas vezes cada número aparece em um array de 50 números aleatórios de 1 até 6
import numpy as np
contados = []
array = np.random.randint(1, 7, size=(50))
print(array)
cont = 1
while True:
    contagem = 0
    if cont not in contados:
        contados.append(cont)
        for y in range(0, len(array)):
            if array[y] == cont:
                contagem += 1
        print(f'Número {cont} apareceu {contagem} vezes')
    cont+=1
    if cont > np.max(array):
        break