# Pareto Dist: 80:20 ratio. (20% factors cause 80% outcome or result)
# Param - a represents shape, size

# sample for pareto dist with shape 2 and size 2*3
from numpy import random
x= random.pareto(a= 2, size=(2, 3))
print(x)

# Visualization of pareto dist
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), hist=True, kde=False)
plt.show()