#normal(Gussain) Distribution
from numpy import random
Atif = random.normal(size = (2, 3))
print(Atif)

from numpy import random
Atif = random.normal(loc = 1, scale =2, size=(2,3))
print(Atif)
#visualization
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
sns.distplot(random.normal(size = 1000), hist = False)
plt.show()