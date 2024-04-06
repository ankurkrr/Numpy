# Exponential Distribution: It is used for describing the time till next event is like failure or success.

# Param - scale(inverse of rate - lam == n*p), size

# Here we will draw a sample of a exponential dist. with 2.0 scale and 2*3 size.
from numpy import random
x = random.exponential(scale=2, size=(2, 3))
print(x)

# Visualization of exponential dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(scale=2, size=1000), hist=False)
plt.show()


#