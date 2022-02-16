# numpy arrays require less memory
# numpy uses fixed types
# most useful feature is n dimensional array object -> ndarray

import numpy as np

my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(f'a: ')
print(my_array)
print(f'type of our_array is:\t\t{type(my_array)}')
print(f'dimensions of our_array:\t{my_array.ndim}')
print(f'shape of our_array is:\t\t{my_array.shape}')  # returns (row, col)

# basic array operations
# accessing items - a[row][col]
print(my_array[1][0])  # prints 1
print(my_array.itemsize)  # returns size of one element in bytes

z = np.zeros((3, 4))  # initializes array of zeroes, shaped passed as arg
print(z)

# you can also initialize a matrix with a range
# for a 2d array, use np.mgrid
array_range = np.arange(1, 5)  # array will have 1 -> 4, 5 not included
print(array_range)

# return a flattened array
print(my_array.ravel())  # does not alter array in place


# mathematical functions
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(b.min())
print(b.max())
print(b.sum())  # sums all number

#           Axis = 0
#           [1][2]
# Axis = 1  [3][4]
#           [5][6]

print(b.sum(axis=0))  # returns sum over column axis
print(b.sum(axis=1))  # returns sum over row axis

print(np.sqrt(b))  # sqrt is a function of the np module, it is not a ndarray method

# numpy also has various Statistic functions:
# https://numpy.org/doc/stable/reference/routines.statistics.html

print(np.median(b))
print(np.std(b))

# mathematical operations
s = np.array([[1, 2], [3, 4]])
t = np.array([[5, 6], [7, 8]])

print(s+t)
print(s*t)
print(s-t)
print(s.dot(t))  # you can even use matrix operations!

# There is, however, an entire library for matrix functions, too
# https://numpy.org/doc/stable/reference/routines.matlib.html#

print("")

# numpy also has built-in constants you can use:
our_float_array = np.array([2.1, 2.5, np.nan], dtype='float16')
print(our_float_array)
