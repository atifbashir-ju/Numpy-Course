#now we will numpy ndarray object
#the array object in numpy is called ndarray
import numpy as np
x = np.array([1, 2, 3, 4, 5])
print((x))
print(type(x))

#we can also pass a list using tuple or any array like object with array() 
import numpy as np
y = np.array((1, 2, 3, 4, 5))
print(y)
print(type(y))

#dimensions in arrays
# a dimensions in arrays is one level of array depth(netsed array)

# 0-D array- scalers, are the elements in an array, each value iin an array is a 0-D array 

#now we will create 0_D array with value 42
import numpy as np
x = np.array(42)
print(x)

#1-D array an array that has 0-D arrays as its elements is called uni directional or 1 -D

import numpy as np
Atif = np.array([1, 2, 3, 4, 5])
print(Atif)

#2-D array
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)

#3-D array
import numpy as np
x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(x)

#check how many dimension the array have: ndim atribute
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#create an array with five dimension and verify that it has five dimension

import numpy as np
Atif = np.array([1, 2, 3, 4, 5], ndmin=5)
print(Atif)
print('number of dimension: ', Atif.ndim)


