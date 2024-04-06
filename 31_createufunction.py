# To create the ufunction, we have to define a function like you do in normal function
# in python,then you add it to  the numpy with frompyfunc() method.

# Arguments of frompy func() : function, inputs, outputs

# Create your own ufunc for addition:
import numpy as np
def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4],[5,6,7,8]))


# Checking if this function is ufunc or not:
print(type(np.add))


# Concatenate
print(type(np.concatenate))



# What if ufunc does not exist:
##print(type(np.sdfdfs))




# use an if statement to check if the function is ufunc or not.
if type(np.add) == np.ufunc:
    print("Yes this function is u func")
else:
    print("this function is not a ufunc")