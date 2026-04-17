#shape of an array: 

#now we will try to get the shape of an array.
import numpy as np
Atif = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(Atif.shape)

# (2,4) which means the array has two dimension and it has 4 elemnets

# 5-D array using ndmin:
import numpy as np
Atif = np.array([1, 2, 3, 4,], ndmin = 5)
print(Atif)
print('shape of array is: ', Atif.shape)
