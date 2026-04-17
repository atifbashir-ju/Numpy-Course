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

#checking the data type of numpy array
import numpy as np
Atif = np.array([1, 2, 3, 4])
print(Atif.dtype)


#checking the data type of numpy array-string
import numpy as np
Atif = np.array(['Apple', 'banana', 'cherry'])
print(Atif.dtype)

#creating array with a defined data type:
import numpy as np
Atif = np.array([1, 2, 3, 4], dtype='S')
print(Atif)
print(Atif.dtype)

#now we will create an array with data type of 4 byte int:
import numpy as np
Atif = np.array([1, 2, 3, 4], dtype = 'i4')
print(Atif)
print(Atif.dtype)

#if a type is given in which the element cannot be casted then numpy will raise error. what if a value cannot be converted?


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

