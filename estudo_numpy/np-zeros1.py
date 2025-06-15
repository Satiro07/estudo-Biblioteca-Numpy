# formar borda array

import numpy as np 
array = np.zeros((10, 10))
print('Array inicial:')
print(array)

for i in range(0, len(array)):
    array[i][0] = 255
    array[i][-1] = 255
    
array[0] = 255
array[-1] = 255
print('Array modificada:')
print(array)