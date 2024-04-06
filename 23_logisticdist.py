# Logistic dist - Describe growth it is basically important in regression and neural network.
# parameter - loc(mean = 0), scale(standard deviation, 1), size

# Draw 2*2 sample of logistic with mean at 1 and standard deviation = 2.0
from numpy import random
x = random.logistic(loc=1, scale=2, size=(2,3))
print(x)


# Visualization of logistic dist
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False, label="logistic")
sns.distplot(random.normal(size=1000),hist=False, label="normal")
plt.show()