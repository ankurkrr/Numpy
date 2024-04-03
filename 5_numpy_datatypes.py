# Datatypes in Python :-
# str, int, float, boolean, complex

# Datatypes in Numpy :-
# int = i,
# boolean = b,
# unsigned integer = u,
# float = f,
# complex = c,
# timedelta = m,
# datetime = M,
# object = O,
# string = S,
# Unicode string = U,
# memory = V

# Checking Datatype of Numpy array - dtype
import  numpy as np

x = np.array([1,2,3,4])
print(x.dtype)

# Checking Datatype of Numpy array - string

y = np.array(['apple','banana','grapes'])
print(y.dtype)


#   Creating array with a defined datatype:
a = np.array([1,2,3,4],dtype='S')
print(a)
print(a.dtype)
print('')


# Now we will Create an array with datatype of 4 byte int:
a = np.array([1,2,3,4],dtype='i4')
print(a)
print(a.dtype)
print('')


# if a type is given in which the elements cannot be casted
# then numpy will raised error. what if a value cannot be
# converted?
b = np.array(['1','2','3'],dtype='i')
print(b.dtype)
print('')


# Converting Data Type in existing array - astype()
d = np.array([1.1,2.1,3.1])
d1 = d.astype('i') #change float to int
print(d1)
print(d.dtype)
print(d1.dtype)
print('')

# Converting DataType from integer to boolean
d = np.array([1,0,3])
d1 = d.astype(bool)
print(d1)
print(d.dtype)
print(d1.dtype)
print('')