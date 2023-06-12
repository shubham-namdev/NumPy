import numpy as np

#~ Shape Manipulation Function
#>> Allow us to restructure our array without changing their values

a = np.array([
    [1,2,3,4,5],
    [7,8,9,4,5],
    [1,4,7,2,5]
])

#>> a.reshape(x, y) - returns array with same values structured in different shape
#>> a.flatten()     - returns flattened one dimentions copy of array
#>> a.ravel()       - Does the same as flatten but works with the actual array instead of a copy
#>> a.transpose()   - returns array with same values but swapped dimentions
#>> a.swapaxex()    - return array with same values but swapped axes
#>> a.flat          - iterator for flattened version of array

#? Both swapaxes and transpose provide similar functionality but with different syntax and usage.


#~ Joining Functions
#>> Used to cumbine multiple arrays into one array

#>> np.concatenate(a, b) - joins a and b along an existing axis
#>> np.stack(a, b)       - joins a and b along new axis
#>> np.hstack(a, b)      - stacks arrays horizontally (column-wise)
#>> np.vstack(a, b)      - stacks arrays vertically (row-wise)

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

#print(np.concatenate((a, b))) #? [10 20 30 40 50 60]

#print(np.stack((a, b)))
"""
[[10 20 30]
 [40 50 60]]
"""
#print(np.hstack((a, b))) #?[10 20 30 40 50 60]

#print(np.vstack((a, b)))
"""
[[10 20 30]
 [40 50 60]]
"""


#~ Splitting Functions
#>> used to split arrays into multiple sub-arrays.

#>> np.split(a, k) - splits array a int k sub-arrays
#>> np.hsplit(a, k) - splits array a int k sub-arrays horizontally (column-wise)
#>> np.vsplit(a, k) - splits array a int k sub-arrays vertically (row-wise)


a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

#print(np.split(a, 2)) #? [array([[10, 20, 30, 40]]), array([[50, 60, 70, 80]])]

#print(np.hsplit(a, 2))
"""[array([[10, 20],
           [50, 60]]), 
    array([[30, 40],
           [70, 80]])]
"""

#print(np.vsplit(a, 2)) #? [array([[10, 20, 30, 40]]), array([[50, 60, 70, 80]])]



#~ Adding and Removing

#>> np.resize(a, (x, y))      - returns resized version of array 'a' and fills empty spaces with repeating copy of
#>> np.append(a, [values...]) - appends value  at the end of the array
#>> np.insert(a, x, values)   - appends value at the index 'x' of array
#>> np.delete(a, x, y )       - deletes axes of array

a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

print(np.append(a, [100, 200, 300])) #? [ 10  20  30  40  50  60  70  80 100 200 300]

print(np.insert(a, 0, [4, 5])) #? [ 4  5 10 20 30 40 50 60 70 80]

print(np.delete(a, 0, 1))
"""
[[20 30 40]
 [60 70 80]]
"""

