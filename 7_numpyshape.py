# Shape of an array - The shape of an array is the
# number of elements in each dimensions.

# Now we will try to get shape of an array.
import numpy as np
x = np.array([[1,2,3,4],[5,6,7,8]])
print(x.shape) #(2,4) which means 2 dim array and 4 elements
print(" ")

# Now we will create 5-d array using ndim
d5 = np.array([1,2,3,4,6],ndmin=5)
print(d5)
print('Shape of array is', d5.shape)
