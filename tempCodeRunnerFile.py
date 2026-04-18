import numpy as np
Atif = np.array([41, 42, 43, 44])
Atifempty = Atif > 42
Atifnew = Atif[Atifempty]
print(Atifempty)
print(Atifnew)