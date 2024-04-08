# Rounding decimals: there are 5 ways of rounding off the decimals
# in numpy: truncate, fix, rounding, floor, ceil.

# truncation: trunc() and fix()
# here we are truncating the below array, these commands remove decimals and return the float number closest to zero.
import numpy as np
x = np.trunc([-3.1666, 3.999])
print(x)

# Fix example
f = np.fix([-3.1666, 3.999])
print(f)


# Rounding off : around() function increments preceding digit or decimal by nearest to 1. if n>5 = 1, if n<5 = 0
r = np.around(3.1666, 3)
print(r)


# floor() - round off the decimals of lower integers
y = np.floor([-3.1666, 3.6667])
print(y)

# ceil : opposite of floor
c = np.ceil([-3.999, 3.0001])
print(c)