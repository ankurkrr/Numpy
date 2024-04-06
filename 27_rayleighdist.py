# Rayleigh dist: It is used in Signal processing.
# Param - scale(standard deviation, how flat the distribution is..default 1.0), size

# sample for RL with scale 2.0 with size 2*3
from numpy import random
x = random.rayleigh(scale=2.0, size=(2, 3))
print(x)


# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist= False)
plt.show()