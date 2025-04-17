
import numpy as np
array = np.arange(1, 82).reshape(9,9)
print(array)
print()

x = int(input('Valor x: '))
y = int(input('Valor y: '))
array = array[x:y+1,x:y+1]
print(array)
print()

array2 = np.flip(array[::-1]) # inverte começando do final da array (porém, não fica na mesma colna)

array_invertida = np.flip(array2) # inverte deixando o número na mesma coluna
print(array_invertida)