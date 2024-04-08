# Arithmetic operators: +, -, /, *
#by using ufunc additional arguments like, where, dtype and out.

# we use add.
import numpy as np
x = np.array([10,11,12,13,14,15])
x1 = np.array([20,21,22,23,24,25])

x_add = np.add(x,x1)
print(x_add)

# We use substract
x_subs = np.subtract(x1,x)
print(x_subs)

# multiply
x_multiply = np.multiply(x,x1)
print(x_multiply)

# divide
x_div = np.divide(x,x1)
print(x_div)

# Power() function raises the value from the 1st array to the power of the value of 2nd array
# and return the results in a new array.
y = np.array([10,20,30,40,50,60])
y1 = np.array(([3,5,6,8,2,33]))
y_pow = np.power(y,y1)
print(y_pow)


# remainder - mod() and remainder() functions return the remainder of the 1st array
# corresponding to the 2nd array, result in new array.
r = np.array([10,20,30,40,50,60])
r1 = np.array(([3,5,6,8,2,33]))
rem = np.remainder(r,r1)
print(rem)

mod = np.mod(r,r1)
print(mod)


# quotaient and mod(remainder)
# This function return the both quotaient and mod.
q = np.array([10,20,30,40,50,60])
q1 = np.array(([3,5,6,8,2,33]))
quot = np.divmod(q,q1)
print(quot)


# Absolute() and abs() - do the same operation but here we should use absolute()
# to avoid confusion with python inbuilt function math.abs()
m = np.array([-1, -2, -3, -4, -5])
m1 = np.absolute(m)
print(m1)