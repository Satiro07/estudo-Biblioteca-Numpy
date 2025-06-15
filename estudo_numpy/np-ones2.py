# mudando o centro da matriz
import numpy as np

array = np.ones((6, 6))
print('Matriz antes')
print(array)
print()

for i in range(1, len(array)-1):
    array[i][1:-1] = 0

print('Matriz modificada')
print(array)