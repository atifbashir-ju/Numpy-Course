#1-D 
import numpy as np
Atif = np.array([1, 2, 3])
for i in Atif:
    print(i)

import numpy as np
Atif = np.array([[1, 2, 3], [4, 5, 6]])
for i in Atif:
    print(i)

#iterrate on each element
import numpy as np
Atif = np.array([[1, 2, 3,], [4, 5, 6]])
for i in Atif:
    for a in i:
        print(a)

import numpy as np
Atif = np.array([[[1, 2, 3],[4, 5, 6], [7, 8, 9,]]])
for i in Atif:
    for a in i:
        for b in a:
            print(b)
          

# iterating arrays using nditer() function.

import numpy as np
Atif = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
for i in np.nditer(Atif):
    print(i)


import numpy as np
Atif = np.array([[1, 2, 3, 4], [5, 6, 7, 9]])
for i in np.nditer(Atif[:, ::2]):
    print(i)

