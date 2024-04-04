# sort() - the numpy ndarray object has a function which is called
# sort(), and this will sort a specified array.

import numpy as np
x = np.array([3, 2, 4, 0, 1])
print(np.sort(x)) # This method is like a copy()
print("End \n")

# Sort the array alphabetically
s = np.array(['Banana', 'Apple', 'Cherry', 'Grapes'])
print(np.sort(s))
print("End \n")


# Sort the boolean array
b = np.array([True, False, True, False])
print(np.sort(b))
print("End \n")


#Sorting 2-D array
d2 = np.array([[3, 2, 4],[5,0,1]])
print(np.sort(d2)) # This method is like a copy()
print("End \n")


