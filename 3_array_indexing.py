# 1-D Array indexing is the same as accessing an array element.
#start with 0, second 1

import numpy as np
x = np.array([1,2,3,4])
print(x[1])
print("")

# We can get the third and elements from adding them
a = np.array([1,2,3,4,5])
print(a[2]+a[3])
print("")

# Accessing 2-D it is like a row and columns.
b = np.array([[1,2,3,4,5,],[6,7,8,9,10]])
print("2nd and 5th element in the 1st row :",b[0,1], 'and 2nd row : ',b[1, 4])
print("")


# Accessing 3-D it is like a row and columns.
c = np.array([[[1,2,3], [4,5,6,], [7,8,9],[10,11,12]]])
print(c[0, 1, 1],c.ndim)






