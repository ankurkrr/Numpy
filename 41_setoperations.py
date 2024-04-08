# what is set? : set is collection of unique elements.

# for creating the set we use numpy's unique() to find the unique elements from any array:

# we will convert the array with repeated elements to a set
import numpy as np
x = np.array([1,1,2,2,3,4,5,5,6,7])
x1 = np.unique(x)
print(x1)
print("End \n")


# To find the unique value of 2 Diffrent 1-D array. we will use uniold() method.
u = np.array([1,2,3,4])
u1 = np.array([3,4,5,6])
u_new = np.union1d(u, u1)
print(u_new)
print("End \n")



# Finding intersection value : to find the only values that are present in both arrays,
# we use intersect1d() method.
i = np.array([1,2,3,4])
i1 = np.array([3,4,5,6])
i_new = np.intersect1d(i, i1, assume_unique=True)
print(i_new)
print("End \n")


# To find the only values that are in 1st set and NOT present in the 2nd set. we use
# setdiff1d()
s = np.array([1,2,3,4])
s1 = np.array([3,4,5,6])
s_new = np.setdiff1d(s, s1, assume_unique=True)
print(s_new)
print("End \n")




# To find the only values that are not present in both sets. we use
# setxor1d()
s = np.array([1,2,3,4])
s1 = np.array([3,4,5,6])
s_new = np.setxor1d(s, s1, assume_unique=True)
print(s_new)
print("End \n")
