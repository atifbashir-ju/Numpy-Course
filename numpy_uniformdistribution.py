#uniform distribution: it is used for probability(p)

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
Atif = random.uniform(size = (2, 3))
print(Atif)

sns.distplot(random.uniform(size = 1000), hist = False)
plt.show()