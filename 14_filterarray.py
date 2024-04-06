# Getting some elements out of an existing array and
# creating a new array is called filtering.

# A boolean index list is a list of boolean corresponding
# to indexes in the array.

# Create an array from the element on index 0 to 2:

import numpy as np
x = np.array([41, 42, 43, 44, 45])
x1 = [True, False, True, True, False]
xfinal = x[x1]
print(xfinal)
print("End \n")


# Now we will create a filter array
# that will return only values higher then 42.
x = np.array([41, 42, 43, 44, 45])
filter_x = []
for i in x:
    if i > 43:
        filter_x.append(True)
    else:
        filter_x.append(False)

xnew = x[filter_x]
print(filter_x)
print(xnew)
print("End \n")

# Create a filter array that will return only even elements from
# the original array
e = np.array([1, 2, 3, 4, 5, 6, 7])
e_empty = []
for i in e:
    if i%2 == 0:
        e_empty.append(True)
    else:
        e_empty.append(False)
enew = e[e_empty]
print(e_empty)
print(enew)
print("End \n")


# Yes, you can also create filter directly from array
# That will return only values higher then 45
f = np.array([41, 42, 43, 44, 45])
f1 = f>42
ffinal = f[f1]
print(f1)
print(ffinal)
print("End \n")


# Yes, you can also create filter directly from array
# Create a filter array that will return only even elements from
# the original array
d = np.array([1, 2, 3, 4, 5, 6, 7])
d1 = d%2 == 0
d2 = d[d1]
print(d1)
print(d2)