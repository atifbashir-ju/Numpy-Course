#numpy array copy vs view

#we will make copy firt
import numpy as np
Atif = np.array([1, 2, 3, 4, 5])
Atif1 = Atif.copy()
Atif[0] = 42
print(Atif)
print(Atif1)

#will make now view
import numpy as np
Atif = np.array([1, 2, 3, 4, 5])
Atif1 = Atif.view()
Atif[0] = 42
print(Atif)
print(Atif1)

