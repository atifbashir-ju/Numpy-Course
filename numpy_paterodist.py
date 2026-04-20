#petro distribution: 80:20 ratio (20% factors cause 80 outcome)
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 
Atif = random.pareto(a =2, size = (2, 3))
print(Atif)
sns.distplot(random.pareto(a = 2, size = 1000), kde = False)
plt.show()