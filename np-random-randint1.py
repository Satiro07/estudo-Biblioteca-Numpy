# 'simulação' de dados, media cada aluno, aluno com maior nota
import numpy as np
array = np.random.randint(0, 10, size=(5, 10))
cont = 1
print(array)
for i in array:
    media = np.mean(i)
    print(f'Aluno {cont}: {media}')
    cont += 1
