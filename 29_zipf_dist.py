# Zipf dist: its definition is like...common word in english has occurs nearly 1/5 times
# as of the most hindi words.
# param - a defines as dist param, size

# Sample for zipf dist with a as 2 with size 2*3
from numpy import random
x = random.zipf(a=2, size=(2, 3))
print(x)

# Visualization of zipf dist.
import matplotlib.pyplot as plt
import seaborn as sns

x1 = random.zipf(a=2, size=1000)
sns.distplot(x1[x1<10], kde=False)
plt.show()