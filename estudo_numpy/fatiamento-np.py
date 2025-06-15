# cortar um array pela metade, deixar em 'dois pedaços' 
import numpy as np
array = np.arange(0, 20)
quantidade = len(array)/2
pedaco1 = array[0: int(quantidade)]
pedaco2 = array[int(quantidade):]
print(array)
print()
print('Primeiro pedaço')
print()
print(pedaco1)
print()
print('Segundo pedaço')
print()
print(pedaco2)
array_mult = pedaco1 * 2
print()
print('Pedaço um multiplicado por 2')
print()
print(array_mult)
print()
array_final = np.array([i for i in array_mult] + [n for n in pedaco2])
print('Array final')
print()
print(array_final)