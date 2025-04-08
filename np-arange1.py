import numpy as np

array_p = np.ones(int(5, 5))
array = np.arange(0, 21, 5)
for i in range(0, len(array_p)):
    array_p[i] = array
print(array_p)