import numpy as np

# you can specify the type of the elements, too.
# there are methods for manipulating strings:
a = np.array([['cat', 'dog', 'frog'], ['tiger', 'bear', 'giraffe']], dtype='str')
print(np.char.chararray.upper(a))
