# Permutation refers to an arrangement of elements like
# [3,2,1] is permutation of [1,2,3] and vice versa.

# numpy random module provides 2 methods : shuffling() and
# permutation().

# shuffle() method make changes to the original array
# randomly shuffling elements of the below array:
from numpy import random
import numpy as np
x = np.array([1,2,3,4,5])
random.shuffle(x)
print(x)
print(("End \n"))

# now we will generate a permutation of the elements for the
# below array.
# the permutation() method leaves the original array unchanged.
y = np.array([1,2,3,4,5])
random.permutation(y)
print(random.permutation(y))
