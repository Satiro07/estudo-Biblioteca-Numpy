import numpy as np


array = np.ones((4, 4))
print('Matriz inicial')
print(array)
print()
for i in range(0, len(array)):
    array[i] *= i+1
print('Matriz final')
print(array)
