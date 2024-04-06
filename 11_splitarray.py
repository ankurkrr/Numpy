# Spliting arrays in numpy - it is reverse to
# joining, breaking the array.

# array_split()
# split the array in 3 parts
import numpy as np
x = np.array([1,2,3,4,5,6])
x1 = np.array_split(x,3)
print(x1)
print("End \n")

# Split in 4 parts
x = np.array([1,2,3,4,5,6])
x1 = np.array_split(x,4)
print(x1)
print("End \n")

# Split into array
y = np.array([1,2,3,4,5,6])
y1 = np.array_split(y,3)
print(y1[0])
print(y1[1])
print(y1[2])
print("End \n")


# Splitting the 2-D array
d2 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
d21 = np.array_split(d2, 3)
print(d21)
print("End \n")


# Split the 2-D array into three 2-D array
d2 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
d21 = np.array_split(d2, 3)
print(d21)
print("End \n")



# Splitting the 2-D into three 2-D along the rows
r = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
r1 = np.array_split(r, 3, axis=1)
print(r1)
print("End \n")


# Alternate solution using hsplit(), opposite hstack()
h = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
h1 = np.hsplit(h, 3)
print(h1)
print("End \n")

v = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
v1 = np.vsplit(v, 3)
print(v1)