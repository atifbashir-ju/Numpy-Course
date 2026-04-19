#reshaping: changing the shape of an array

import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
Atif1 = Atif.reshape(4, 3)
print(Atif1)


import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
Atif1 = Atif.reshape(2, 3, 2)
print(Atif1)


import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(Atif.reshape(2, 4).base)

# unknown dimensio
import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7, 8,])
Atif1 = Atif.reshape(2, 2, -1)
print(Atif1)
