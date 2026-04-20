#it is used to describe the next time event that is like failure and success
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
Atif = random.exponential(scale = 2, size = (2, 3))
print(Atif)

sns.distplot(random.exponential(size = 100), hist = False)
plt.show()


