# diffrence: use diff() function for finding the diffrence
# Example: [1,2,3,4], the discrete diffrence of this would be [2-1, 3-2, 4-3] = [1,1,1] by using diff()
import numpy as np
x = np.array([10,15,25,5]) # [5, 10, -20] bcz 15-10=5, 25-15=10, 5-25=-20
x_new = np.diff(x)
print(x_new)