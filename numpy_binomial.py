#binomial Dist - discrete distribution
#parameter - n(number of trials), p(probablity), size(shape)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
Atif = random.binomial(n = 10, p=0.5, size = 20)
print(Atif)
sns.distplot(random.binomial(n=10, p=.5, size = 1000), hist = True, kde=False)
plt.show()



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=5, size = 1000), hist = False, label='normal')
sns.distplot(random.binomial(n=5,p=0.5, size = 1000), hist=False, label = 'binomial')
plt.show()