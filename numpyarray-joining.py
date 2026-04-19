import numpy as np
Atif = np.array([1, 2, 3])
Atif1 = np.array([4, 5, 6])
Atif2 = np.concatenate((Atif, Atif1))
print(Atif2)

import numpy as np
Atif = np.array([[1, 2, 3], [4, 5, 6]])
Atif1 = np.array([[7, 8, 9], [10, 11, 12]])
Atif2 = np.concatenate((Atif, Atif1), axis = 1 )
print(Atif2)

import numpy as np
Atif = np.array([1, 2, 3 ])
Atif1 = np.array([4, 5, 6])
Atif2 = np.stack((Atif, Atif1), axis = 1)
print(Atif2)

# hstack()
import numpy as np
Atif = np.array([1, 2, 3])
Atif1 = np.array([4, 5, 6])
Atif2 = np.hstack((Atif, Atif1))
print(Atif2)

import numpy as np
Atif = np.array([1, 2, 3])
Atif1 = np.array([4, 5, 6])
Atif2 = np.vstack((Atif, Atif1))
print(Atif2)

import numpy as np
Atif = np.array([1, 2, 3])
Atif1 = np.array([4, 5, 6])
Atif2 = np.dstack((Atif, Atif1))
print(Atif2)

