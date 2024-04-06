# matplotlib(pyplot) - seaborn
# seaborn is a library that uses matplotlib underneath to plot graph i.e pyplot.
# Distplot - distribution plot

import matplotlib.pyplot as plt
import seaborn as sns
#sns.distplot([0,1,2,3,4,5])
#plt.show()

#plotting a distplot without a histogram
#sns.distplot([0,1,2,3,4,5], hist=False)
#plt.show()

x = [0,1,2,3,4,5]
sns.distplot(x, hist=False)
plt.show()