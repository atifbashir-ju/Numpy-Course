#U-function: stands for universal function they are actually numpy function that operates on the nd array objects

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
    z.append(i+j)
print(z)

#with u function:
import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x,y)
print(z)


