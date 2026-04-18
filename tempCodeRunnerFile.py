import numpy as np
Atif = np.array([1, 3, 5, 7])
Atifnew = np.searchsorted(Atif, [2,4,6])
print(Atifnew)