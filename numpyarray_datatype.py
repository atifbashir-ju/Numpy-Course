#data type im numpy
# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex
# s for string
# m for timedelta
# o for object
# u for unicode string
# v - memory junck

import numpy as np
Atif = np.array([1, 2, 3, 4])
print(Atif.dtype)

import numpy as np
Atif = np.array(['Apple', 'banana', 'cherry'])
print(Atif.dtype)

import numpy as np
Atif = np.array([1, 2, 3, 4], dtype='S')
print(Atif)
print(Atif.dtype)


import numpy as np
Atif = np.array([1, 2, 3, 4], dtype = 'i4')
print(Atif)
print(Atif.dtype)


import numpy as np
Atif = np.array(['a', '2', ' 3'], dtype = 'i')
print(Atif)
print(Atif.dtype)

#converting data type in existing array - astype()
import numpy as np
Atif = np.array([1.1, 2.3, 56.6])
Atif1 = Atif.astype(int)
print(Atif1)
print(Atif1.dtype)


#conerting data type from integer to boolean
import numpy as np
Atif = np.array([1, 0, 3])
Atif1 = Atif.astype(bool)
print(Atif1)
print(Atif.dtype)

