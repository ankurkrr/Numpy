# Products: use prod() function.
# here we will find the product of the element of the below array:
import numpy as np
x = np.array([1,2,3,4])
x1 = np.prod(x)
print(x1)



# finding the product of element in 2 Diffrent 1D array:
y = np.array([1,2,3,4])
y1 = np.array([5,6,7,8])
y_new = np.prod([y,y1]) # 1*2*3*4*5*6*7*8 = 40,320
print(y_new)



# product over an axis
z = np.array([1,2,3,4])
z1 = np.array([5,6,7,8])
z_new = np.prod([z,z1], axis=1)
print(z_new)



# Numpy cumulative product:
# example of partial product of [1,2,3,4] is [1,1*2, 1*2*3, 1*2*3*4] = [1,2,6,24] represented by cumprod().
c = np.array([5,6,7,8])
c_new = np.array([1,2,3,4])
c1 = np.cumprod(c)
c_new2 = np.cumprod(c_new)
print(c1)
print(c_new2)