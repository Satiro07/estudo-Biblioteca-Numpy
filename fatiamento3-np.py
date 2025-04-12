
import numpy as np
array = np.random.randint(1, 37, size=(9, 9))
x = int(input('Valor x: '))
y = int(input('Valor y: '))
print(array)
array_g = np.array([])
auxi = []
for i in range(0, 1):
    
    for i in range(0, x):
        aux = [i for i in array[x-1][x:y]]
        auxi.append(aux)
        x += 1
    array_g = np.array(auxi)





print()
print(array_g)

# # array2 = np.array([array])