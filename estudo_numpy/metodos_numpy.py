import numpy as np
array = np.arange(1, 82).reshape(9,9)
print(array)
print(np.diag(array)) # pega a diagonal de um array
print(np.flip(array)) # inverte o array
divi = np.split(array, 3) # divide o array
print(divi)
array1 = np.arange(1, 10)
array2 = np.arange(5, 10)
print(np.concatenate((array1, array2))) # junta arrays
print(np.ravel(array)) # transforma um array com várias dimensões em um com apenas uma dimensão

axis=0 # vertical
axis=1 # horizontal
