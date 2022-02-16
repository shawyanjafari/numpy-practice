# numpy arrays require less memory

import numpy as np

our_array = np.array([[1, 2, 3], [4, 5, 6]])
print(f'a: ')
print(our_array)
print(f'type of our_array is:\t\t{type(our_array)}')
print(f'dimensions of our_array:\t{our_array.ndim}')
print(f'shape of our_array is:\t\t{our_array.shape}')
