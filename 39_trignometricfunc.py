# Trigonometric function: numpy provides the unfunc line sin(), cos() and tan() that takes
# values in radians and produce the corresponding sin, cos and tan values.

# Example : now we will find the sin value of pi/2
import numpy as np
sin = np.sin(np.pi/2)
print(sin)
print("End \n")



# now finding the sin value of an array
import numpy as np
sin1 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
sin_new = np.sin(sin1)
print(sin_new)
print("End \n")


# converting degree into radians: by default all of the trignometric functions radians as parameter.

# note: radians values are pi/180* degree value.

# Example: converting all the array values to radians:
import numpy as np
x = np.array([90, 180, 270, 360])
x_new = np.deg2rad(x)
print(x_new)
print("End \n")


# here we will convert the radian into degree.
import numpy as np
y = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
y_new = np.rad2deg(y)
print(y_new)
print("End \n")



# We can also find angles : arcsin(), arccos() and arctan() that takes
# values in radians and produce the corresponding sin, cos and tan values.

# now finding angle 1.0
a = np.arcsin(1.0)
print(a)
print("End \n")


# Angles of each values in an array:
a1 = np.array([1, -1, 0.1])
a1_new = np.arcsin(a1)
print(a1_new)
print("End \n")


# Here we can also find the hypotaneous using the pythogoras theorem
# hypot() functions that takes values in radians and produce the corresponding sin, cos and tan values.

# we will find the hypot for 3 base and 4 perpendicular.
base = 3
perp = 4
h = np.hypot(base, perp)
print(h)
print("End \n")
