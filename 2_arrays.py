import numpy as np

# Now we will create numpy ndarray object
# The array object in numpy is called ndarray
# array()

a = np.array([1,2,3,4,5])
print(a)
print(type(a))
print("")

# we can also pass a list, tuple or any array like object
# with array() method and it wil be converted to ndarray.

b= np.array((1,2,3,5,6))
print(b)
print(type(b))
print("")

# Dimension in Arrays - a dimension in array is one level of array depth(nested array)

# 0-D arrays - scalers, are the elements in array, each value in an array is a 0-D array.

# Now we will create 0-D array with value 42

c = np.array(42)
print(c)
print("")

# 1D arrays - an array that has 0-D arrays as its elements is called uni dimensional or 1-D
d = np.array([1,2,3,4,5])
print(d)
print("")

# 2-D array - contain 2 arrays with certain values.

d2 = np.array([[1,2,3],[4,5,6]])
print(d2)
print("")

# Now we will create a 3-D array with two 2-D array.
d3 = np.array([[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]]])
print(d3)
print(d3.ndim) # Check dimensions of the array have : ndim
print("")

# Create an array with 5 dimensions and verify that it has 5 dimensions
d5 = np.array([1,2,3,4,5],ndmin=5)
print(d5)
print("No. Of Dimensions : ", d5.ndim)

