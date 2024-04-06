# Multinomial dist: it is a generalization of binomial dist.

# Param - n(number of outcome or possibility), pvals(list of possibility or outcome), size

# draw out a sample for dice roll
from numpy import random
x= random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

# Multinomial samples will not produce a single value, they will produce one value for each pvals.
