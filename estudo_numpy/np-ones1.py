# pontos jogadores np.ones()

import numpy as np
from random import randint

array = np.ones((2, 5))
cont = 1
array[1] = 10
for i in range(0, len(array[0])):
    array[0][i] = cont
    cont += 1
print(array)

for i in range(0, 3):
    print(f'Pontos na rodada {i+1}')
    for y in range(0, 5):
        pontos = randint(-50, 50)
        palavra = 'perdeu'
        if pontos > 0:
            palavra = 'ganhou'
        print(f'Jogador {array[0][y]:.0f} {palavra} {pontos} pontos')
        array[1][y] += pontos
    print()
    
ganhador = 0
pontos = 0
for i in range(0, 5):
    if array[1][i] > pontos:
        ganhador = array[0][i]
        pontos = array[1][i]
    
print(f'Tabela final:')
print(array)
print()
print(f'Ganhador: jogador {ganhador:.0f} - pontos: {pontos:.0f}')
