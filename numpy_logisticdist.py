#logistic dist: describe growth it is basically imp in regression and neural network

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

Atif = random.logistic(loc = 1, scale = 2, size = (2, 3))
print(Atif)

sns.distplot(random.logistic(size=1000), hist = False)
plt.show()