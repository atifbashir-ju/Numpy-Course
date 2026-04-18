#now we will numpy ndarray object:-> it means creating N number of Arrays
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


import numpy as np
x = np.array(42)
print(x)

import numpy as np
Atif = np.array([1, 2, 3, 4, 5])
print(Atif)

import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)

import numpy as np
x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(x)

import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


import numpy as np
Atif = np.array([1, 2, 3, 4, 5], ndmin=5)
print(Atif)
print('number of dimension: ', Atif.ndim)

import numpy as np
Who = np.array([1, 2, 3, 4, 5], ndmin = 6)
print(Who)
print(Who.ndim)


