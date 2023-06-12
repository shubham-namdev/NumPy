"""
-> NumPy
It is essential for the efficient management of arrays and linear algebra.
"""

import numpy as np

#>> Creating Arrays 
a = np.array([10, 20, 30, 40])

#>> Multi-Dimensional Arrays
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
], dtype=int)


#~ Filling Arrays

#>> Full Function - Fill array of certain shape with same number

a = np.full((3, 4, 5), 7) # 3 * 4 * 5 matrix filled with 7

#>> Zeros - fill with zero

a = np.zeros((4, 4))

#>> Ones - fill with ones

a = np.ones((5, 5, 4))

#>> Empty - empty array of given dimensions

a = np.empty((5, 5))

#>> random - array of random numbers

a = np.random.random((4, 4))

#>> arange() function - creates list of values that range from min to max. Step size have to be given.

a = np.arange(10, 100, 15) # (min, max, step_size)
#? [10 25 40 55 70 85]

#>> linspace() function - creates same list from min to max but in place of step size, we have to give the amount of
#>>                       numbers we want. They will spread evenly and have same distance to their neighbour.

a = np.linspace(0, 100, 11) # (min, max, amount)
#? [  0.  10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]

#! NaN - Not a Number
#>> Used as a placeholder for empty spaces. It indcates something is missing at that place. 


#~ Attributes of arrays

import numpy as np

a = np.zeros((3, 4, 5))
print(a)

#>> a.shape - returns shape - (3, 4, 5) : tuple
#>> a.ndim  - returns number of dimensions - 3 : int
#>> a.size  - returns amount of elements in array - 60 : int
#>> a.dtype - returns data type of values in arrat - float64 by default

print(a.dtype)
