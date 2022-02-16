import numpy as np

a = np.arange(12).reshape(3, 4)
b = a > 6  # returns a mask of True/False values, similar to pandas filtering
print(b)

# extract elements that fulfill a certain criteria and/or replace them
print(a[b])  # looks at b and returns elements that match its criteria
a[b] = -1  # every element greater than 6 will be changed to -1
print(a)
