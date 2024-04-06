# Poisson Dist - It estimates how many times an event can happen.

# Parameters - lam(number of occurance or rate), size

# Generate a random 1*10 dist for the occurance 2
from numpy import random
x = random.poisson(lam=2, size=10)
print(x)

# Visualization of poisson dist
import matplotlib.pyplot as plt
import seaborn as sns

"""sns.distplot(random.poisson(lam=2, size=1000),kde=False)
plt.show()"""

# Presenting both hte plot in same figure normal and poisson dist.
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label="Normal")
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label="Poisson")
plt.show()

# n*p == lam