#filter array
import numpy as np
Atif = np.array([41, 42, 43, 44])
emptyAtif = []
for i in Atif:
    if i > 42:
        emptyAtif.append(True)
    else:
        emptyAtif.append(False)

Atifnew = Atif[emptyAtif]
print(emptyAtif)
print(Atifnew)

import numpy as np
Atif = np.array([1, 2, 3, 4, 5, 6, 7])
emptyAtif = []
for i in Atif:
    if i % 2 == 0:
        emptyAtif.append(True)
    else:
        emptyAtif.append(False)
Atifnew = Atif[emptyAtif]
print(emptyAtif)
print(Atifnew)


# Alternate method
import numpy as np
Atif = np.array([41, 42, 43, 44])
Atifempty = Atif > 42
Atifnew = Atif[Atifempty]
print(Atifempty)
print(Atifnew)