# Binomial dist - discrete dist - binary output.
# param - n(number of trials), p(probability), size(shape-returned array)

# given 10 trials for a coin which will generate 10 data points:

from numpy import random
"""x = random.binomial(n=10, p=0.5, size=10)
print(x)"""

# Visualization of binomial dist
import matplotlib.pyplot as plt
import seaborn as sns
"""sns.distplot(random.binomial(p=0.5, n=10, size=1000),hist=True, kde=False)
plt.show()"""


# Diffrence between normal and binomial : Normal - Continous and Binomial - Discrete

# Always use 100 datapoints for normal and 500 datapoints for binomial

sns.distplot(random.normal(loc=50, scale=5, size=100), hist=False, label= "Normal")
sns.distplot(random.binomial(n=100, p=0.5, size=500), hist=False, label="Binomial")
plt.show()
