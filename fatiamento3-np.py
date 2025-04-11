
import numpy as np
array = np.random.randint(1, 37, size=(9, 9))
print(array)
array1 = np.array([i for i in array[3:6, 3]])

array2 = np.array([i for i in array[3][3:6]])

array_g = np.array([i for i in array[3:6, 3]] + [i for i in array[3][3:6]]).reshape(3, 2)
print(array1)
print(array2)
print()
print(array_g)

# array2 = np.array([array])