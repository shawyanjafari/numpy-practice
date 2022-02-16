import numpy as np

# Remember how you can slice a list?
my_list = [4, 5, 6]
print(my_list[0:2])  # returns only 4 and 5

# You can also slice a ndarray!
# a[row][col]
# a[row,col]
a = np.array([[8, 5, 3], [7, 5, 6], [5, 5, 4]])
b = np.array([[1, 1, 1], [1, 1, 1]])
print(a[0][0:2])  # returns row 0, items in index 0 and 1
print(a[1][1:])  # prints 5 and 6
print(a[-1])  # returns last row
print(a[0:2, ])  # prints entirety of first two rows
print(a[..., 2])  # prints out tuple with last values in each row
print(a[2, ...])  # grabs everything in row at index 2

for row in a:
    print(row[2])  # prints last value in each row

print('')
for element in a.flat:
    print(element)
print('')

# you can vertically stack arrays
print(np.vstack((a, b)))
try:
    print(np.hstack((a, b)))  # won't work
except ValueError:
    print('This won\'t work because the matrices aren\'t the same height...')
