
import numpy as np
array = np.random.randint(1, 37, size=(9, 9))
print(array)
coluna = (len(array)// 2)-1
print(coluna)

linha = (len(array[0])//2)-1
print(linha)
array_g = np.array([i for i in array[coluna][linha:linha+3]] + [i for i in array[coluna+1][linha:linha+3]] + [i for i in array[coluna+2][linha:linha+3]]).reshape(3, 3)

print()
print(array_g)

# # array2 = np.array([array])