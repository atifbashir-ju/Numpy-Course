import numpy as np
Atif = np.array([[1, 2, 3, 4], [5, 6, 7, 9]])
for i in np.nditer(Atif[:, ::2]):
    print(i)

