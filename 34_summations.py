# summations: diffrence: addition is done between 2
# arguments whereas summation happens over n elements.

# adding the 2 array.
import numpy as np
x = np.array([1,2,3])
x1 = np.array([1,2,3])
x2 = np.add(x, x1)
print(x2)


# sum the value in 2 array:
y = np.array([1,2,3])
y1 = np.array([1,2,3])
y2 = np.sum([y, y1])
print(y2)


# summation over an axis: if you specify axis=1,
# numpy will sum the number in each group
z = np.array([1,2,3])
z1 = np.array([1,2,3])
z2 = np.sum([z, z1], axis=1)
print(z2)


# Cummulative sum: means partially adding the elements in array.
# example: [1,2,3,4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10]
# Represent by cumsum()
c = np.array([1,2,3])
c1 = np.cumsum([1,2,3])
print(c1)