#rayleigh distribution it is used in signal processing

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
Atif = random.rayleigh(scale = 2, size =(2, 3))
print(Atif)
sns.distplot(random.rayleigh(size = 1000), hist=False)
plt.show()


