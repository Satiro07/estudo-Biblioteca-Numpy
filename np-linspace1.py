import numpy as np

array = np.linspace(1, 1000, 20)
print(f'array antes: ')
print(array.astype(int))

array_dedpois = array**2
print('Array depois:')
print(array_dedpois)