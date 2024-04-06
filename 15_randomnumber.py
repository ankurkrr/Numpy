# Random - Something that cannot be predicted logically

# Now we will generate a random no. from 0 to 100

#import numpy as np
from numpy import random
x = random.randint(400)
print(x)
print("End \n")


# You can also generate float() via rand()
y = random.rand()
print(y)
print("End \n")

# Generate Random array
# We will generate a 1-D array containing 5 random int
# from 0 to 100
d1 = random.randint(100, size=(5))
print(d1)
print("End \n")


# Generate Random array
# We will generate a 2-D array with 3 rows, each row
# containing 5 random int from 0 to 100
d2 = random.randint(100, size=(3, 5))
print(d2)
print(d2.ndim)
print("End \n")


# Generating float array.
# We will generate a 1-D array containing 5 random float.
f1 = random.rand(5)
print(f1)
print("End \n")


# We will generate a 2-D array with 3 rows each containing
# 5 random float.
f2 = random.rand(3, 5)
print(f2)
print("End \n")


# Generate random no. from an array using
# choice() method
a = random.choice([3,5,7,9,1,4])
print(a)
print("End \n")


# Generate random no. from a 2-D array using
# choice() method
a2 = random.choice([3,5,7,9,1,4],size=(3, 5))
print(a2)



