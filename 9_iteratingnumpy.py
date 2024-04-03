# Iterating array - means going through the elements one by one
# or step by step. like for loop

# Iterate the element of 1-D
import numpy as np
x = np.array([1,2,3])
for i in x:
    print(i)
print("End \n")

# Iterate 2D
y = np.array([[1,2,3],[4,5,6]])
for i in y:
    print(i)

#Iterate on each element
z = np.array([[1,2,3],[4,5,6]])
for i in z:
    for a in i:
        print(a)
print("end \n")


# Iterate a 3-D
d3 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in d3:
    for a1 in i:
        for a2 in a1:
            print(a2)
print("End \n")


# Iterating arrays using the nditer() function
# Now we wil iterate on each scaler element.
d4 = np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(d4):
    print(i)
print("End \n ")


# Now we will Iterate with diffrent step sizes
d1 = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(d1[:, ::2]):
    print(i)

