
import numpy as np
array = np.arange(1, 82).reshape(9,9)
print(array)


x = int(input('Valor x: '))
y = int(input('Valor y: '))
linha = (len(array)//2)-1
x1 = x
array_g = np.array([])
auxi = []
for i in range(0, 1):
    for i in range(1, y-1):
        aux = [i for i in array[x][x1:y+1]]
        auxi.append(aux)
        x += 1
    array_g = np.array(auxi)





print()
print(array_g)

# # array2 = np.array([array])