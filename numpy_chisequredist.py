import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
Atif = random.chisquare(df = 2, size = (2, 3))
print(Atif)
sns.distplot(random.chisquare(df = 1, size = 1000), hist = False)
plt.show()