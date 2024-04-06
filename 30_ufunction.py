# Ufunction : Stands for universal function and the are actually numpy functions
# that operates on the ndarray objects.

# ufunc also takes additional arguments like, where, dtype and out.

# Vectorization - converting the iterative statements into a vector based statements.

# Example without ufunc here we will use python inbuilt zip().
x = [1,2,3,4]
y = [4,5,6,7]
z = []

for i, j in zip(x,y):
    z.append(i+j)
print(z)

# Example with ufunc, using add() function:
import numpy as np
x = [1,2,3,4]
y = [4,5,6,7]
z1 = np.add(x, y)
print(z1)