# Slicing array - slicing in python means taking elements
# from one give index to another index

#[start:end], [start:end:steps]

# Now we will slice an element from 1 to 5 :

import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
print(x[1:5])
print('')


#Now we will slice an element from 4 to end
print(x[3:])
print('')


# Now we will slice the element from the beginning to index
print(x[:4])
print('')


# Negative slicing - index 3 to end
print(x[-3:-1])
print('')

#Step : you will use step value to determine the step of the slicing
# return every other value from index 1 to 5

print(x[1:5:2])
print('')

# now return every other number from the entire array
print(x[::3])
print('')

# Slicing 2-D array : print 7,8,9
y = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(y[1,1:4])
print('')


# another example
print(y[0:2, 2])
print('')


#another example tough 2-D : print from both, index 1:4
print(y[0:2,1:4])
print('')



#In 3-D
a3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print("In 3-D")
print(a3[0,0:2,1])