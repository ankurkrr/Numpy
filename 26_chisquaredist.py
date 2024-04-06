# Chi Square Dist: it is basically used as basis to verify the hypotheses.

#param - df(degree of freedom), size

# sample for chi squared dist with df 2 with size 2*3
from numpy import random
x = random.chisquare(df=2, size=(2, 3))
print(x)

# Visualization of chi square
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=500), hist=False)
plt.show()