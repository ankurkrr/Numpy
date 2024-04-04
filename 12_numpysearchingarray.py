# Searching array - you can search an array for a certain
# value and return the indexes that get the match. by using where()

import numpy as np
x = np.array([1, 2, 3, 4, 5, 4, 4])
x1 = np.where(x == 4)
print(x1)
print("End \n")


# Now we will find the indexes where the values are even:
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y1 = np.where(y % 2 == 0)
print(y1)
print("End \n")


# Now we wil find the indexes where the values are odd:
z = np.array([1, 2, 3, 4, 5, 6, 7, 8])
z1 = np.where(z % 2 == 1)
print(z1)
print("End \n")


# Searchsorted() - Perform binary search in array. return index
# We will now find the index where the value 7 should be inserted.
s = np.array([6, 7, 8, 9])
s1 = np.searchsorted(s, 7)
print(s1)
print("End \n")

# Now we will search from right side
s = np.array([6, 7, 8, 9])
s1 = np.searchsorted(s, 7, side="right")
print(s1)
print("End \n")


# How to search multiple value
m = np.array([1, 3, 5, 7])
m1 = np.searchsorted(m, [2, 4, 6])
print(m1)
print("End \n")
