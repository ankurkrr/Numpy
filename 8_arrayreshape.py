# reshaping - changing the shape of an array, like adding or removing the elements.

#reshaping from 1-D to 2-D
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(4,3)
print(x1)
print("End\n")

# reshaping from 1-D to 3-D
x2 = x.reshape(2,3,2)
print(x2)
print("End\n")

y = np.array([1,2,3,4,5,6,7,8])
y1 = y.reshape(2,2,2)
print(y1)
print("End\n")


# Return copy or view
z = np.array([1,2,3,4,5,6,7,8])
print(z.reshape(2,4).base)
print("End\n")

# Unknown Dimension - you r only allowed to have one unknown dimension. pass -1.
u = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
u1 = u.reshape(2,2,-1)
print(u1)
print("End \n")


# Flattening the array by converting multidimensional array
# into 1-D
d = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
d1 = d.reshape(-1)
print(d1)
print("End \n")

# There are alot of functions for changing the shape of an
# array in numpy. like flatten, ravel and also rearranging
# the element rot90, flip, fliplr, flipud. they are actually
# come under advance numpy.
