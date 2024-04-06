# Unifrom dist - it is only made for probability(p)
# parameter - a(lower bound - 0.0), b(upper bound 1.0), size

from numpy import random
x = random.uniform(size=(2, 3))
print(x)

# Visualization of Uniform dist
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000),hist=False)
plt.show()
