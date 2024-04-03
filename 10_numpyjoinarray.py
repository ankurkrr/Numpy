# Joining the numpy array - here for this we will pass concatenate

import numpy as np
x = np.array([1,2,3])
x1 = np.array([4,5,6])
x2 = np.concatenate((x,x1))
print(x2)
print("end \n")

# Joining of 2-D arrays along with rows(axis=1)
y = np.array([[1,2],[3,4]])
y1 = np.array([[5,6],[7,8]])
y2 = np.concatenate((y,y1),axis=1)
print(y2)
print("End \n")


# Joining array using the stack function
s = np.array([1,2,3])
s1 = np.array([4,5,6])
s2 = np.stack((s,s1),axis=1)
print(s2)
print("end \n")


#Stacking along with rows: hstack()
h = np.array([1,2,3])
h1 = np.array([4,5,6])
h2 = np.hstack((h,h1))
print(h2)
print("end \n")


# Stacking along with column
v = np.array([1,2,3])
v1 = np.array([4,5,6])
v2 = np.vstack((v,v1))
print(v2)
print("end \n")

# Stacking along with Height or Depth
d4 = np.array([1,2,3])
d5 = np.array([4,5,6])
d6 = np.dstack((d4,d5),axis=1)
print(d6)
print("end \n")









