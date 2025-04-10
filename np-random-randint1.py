# 'simulação' de dados, media cada aluno, aluno com maior nota
import numpy as np
array = np.random.randint(0, 10, size=(5, 10))
cont = 1
print(array)
nome_maior = ''
media_maior = 0
for i in array:
    media = np.mean(i)
    print(f'Aluno {cont}: {media}')
    if media > media_maior:
        nome_maior = (f'Aluno {cont}')
        media_maior = media
    cont += 1
print()
print(f'{nome_maior} (média: {media_maior})')
