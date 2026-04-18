#sipliting
import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6])
Atifnew = np.array_split(Atif, 3)
print(Atifnew)

import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6])
Atifnew = np.array_split(Atif, 4)
print(Atifnew)

import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6])
Atifnew = np.array_split(Atif, 3)
print(Atifnew[0])
print(Atifnew[1])
print(Atifnew[2])


import numpy as np
Atif = np.array([[1, 2],[3, 4], [5, 6], [7, 8], [9, 10], [11,12]])
Atifnew = np.array_split(Atif, 3)
print(Atifnew)

#hsplit()
import numpy as np
Atif = np.array([[1, 2],[3, 4], [5, 6], [7, 8], [9, 10], [11,12]])
Atifnew = np.hsplit(Atif,2)
print(Atifnew)
