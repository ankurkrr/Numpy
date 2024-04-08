# finding GCD(greatest common denominator), also known as HCF(Highest common factor)

# Here we will find hcf of the below 2 numbers:
import numpy as np
x = 6
x1 = 9
x_new = np.gcd(x,x1)
print(x_new)


# Finding the GCD in array
# the reduce() method will use the ufunc,
# in this case the gcd() function on each element and it will
# reduce the array by 1 dimension.
y = np.array([28,8,32,16,36])
y1 = np.gcd.reduce(y)
print(y1)