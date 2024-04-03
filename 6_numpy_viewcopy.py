# Diffrence between numpy and array copy view
# we will make a copy, change in original array, and display both.
import numpy as np
x = np.array([1,2,3,4,5])
x1 = x.copy()
x1[0] = 12
print(x)
print(x1)
print(" ")

# Now we will make a view, change original, display both
y = np.array([1,2,3,4,5])
y1 = y.view(),
y[0] = 62
print(y)
print(y1)
