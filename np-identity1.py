
import numpy as np
array = np.arange(1, 10)
array = array.reshape(3, 3)
print(array)
print()
array_inv = (array/array) *- 1
print(array_inv)
print()
produto = array * array_inv
print(produto)