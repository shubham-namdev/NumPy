
#~ Arithmetic Operations

import numpy as np

a = np.array([
[ 1 , 4 , 2 ],
[ 8 , 8 , 2 ]
])

print(a + 1) #>> adds 1 to each element
print(a - 1) #>> subtracts 1 from each element
print(a * 2) #>> multiplies each element with 2
print(a / 2) #>> divides each element by 2 

#>> Operations on multiple arrays

#! To apply these operations on multiple arrays their shape must be similar. Either the number of
#! rows or number of coloums must be similar. When the shape differs too much we get ValueErrors.

a = np.array([
[ 1 , 4 , 2 ],
[ 8 , 8 , 2 ]
])

b = np.array([
[ 1 , 2 , 3 ]
])

c = np.array([
[ 1 ],
[ 2 ]
])

d = np.array([
    [1 , 2 , 3, 4, 5],
    [1 , 2 , 3, 4, 5],
    [1 , 2 , 3, 4, 5],
    [1 , 2 , 3, 4, 5],
    [1 , 2 , 3, 4, 5]
])

print(a + b)

""" 
[[ 2  6  5]
 [ 9 10  5]]
"""

print(a + c)

"""
[[ 2  5  3]
 [10 10  4]]
"""
print(a + d)
#! ValueError: operands could not be broadcast together with shapes (2,3) (5,5)


#~ Mathematical Functions

#>> np.exp(a)  - takes e to the power of each value
#>> np.sin(a)  - returns sine of each value
#>> np.cos(a)  - returns cosine of each value
#>> np.tan(a)  - returns tangent of each value
#>> np.log(a)  - returns logarithm of each value
#>> np.sqrt(a) - returns square root of each value


#~ Aggregate Functions

#>> a.sum()  - returns sum of all values in array
#>> a.min()  - returns lowest value in array
#>> a.max()  - return maximum value in array
#>> a.mean() - returns mean of all values in array
#>> np.median(a) - returns meanian of values of array
#>> np.std(a) - returns standard deviation of values in array
