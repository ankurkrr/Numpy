# finding LCM(Lowest common multiplication)
# here we will find the LCM of the 2 numbers:

import numpy as np
x = 4
x1 = 6
x_new = np.lcm(x,x1)
print(x_new)
# the answer is 12 bcz lcm of both no. is 12


# finding lcm in array:
y = np.array([2,6,9])
y1 = np.lcm.reduce(y) # the reduce() method will use the ufunc,
# in this case the lcm() function on each element and it will
# reduce the array by 1 dimension
print(y1)



# we will find the LCM of all of an array where the array contains
# all integers from 1 to 10.
z = np.arange(1,11)
z1 = np.lcm.reduce(z)
print(z1)