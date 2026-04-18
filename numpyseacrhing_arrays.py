#searching Array:
import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 4, 4])
Atifnew = np.where(Atif ==4)
print(Atifnew)

import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Atifnew = np.where(Atif % 2 == 0)
print(Atifnew)


import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Atifnew = np.where(Atif % 2 == 1)
print(Atifnew)

#searchshorted()
import numpy as np
Atif = np.array([6, 7, 8, 9])
Atifnew = np.searchsorted(Atif, 9)
print(Atifnew)

import numpy as np
Atif = np.array([6, 7, 8, 9])
Atifnew = np.searchsorted(Atif, 7, side = 'right')
print(Atifnew)
