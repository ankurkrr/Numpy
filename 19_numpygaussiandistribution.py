# Normal(Gaussian) Distribution - Very Important.
# random.normal() method- loc(), scale(standard deviation), size

# Generating a random normal distribution of size 2x3
from numpy import random
x = random.normal()
x = random.normal(size=(2, 3))
print(x)
print("End \n")

# Generate a random noraml distribution of size 2x3 with mean at 1 and standard deviation of 2:
from numpy import random
y = random.normal(loc=1, scale=2, size=(2, 3))
print(y)
print("End \n")

# Visualization of normal distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000),hist=False)
plt.show()

# Curve of a normal distribution is also called as bell curve
