#poisson: it estimates how many time an event can happen.

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
Atif = random.poisson(lam=2, size =10)
print(Atif)

#visulization
sns.distplot(random.poisson(lam = 2, size =100), kde = False)
plt.show()



import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale = 7, size =1000), hist= False, label = 'normal')
sns.distplot(random.poisson(lam=50, size = 1000), hist = False, label = 'poisson')
plt.show()
