# hyperbolic function: numpy provides the ufuncs line sinh(),
# cosh() and tanh() that takes values in radians and produce the corresponding
# sin, cos and tan values.

# we will find the value of sinh of pi/2
import numpy as np
x = np.sinh(np.pi/2)
print(x)
print("End \n")


# finding cosh value in array.
sin1 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
sin_new = np.cosh(sin1)
print(sin_new)
print("End \n")


# Finding angles: We can also find angles : arcsinh(), arccosh() and arctanh() that takes
# values in radians and produce the corresponding sinh, cosh and tanh values.


# now finding angle 1.0
a = np.arcsinh(1.0)
print(a)
print("End \n")


# Angles of each tanh values in an array:
a1 = np.array([0.1, 0.2, 0.5])
a1_new = np.arctanh(a1)
print(a1_new)
print("End \n")


