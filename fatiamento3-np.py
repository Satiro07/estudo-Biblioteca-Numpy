
import numpy as np
array = np.random.randint(1, 37, size=(9, 9))
print(array)
coluna = (len(array)// 2)-1
print(coluna)

linha = (len(array[0])//2)-1
print(linha)
x = int(input('Valor x: '))
y = int(input('Valor y: '))
array_g = np.array([])
for i in range(0, x):

    array_g = np.array([i for i in array[x][y:y+y]])
    x += 1





print()
print(array_g)

# # array2 = np.array([array])