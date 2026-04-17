#slicing array- sllicing in pyhton means takking elemnt from one given index to another index

#now we will slice an element from 1 to 5:
import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(Atif[1:5])

#now we will slilce from index 4 to end value

import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(Atif[4:])

#now we will slice the element from the begining to index 4
import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(Atif[:4])

#negative slicing- index 3 to end
import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(Atif[-6:-1])

#step: we use step value to determine the step of the slicing
#return every other value from index 1 to 5

import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(Atif[1:5:2])

#now return every other number from the entire array 
import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(Atif[::2])

#2-D Array slicing print 7 8 9
import numpy as np
Atif = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(Atif[1, 1: ])

#another example:

import numpy as np
Atif = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(Atif[0:2, 2])

#another example print from both index 1:4
import numpy as np
Atif = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])    
print(Atif[0:2, 1:4])

