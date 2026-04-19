#multinomial: it is a genralization of binomial distribution
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

Atif = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(Atif)
