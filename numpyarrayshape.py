#shape of an array: 
import numpy as np
Atif = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(Atif.shape)

import numpy as np
Atif = np.array([1, 2, 3, 4,], ndmin = 5)
print(Atif)
print('shape of array is: ', Atif.shape)

#flattening
import numpy as np
Atif = np.array([[1, 2, 3], [4, 5, 6]])
Atif1 = Atif.reshape(-1)
print(Atif1)

#there are a lot of function for changing the shape on an array in numpy like flatten, revel, and aslo rearranging the element rot90, glip, flipr, flipud: they all are actually comes from advanced numpy
